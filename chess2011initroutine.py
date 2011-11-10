import os

from xrd_fileIO_fcns import *
#from xrd_math_fcns import *
from xrdUI import *
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

mainapp = QApplication(sys.argv)
mm = MainMenu()
    
def chess2011importattrDialogcaller(p1, p2, p3, command=None):
    idialog = importattrDialog(p1, p2, p3, command=command)
    ellineditlist=[idialog.el1LineEdit, idialog.el2LineEdit, idialog.el3LineEdit, idialog.el4LineEdit]
    ellist=[str(unicode(le.text())) for le in ellineditlist]
    xgrid=(idialog.xstartSpinBox.value(), idialog.xintSpinBox.value(), idialog.xptsSpinBox.value())
    zgrid=(idialog.zstartSpinBox.value(), idialog.zintSpinBox.value(), idialog.zptsSpinBox.value())
    returndict ={
    'wavelength':idialog.wavelengthSpinBox.value(),
    'command':str(unicode(idialog.cmdLineEdit.text())),
    'elements':ellist,
    'xgrid':xgrid,
    'zgrid':zgrid,
    'counter':idialog.inttimeSpinBox.value(),
    'cal':[idialog.xcenSpinBox.value(), idialog.ycenSpinBox.value(), idialog.LSpinBox.value(), idialog.martiltSpinBox.value(), idialog.tiltrotSpinBox.value()],
    'alpha':idialog.alphaSpinBox.value(),
    'bcknd':str(unicode(idialog.bckndComboBox.currentText())),
    'chessrunstr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())))),
    'imapstr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'imap', str(unicode(idialog.imapcomboBox.currentText())))),
    'chimapstr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'chimap', str(unicode(idialog.chimapcomboBox.currentText())))),
    'killmapstr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'killmap', str(unicode(idialog.killmapcomboBox.currentText())))),
    'qimagestr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'qimage')),
    'chiimagestr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'chiimage')),
    'dqchiimagestr':'/'.join(('', str(unicode(idialog.chessruncomboBox.currentText())), 'dqchiimage')),
    'xrdname':str(idialog.xrdnameLineEdit.text()), 
    'psize':idialog.psizeSpinBox.value(), 
    }
    if returndict['command']!='USER-COMPILED':
        if idialog.usespecCheckBox.isChecked():
            for k, v in idialog.fromspecattr.iteritems():
                returndict[k]=v
        else:
            for k, v in specattr_xzgrid(xgrid, zgrid, 'mesh' in returndict['command']).iteritems():
                returndict[k]=v
    return returndict

def chessbatch2011init(h5path,critratiotoneighbors=3.,  removepctilebeforeratio=.05, insituscalarname='IC3', test=False):
    command=None
    idialog2=importh5scanDialog(mm, h5path)
    for optstr in idialog2.optionlist:
        print optstr
        h5groupstr, temp, command=optstr.partition(':')
        h5groupstr=str(h5groupstr)
        
        h5file=h5py.File(h5path, mode='r+')
        if not 'analysis' in h5file[h5groupstr]:
            h5file[h5groupstr].create_group('analysis')
        h5file.close()

        attrdicttemp = chess2011importattrDialogcaller(mm, h5path, h5groupstr, command=command)
        if attrdicttemp is None:
            print 'problem with batch initialize for ', h5groupstr
            continue
        
        writeattr(h5path, h5groupstr, attrdicttemp)
        h5file=h5py.File(h5path, mode='r+')
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        xrdname=getxrdname(h5analysis)
        if not xrdname in h5analysis:
            h5analysis.create_group(xrdname)
        h5analysis=h5file['/'.join((h5groupstr, 'analysis'))]
        try:
            h5marcounts=h5file['/'.join((h5groupstr,'measurement', getxrdname(h5analysis),'counts'))]
        except:
            print 'no counts found for ', h5groupstr
            h5file.close()
            continue
        attrdict=getattr(h5path, h5groupstr)
        pointlist=range(h5marcounts.shape[0])
        h5analysis.attrs['pointlist']=pointlist
        h5file.attrs['defaultscan']=str(h5groupstr)
        
#        for pointind in pointlist:
#            arr=h5marcounts[pointind, :, :]
#            print '*', arr.shape
#            h5marcounts[pointind, :, :], inds=removesinglepixoutliers(arr,critratiotoneighbors=critratiotoneighbors, removepctilebeforeratio=removepctilebeforeratio, returninds=True)
#            if len(inds[0])>0:
#                h5marcounts.attrs['replacedinds%03d' %pointind]=inds
#                h5marcounts.attrs['replacedvals%03d' %pointind]=arr[inds]
        for pointind in pointlist:
            arr=h5marcounts[pointind, :, :]
            temp, inds=removesinglepixoutliers(copy.copy(arr),critratiotoneighbors=critratiotoneighbors, removepctilebeforeratio=removepctilebeforeratio, returninds=True)
            if len(inds[0])>0:
                h5marcounts.attrs['replacedinds%03d' %pointind]=inds
                h5marcounts.attrs['replacedvals%03d' %pointind]=arr[inds]
            h5marcounts[pointind, :, :]=temp[:, :]
        h5marcounts.attrs['critratiotoneighbors']=critratiotoneighbors
        h5marcounts.attrs['removepctilebeforeratio']=removepctilebeforeratio
        if 'tseries 1' in attrdict['command'] and h5marcounts.shape[0]>1:# insitu experiment #TODO: what to do with acquisition_shape?
            nimages=h5marcounts.shape[0]
            g=h5file['/'.join((h5groupstr, 'measurement', 'scalar_data'))]
            temp=[insituscalarname]
            if insituscalarname!='Seconds':
                temp+=['Seconds']
            for nam in temp:
                totic=g[nam]
                ic=numpy.ones(nimages, dtype='float32')*totic/nimages
                g.copy(nam, 'asimported_'+nam)
                del g[nam]
                g.create_dataset(nam, data=ic)
            h5analysis.attrs['insitu']=True
            h5analysis.parent.attrs['insitu']=True
            print 'insitu'
        else:
            h5analysis.attrs['insitu']=False
            h5analysis.parent.attrs['insitu']=False
        h5file.close()
        if test:
            break
