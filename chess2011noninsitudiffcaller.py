from diffcountsfcn3 import *
from diffcountsfcn2 import chess2011integrate
#p='F:/CHESS2011_h5MAIN/2011Oct02D_Bi.h5'
p='E:/2011Oct02D_Bi85.h5'
h5groupstr='85'
sourcespec='85'



#calcdiffcounts_lin(p, h5groupstr, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)
#chess2011integrate(p, h5groupstr)
calcdiffcounts_lin1d(p, h5groupstr, savename='mcounts', savebool=0, plotbool=1)
print 'done'
