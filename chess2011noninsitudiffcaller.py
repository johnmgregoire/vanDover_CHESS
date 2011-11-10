from chess2011initroutine import chessbatch2011init
from diffcountsfcn3 import calcdiffcounts_lin
p='F:/CHESS2011_h5MAIN/2011Oct02D_Bi.h5'

h5groupstr='85'
sourcespec='85'



calcdiffcounts_lin(p, h5groupstr, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)

print 'done'
