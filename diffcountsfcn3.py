import os

from xrd_fileIO_fcns import *
#from xrd_math_fcns import *
#from xrdPLOT import *
from xrd_diffraction_conversion_fcns import *

import time, copy
import os
import sys
import numpy
import h5py
import pylab


#h5path='E:/temp2011Oct02D_Bi.h5'
#p='E:/temp2011Oct02D_Bi.h5'
#
#segind=4
#cell=20
#
#f=h5py.File(p, mode='r')
#
#h5groupstr='84'
#sourcespec='84'
#diffdict={}
#diffdict['sourcepath']=p
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(38, 56)

def calcdiffimage_blin(h5g, pointind, icname='IC3', plotbool=False, calcarr=True):
    plotbool=plotbool and calcarr
    pntl=[h5g['analysis/area_detector/blin0'], h5g['analysis/area_detector/blin1']]
    dl=[]
    for pnt in pntl:
        d={}
        sp=pnt.attrs['sourcefile']
        if 'attrs_maps' in sp:
            f=CHESSRUNFILE()
            closebool=True
        elif pnt.file.filename.strip('/')==sp.strip('/'):
            f=pnt.file
            closebool=False
        else:
            f=h5py.File(sp, mode='r')
            closebool=True
        ds=f[pnt.attrs['sourcename']]
        if calcarr:
            if isinstance(pnt.attrs['sourcearrayindex'], int):
                d['x']=ds[pnt.attrs['sourcearrayindex'], :, :]
            elif isinstance(pnt.attrs['sourcearrayindex'], numpy.ndarray):
                d['x']=ds[pnt.attrs['sourcearrayindex'][pointind], :, :]
            else:
                d['x']=ds[:, :]
        if isinstance(ds.attrs['subexposures'], (int, long)):
            d['n']=float(ds.attrs['subexposures'])
        elif isinstance(ds.attrs['subexposures'], numpy.ndarray):
            d['n']=float(ds.attrs['subexposures'][pointind])
        else:
            print 'cannot find subexposures for ', ds.name
        if not (icname in ds.attrs.keys()):
            try:
                d['c']=ds.parent.parent['scalar_data'][icname][pointind]
            except:
                print 'cannot find IC for ', ds.name
                raise
        elif isinstance(ds.attrs[icname], float):
            d['c']=ds.attrs[icname]
        elif isinstance(ds.attrs[icname], numpy.ndarray):
            d['c']=ds.attrs[icname][pointind]
        else:
            print 'cannot find IC for ', ds.name
        dl+=[d]
    if closebool:
        f.close()
    ds=h5g['measurement/area_detector/counts']
    if isinstance(ds.attrs['subexposures'], (int, long)):
        n=float(ds.attrs['subexposures'])
    elif isinstance(ds.attrs['subexposures'], numpy.ndarray):
        n=float(ds.attrs['subexposures'][pointind])
    else:
        print 'cannot find subexposures for ', ds.name
    ds=h5g['measurement/scalar_data'][icname]
    c=ds[pointind]
    w0calc=lambda n0, c0, n1, c1, n, c:(c-c1*n/n1)/(c0-c1*n0/n1)
    w1calc=lambda n0, w0, n1, n:(n-w0*n0)/n1
    try:
        w0=w0calc(dl[0]['n'], dl[0]['c'], dl[1]['n'], dl[1]['c'], n, c)
        w1=w1calc(dl[0]['n'], w0, dl[1]['n'], n)
    except:#if divide by zero problem then trasnpose the indeces
        w1=w0calc(dl[1]['n'], dl[1]['c'], dl[0]['n'], dl[0]['c'], n, c)
        w0=w1calc(dl[1]['n'], w1, dl[0]['n'], n)
    if calcarr:
        b=w0*numpy.float32(dl[0]['x'])+w1*numpy.float32(dl[1]['x'])
    if plotbool:
        pylab.figure()
        pylab.subplot(311)
        pylab.imshow(dl[0]['x'], interpolation='nearest')
        pylab.title('num exp: %d, IC: %.2e, wt: %.2e' %(dl[0]['n'], dl[0]['c'], w0))
        pylab.colorbar()
        pylab.subplot(312)
        pylab.imshow(dl[1]['x'], interpolation='nearest')
        pylab.title('num exp: %d, IC: %.2e, wt: %.2e' %(dl[1]['n'], dl[1]['c'], w1))
        pylab.colorbar()
        pylab.subplot(313)
        pylab.imshow(b, interpolation='nearest')
        pylab.title('num exp: %d, IC: %.2e, w0n0+w1n1: %.2e, w0c0+w1c1: %.2e' %(n, c, w0*dl[0]['n']+w1*dl[1]['n'], w0*dl[0]['c']+w1*dl[1]['c']))
        pylab.colorbar()
    if calcarr:
        return b, w0, w1
    else:
        return w0, w1

def calcdiffcounts_lin(h5path, h5groupstr, savename='imcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, intplotallbool=False, icountsbool=True):
    isavename='i'+savename

    if savebool:
        h5file=h5py.File(h5path, mode='r+')
    else:
        h5file=h5py.File(h5path, mode='r')
    h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
    h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
    h5marcounts=h5file['/'.join((h5groupstr,'measurement', getxrdname(h5analysis), 'counts'))]
    pointlist=h5analysis.attrs['pointlist']
    if savebool:
        if savename in h5mar:
            del h5mar[savename]
        diffcounts=h5mar.create_dataset(savename, h5marcounts.shape, dtype=numpy.dtype('float32'))
        if 'diffimage' in h5mar:
            del h5mar['diffimage']
        diffimage=h5mar.create_dataset('diffimage', h5marcounts.shape, dtype=numpy.dtype('float32'))
    else:
        diffcounts=numpy.zeros(h5marcounts.shape, dtype='float32')
        diffimage=numpy.zeros(h5marcounts.shape, dtype='float32')
    weights0=numpy.zeros(h5marcounts.shape[0], dtype='float32')
    weights1=numpy.zeros(h5marcounts.shape[0], dtype='float32')
    for pointind in pointlist:
        print pointind
        b, w0, w1=calcdiffimage_blin(h5file[h5groupstr], pointind, plotbool=plotbool)
        weights0[pointind]=w0
        weights1[pointind]=w1
        diffimage[pointind, :, :]=b[:, :]
        diffcounts[pointind, :, :]=h5marcounts[pointind, :, :]-b[:, :]
        if plotbool:
            pylab.figure()
            pylab.imshow(diffcounts[pointind, :, :], interpolation='nearest')
            pylab.colorbar()
            break
    if savebool:
        diffimage.attrs['weights0']=weights0
        diffimage.attrs['weights1']=weights1
        diffimage.attrs['source0']='blin0'
        diffimage.attrs['source1']='blin1'
    h5file.close()

    if intbool:
        
        h5file=h5py.File(h5path, mode='r')
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]

        imap, qgrid=getimapqgrid(h5analysis.attrs['imapstr'])
        dqchiimage=None
        slots=numpy.uint16(qgrid[2])
        killmap=getkillmap(h5analysis.attrs['killmapstr'])
        imap*=killmap

        h5file.close()
        h5file=h5py.File(h5path, mode='r+')
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
        h5marcounts=h5file['/'.join((h5groupstr,'measurement', getxrdname(h5analysis), 'counts'))]
        diffcounts=h5mar[savename]
        if isavename in h5mar:
            del h5mar[isavename]
        idcounts=h5mar.create_dataset(isavename, data=numpy.zeros((diffcounts.shape[0], qgrid[2]), dtype='float32'))
        idcounts.attrs['qgrid']=qgrid
        for pointind in pointlist:
            print 'idcounts', pointind
            data=diffcounts[pointind, :, :]
            idcounts[pointind, :]=intbyarray(data, imap, dqchiimage, slots, mean=True)[:]
            if intplotbool:
                pylab.figure()
                pylab.plot(idcounts[pointind, :])
                pylab.colorbar()
                break
        if icountsbool:
            isavename2='icounts'
            if isavename2 in h5mar:
                del h5mar[isavename2]
            icounts=h5mar.create_dataset(isavename2, data=numpy.zeros((h5marcounts.shape[0], qgrid[2]), dtype='float32'))
            icounts.attrs['qgrid']=qgrid
            for pointind in pointlist:
                print 'icounts', pointind
                data=h5marcounts[pointind, :, :]
                icounts[pointind, :]=intbyarray(data, imap, dqchiimage, slots, mean=True)[:]
        h5file.close()
        
        if intplotallbool:
            h5file=h5py.File(h5path, mode='r')
            h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
            h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
            pointlist=h5analysis.attrs['pointlist']
            arr=h5mar[isavename][:, :]
            h5file.close()
            pylab.figure()
            for pointind in pointlist:
                pylab.plot(arr[pointind])

    if plotbool or (intbool and (intplotbool or intplotallbool)):
        pylab.show()

def calcdiffcounts_lin1d(h5path, h5groupstr, savename='imcounts', sourcename='icounts', savebool=True, plotbool=False, fraczeroed=0.03, fprecision=[.1, .01, 0.0005], scalarname='IC3', refineduringloop=True, maxtries=1000):#no gui interface
#icounts assumed to be raw integration of counts with only outlier removal performed
    h5file=h5py.File(h5path, mode='r')
    h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
    h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
    icounts=readh5pyarray(h5mar[sourcename])
    pointlist=h5analysis.attrs['pointlist']
    attrdict=getattr(h5path, h5groupstr)
    

    weights0=numpy.zeros(icounts.shape[0], dtype='float32')
    weights1=numpy.zeros(icounts.shape[0], dtype='float32')
    for pointind in pointlist:
        print pointind
        w0, w1=calcdiffimage_blin(h5file[h5groupstr], pointind, plotbool=False, calcarr=False)
        weights0[pointind]=w0
        weights1[pointind]=w1

    h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
    h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]

    kms=attrdict['killmapstr'].rpartition('/')[2]
    ims=attrdict['imapstr'].rpartition('/')[2]
    
    blin0_name=h5mar['blin0'].attrs['sourcename']
    a, b, c=blin0_name.rpartition('/')
    blin0_1dpath='/'.join((a, ims, kms, c))
    blin0_inds=h5mar['blin0'].attrs['sourcearrayindex']
    if isinstance(blin0_inds, int):
        blin0_processtype=1
    elif isinstance(blin0_inds, numpy.ndarray):
        blin0_processtype=2
    else:
        blin0_processtype=0
    
    blin1_name=h5mar['blin1'].attrs['sourcename']
    a, b, c=blin1_name.rpartition('/')
    blin1_1dpath='/'.join((a, ims, kms, c))
    blin1_inds=h5mar['blin1'].attrs['sourcearrayindex']
    if isinstance(blin1_inds, int):
        blin1_processtype=1
    elif isinstance(blin1_inds, numpy.ndarray):
        blin1_processtype=2
    else:
        blin1_processtype=0
    h5file.close()
    
    h5chess=CHESSRUNFILE()
    pnt=h5chess[blin0_1dpath]
    b0=readh5pyarray(pnt)
    pnt=h5chess[blin1_1dpath]
    b1=readh5pyarray(pnt)
    h5chess.close()
    
    if blin0_processtype==1:
        b0=b0[blin0_inds]

    if blin1_processtype==1:
        b1=b1[blin1_inds]
    
    if blin0_processtype==2:
        b0arr=numpy.array([b0[i] for i in blin0_inds])
    else:
        b0cpy=copy.copy(b0)
    
    if blin1_processtype==2:
        b1arr=numpy.array([b1[i] for i in blin1_inds])
    else:
        b1cpy=copy.copy(b1)

    f0list=[]
    f1list=[]
    fraczlist=[]
    for pointind in pointlist:
        print pointind
        
        if blin0_processtype==2:
            b0=b0arr[pointind]
        
        if blin1_processtype==2:
            b1=b1arr[pointind]

        f0=weights0[pointind]
        f1=weights1[pointind]

        if isinstance(fprecision, list):
            for fp in fprecision[:-1]:
                blinclass=calc_blin_factors(icounts[pointind], b0, b1, f0=f0, f1=f1, fraczeroed=fraczeroed, factorprecision=fp, refineduringloop=refineduringloop, maxtries=maxtries)
                if blinclass.warning!='':
                    print 'pointind %d, with fp=%s : %s' %(pointind, `fp`, blinclass.warning)
                f0=blinclass.f0
                f1=blinclass.f1
                print 'after fp=%.4f, f0=%.4f,  f1=%.4f' %(fp, f0, f1)
            fp=fprecision[-1]
        else:
            fp=fprecision
        blinclass=calc_blin_factors(icounts[pointind], b0, b1, f0=f0, f1=f1, fraczeroed=fraczeroed, factorprecision=fp, refineduringloop=refineduringloop, maxtries=maxtries)
        if blinclass.warning!='':
            print 'pointind %d, with fp=%s : %s', (pointind, `fp`, blinclass.warning)
        print 'after fp=%.4f, f0=%.4f,  f1=%.4f' %(fp, blinclass.f0, blinclass.f1)
        f0list+=[blinclass.f0]
        f1list+=[blinclass.f1]
        fraczlist+=[blinclass.fracz]
        if plotbool:
            pylab.figure()
            pylab.plot(icounts[pointind],'k', label='orig')
            x0=blinclass.f0*b0
            x1=blinclass.f1*b1
            pylab.plot(x0,'b', label='w0*blin0')
            pylab.plot(x1,'g', label='w1*blin1')
            pylab.plot(icounts[pointind]-x0-x1,'r', label='ans')
            break
    f0=numpy.array(f0list)
    f1=numpy.array(f1list)
    fracz=numpy.array(fraczlist)
    
    if blin0_processtype==2:
        bcknddata=-1.*numpy.array([f0v*b0arr[pointind] for pointind, f0v in zip(pointlist, f0)])
    else:
        bcknddata=-1.*numpy.array([f0v*b0cpy for f0v in f0])
    if blin1_processtype==2:
        bcknddata+=-1.*numpy.array([f1v*b1arr[pointind] for pointind, f1v in zip(pointlist, f1)])
    else:
        bcknddata+=-1.*numpy.array([f1v*b1cpy for f1v in f1])
    
    #bcknddata=-1.*numpy.dot(numpy.array([f0, f1]).T, numpy.array([b0cpy, b1cpy]))

    if savebool:
        h5file=h5py.File(h5path, mode='r+')
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
        

        newicounts=numpy.zeros(icounts.shape, dtype=icounts.dtype)
        newicounts[pointlist]=numpy.array([ic+bc for ic, bc in zip(icounts[pointlist], bcknddata)], dtype=icounts.dtype)
        #newicounts[newicounts<0.]=0.
        if savename in h5mar:
            del h5mar[savename]
        ds=h5mar.create_dataset(savename, data=newicounts)

        w=numpy.zeros((icounts.shape[0], 2), dtype=f0.dtype)
        w[pointlist, :]=numpy.array([f0, f1]).T
        saveattrs={'weights':w, 'blin0_h5chesspath':blin0_1dpath, 'blin1_h5chess':blin1_1dpath, 'f0startvals':weights0, 'f1startvals':weights1, 'fraczeroed':fraczeroed, 'fprecision':fprecision, 'refineduringloop':numpy.uint8(refineduringloop)}

        for k, v in saveattrs.iteritems():
            ds.attrs[k]=v
        
        updatelog(h5analysis,  ''.join(('1D lin bcknd substraction, all icounts. Saved as ', savename,'. Finished ',  time.ctime())))
        
        h5file.close()
    if plotbool:
        pylab.legend(loc=1)
        pylab.show()
