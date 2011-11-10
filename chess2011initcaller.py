from chess2011initroutine import chessbatch2011init

#h5path='E:/test2011Oct10B_FeNi.h5'
h5path='E:/BackgroundImages.dat.h5'
f=chessbatch2011init(h5path,critratiotoneighbors=10.,  removepctilebeforeratio=.05, test=False)

print 'done'
