from chess2011initroutine import chessbatch2011init
from diffcountsfcn2 import calcdiffcounts
h5path='C:/Users/Kechao/Desktop/test2011Oct02D_Bi.h5'
#chessbatch2011init(h5path,critratiotoneighbors=10.,  removepctilebeforeratio=.05, test=False)

#
#h5groupstr='74'
#sourcespec='74'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(162, 262, 5)
#
#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=True)

h5path='F:/CHESS2011_h5MAIN/2011Oct02D_Bi.h5'

#h5groupstr='84'
#sourcespec='84'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(38, 56)

#h5groupstr='74'
#sourcespec='74'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(180, 262, 4)
#
#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=False)
#
#h5groupstr='80'
#sourcespec='80'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(38, 56)
#
#
#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=False)


#h5groupstr='32'
#sourcespec='32'
#diffdict={}
#diffdict['sourcepath']=h5path
#diffdict['sourcespec']=sourcespec
#diffdict['sourceinds']=range(21, 30)

#calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=False)

h5groupstr='37'
sourcespec='37'
diffdict={}
diffdict['sourcepath']=h5path
diffdict['sourcespec']=sourcespec
diffdict['sourceinds']=range(55, 59)


calcdiffcounts(h5path, h5groupstr, diffdict, savename='dcounts', savebool=True, plotbool=False, intbool=True, intplotbool=False, icountsbool=False)

print 'done'
