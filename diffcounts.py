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


h5path='E:/temp2011Oct02D_Bi.h5'
p='E:/temp2011Oct02D_Bi.h5'

segind=4
cell=20

f=h5py.File(p, mode='r')

h5groupstr='84'
sourcespec='84'
diffdict={}
diffdict['sourcepath']=p
diffdict['sourcespec']=sourcespec
diffdict['sourceinds']=range(38, 56)
savename='dcounts'
savebool=True
plotbool=False
intbool=True
intplotbool=False
icountsbool=True

isavename='i'+savename
f=h5py.File(diffdict['sourcepath'], mode='r')
pnt=f[diffdict['sourcespec']]['measurement/area_detector/counts']
b=numpy.zeros((len(diffdict['sourceinds']),)+pnt.shape[1:], dtype='float32')
for c, i in enumerate(diffdict['sourceinds']):
    b[c, :, :]=numpy.float32(pnt[i, :, :])
f.close()
b=b.mean(axis=0)


if savebool:
    h5file=h5py.File(h5path, mode='r+')
else:
    h5file=h5py.File(h5path, mode='r')
h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
h5marcounts=h5file['/'.join((h5groupstr,'measurement', getxrdname(h5analysis), 'counts'))]
pointlist=h5analysis.attrs['pointlist']

diffcounts=numpy.float32(h5marcounts[:, :, :])
for pointind in pointlist:
    print pointind
    diffcounts[pointind]-=b
    if plotbool:
        pylab.figure()
        pylab.imshow(diffcounts[pointind], interpolation='nearest')
        pylab.colorbar()
if savebool:
    if savename in h5mar:
        del h5mar[savename]
    h5mar.create_dataset(savename, data=diffcounts)
    if 'diffimage' in h5mar:
        del h5mar['diffimage']
    ds=h5mar.create_dataset('diffimage', data=b)
    for k, v in diffdict.iteritems():
        ds.attrs[k]=v
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
    if isavename in h5mar:
        del h5mar[isavename]
    idcounts=h5mar.create_dataset(isavename, data=numpy.zeros((diffcounts.shape[0], qgrid[2]), dtype='float32'))
    idcounts.attrs['qgrid']=qgrid
    for pointind in pointlist:
        print 'idcounts', pointind
        data=diffcounts[pointind, :, :]
        idcounts[pointind, :]=intbyarray(data, imap, dqchiimage, slots)[:]
    if icountsbool:
        isavename2='icounts'
        if isavename2 in h5mar:
            del h5mar[isavename2]
        icounts=h5mar.create_dataset(isavename2, data=numpy.zeros((h5marcounts.shape[0], qgrid[2]), dtype='float32'))
        icounts.attrs['qgrid']=qgrid
        for pointind in pointlist:
            print 'icounts', pointind
            data=h5marcounts[pointind, :, :]
            icounts[pointind, :]=intbyarray(data, imap, dqchiimage, slots)[:]
    h5file.close()
    
    if intplotbool:
        h5file=h5py.File(h5path, mode='r')
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        h5mar=h5file['/'.join((h5groupstr, 'analysis', getxrdname(h5analysis)))]
        pointlist=h5analysis.attrs['pointlist']
        arr=h5mar[isavename][:, :]
        h5file.close()
        pylab.figure()
        for pointind in pointlist:
            pylab.plot(arr[pointind])

if plotbool or (intbool and intplotbool):
    pylab.show()
