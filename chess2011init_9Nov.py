import h5py,numpy, os, operator, pylab, time

from chess2011initroutine import chessbatch2011init
from diffcountsfcn2 import *
from xrd_fileIO_fcns import *
from xrd_math_fcns import *

p='F:/CHESS2011_h5MAIN'
px='F:/CHESS2011XRD_asimported'

fnxrd_fnpnsc=[
#('2011Jun01B.dat.h5','2011Jun01b_AuSiCu.h5',['AuSiCuheat1','AuSiCuheat2','AuSiCuheat3','AuSiCuheat4']),\
#('2011Jun01B.dat.h5','2011Jun01b_NiTiHf.h5',['NiTiHfheat1','NiTiHfheat1_MA','NiTiHfheat1_fast','NiTiHfheat1_slow','NiTiHfheat2','NiTiHfheat2_MA']),\
#('2011Jun01A_ZrCuAl_heat0.dat.h5', '2011Jun01a.h5', ['ZrCuAlheat1', 'ZrCuAlheat2', 'ZrCuAlheat3', 'ZrCuAlheat4', 'ZrCuAlheat5']), \
##('2011Oct02D_AuSiCu.dat.h5', '2011Oct02D_AuSiCu.h5', ['AuSiCuheats']), \
##('2011Oct02D_InSnBi.dat.h5', '2011Oct02D_Bi.h5', ['Bi_ACheats']), \
#('2011Oct10B.dat.h5', '2011Oct10B_NiTiHf.h5', ['NiTiHfheat1', 'NiTiHfheat2', 'NiTiHfheat3', 'NiTiHfheat1_MA', 'NiTiHfheat2_MA', 'NiTiHfheat3_MA']), \
('2011Oct10B_FeNi.dat.h5', '2011Oct10B_FeNi.h5', ['DCheats', 'ACheats']), \
#('2011Oct10C.dat.h5', '2011Oct10C.h5', ['borides']), \
##('2011Oct10D_NiTiHf.dat.h5', '2011Oct10D.h5', ['DCheats', 'ACheats']), \
]

#for fnx, fn, expgrplist in fnxrd_fnpnsc:
#    print '***', fn
#    if not fn.endswith('.h5'):
#        continue
#    chessbatch2011init(os.path.join(p, fn),critratiotoneighbors=10.,  removepctilebeforeratio=.05, test=False)
#
#print '^^^^^^^^^^^^^^^^^^^^^^^^done with init'
#
#h5path='F:/CHESS2011_h5MAIN/2011Oct02D_Bi.h5'
#
#h5groupstr='74'
#sourcespec='74'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(162, 262, 5)
#
#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)
#
#h5path='F:/CHESS2011_h5MAIN/2011Oct02D_Bi.h5'
#
#h5groupstr='84'
#sourcespec='84'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(38, 56)
#
#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)
#
#
#print '^^^^^^^^^^^^^^^^^^^done with couple of insitu processes'

#for fnx, fn, expgrplist in fnxrd_fnpnsc:
#    print '***', fn
#    if not fn.endswith('.h5'):
#        continue
#    p2=os.path.join(p, fn)
#    f=h5py.File(p2, mode='r')
#    insitu=False
#    splist=[]
#    for g in f.values():
#        try:
#            if g['analysis'].attrs['insitu']==insitu:
#                splist+=[g.name.rpartition('/')[2]]
#        except:
#            continue
#    f.close()
#    for sp in splist:
#        print sp
#        calcbcknd(p2, sp, bcknd='lin', bin=2, critfrac=0.020, weightprecision=0.002, normrank=0.800)
        
print '^^^^^^^^^^^^^^^^^^^done with 2d bcknd for noninsitu'

for fnx, fn, expgrplist in fnxrd_fnpnsc:
    print '***', fn
    if not fn.endswith('.h5'):
        continue
    p2=os.path.join(p, fn)
    f=h5py.File(p2, mode='r')
    insitu=False
    splist=[]
    for g in f.values():
        try:
            if g['analysis'].attrs['insitu']==insitu:
                splist+=[g.name.rpartition('/')[2]]
        except:
            continue
    f.close()
    for sp in splist:
        print sp
        chess2011integrate(p2, sp, bckndbool=True)
        linbckndsub1d(p2, sp, fprecision=[.5, .05,.005,.0007, .0001], maxtries=1000)
        process1dint(p2, sp, maxcurv=4)
print '^^^^^^^^^^^^^^^^^^^done with integrate and process for noninsitu'
