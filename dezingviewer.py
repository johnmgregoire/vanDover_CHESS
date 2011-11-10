import h5py, numpy, pylab, copy

p='E:/test2011Oct10B_FeNi.h5'
ind=0
sp='10'
f=h5py.File(p, mode='r')

pnt=f[sp]['measurement/area_detector/counts']
x=pnt[ind,:,:]
y=numpy.zeros(x.shape,x.dtype)

inds=tuple(pnt.attrs['replacedinds%03d' %ind])
vals=pnt.attrs['replacedvals%03d' %ind]
y[inds]=vals


z=copy.copy(x)

z[inds]=vals
f.close()

vmin=x.min()
vmax=y.max()

pylab.subplot(3,1,1)
pylab.imshow(x, interpolation='nearest', vmin=vmin, vmax=vmax)
pylab.colorbar()
pylab.subplot(3,1,2)
pylab.imshow(y, interpolation='nearest', vmin=vmin, vmax=vmax)
pylab.colorbar()
pylab.subplot(3,1,3)
pylab.imshow(z, interpolation='nearest', vmin=vmin, vmax=vmax)
pylab.colorbar()

pylab.show()
