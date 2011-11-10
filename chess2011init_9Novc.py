import h5py,numpy, os, operator, pylab, time

from diffcountsfcn3 import calcdiffcounts_lin
from xrd_fileIO_fcns import *
from xrd_math_fcns import *

p='F:/CHESS2011_h5MAIN'
px='F:/CHESS2011XRD_asimported'

fnxrd_fnpnsc=[
#('2011Jun01B.dat.h5','2011Jun01b_AuSiCu.h5',['AuSiCuheat1','AuSiCuheat2','AuSiCuheat3','AuSiCuheat4']),\
#('2011Jun01B.dat.h5','2011Jun01b_NiTiHf.h5',['NiTiHfheat1','NiTiHfheat1_MA','NiTiHfheat1_fast','NiTiHfheat1_slow','NiTiHfheat2','NiTiHfheat2_MA']),\
#('2011Jun01A_ZrCuAl_heat0.dat.h5', '2011Jun01a.h5', ['ZrCuAlheat1', 'ZrCuAlheat2', 'ZrCuAlheat3', 'ZrCuAlheat4', 'ZrCuAlheat5']), \
##('2011Oct02D_AuSiCu.dat.h5', '2011Oct02D_AuSiCu.h5', ['AuSiCuheats']), \
('2011Oct02D_InSnBi.dat.h5', '2011Oct02D_Bi.h5', ['Bi_ACheats']), \
#('2011Oct10B.dat.h5', '2011Oct10B_NiTiHf.h5', ['NiTiHfheat1', 'NiTiHfheat2', 'NiTiHfheat3', 'NiTiHfheat1_MA', 'NiTiHfheat2_MA', 'NiTiHfheat3_MA']), \
#('2011Oct10B_FeNi.dat.h5', '2011Oct10B_FeNi.h5', ['DCheats', 'ACheats']), \
#('2011Oct10C.dat.h5', '2011Oct10C.h5', ['borides']), \
##('2011Oct10D_NiTiHf.dat.h5', '2011Oct10D.h5', ['DCheats', 'ACheats']), \
]


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
        calcdiffcounts_lin(p2, sp, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)
        

print '^^^^^^^^^^^^^^^^^^^done with integrate for noninsitu'
