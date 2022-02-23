from shapely.geometry import MultiPoint
from shapely.geometry.polygon import Polygon
import numpy as np

arr = np.load('tsne_components_hdr2.1.2.npy')
dids = arr[:,0].astype('int')
coords = arr[:,1:]

coords = [tuple(c) for c in coords]
points = MultiPoint(coords)

stars = np.loadtxt('poly/stars.txt')
gals0 = np.loadtxt('poly/gals0.txt')
gals1 = np.loadtxt('poly/gals1.txt')
qso0 = np.loadtxt('poly/qso0.txt')
qso1 = np.loadtxt('poly/qso1.txt')
qso2 = np.loadtxt('poly/qso2.txt')
qso3 = np.loadtxt('poly/qso3.txt')
qso4 = np.loadtxt('poly/qso4.txt')
qso5 = np.loadtxt('poly/qso5.txt')
qso6 = np.loadtxt('poly/qso6.txt')
bad = np.loadtxt('poly/bad.txt')

stars = Polygon(stars)
gals0 = Polygon(gals0)
gals1 = Polygon(gals1)
qso0 = Polygon(qso0)
qso1 = Polygon(qso1)
qso2 = Polygon(qso2)
qso3 = Polygon(qso3)
qso4 = Polygon(qso4)
qso5 = Polygon(qso5)
qso6 = Polygon(qso6)
bad = Polygon(bad)

starmask = np.zeros((len(points))).astype('bool')
galmask = np.zeros((len(points))).astype('bool')
qsomask = np.zeros((len(points))).astype('bool')
badmask = np.zeros((len(points))).astype('bool')
for idx, point in enumerate(points):
    if (point.within(qso0) | point.within(qso1) | point.within(qso2) | 
        point.within(qso3) | point.within(qso4) | point.within(qso5) |
        point.within(qso6)):
        
        qsomask[idx] = True
        continue

    if point.within(bad):
        badmask[idx] = True
        continue

    if (point.within(gals0) | point.within(gals1)):
        galmask[idx] = True
        continue

    if point.within(stars):
        starmask[idx] = True
        continue

maskarr = np.row_stack((starmask,galmask,qsomask,badmask))
anommask = ~np.any(maskarr,axis=0)

star_dids = dids[starmask]
gal_dids = dids[galmask]
qso_dids = dids[qsomask]
bad_dids = dids[badmask]
anom_dids = dids[anommask]

np.savetxt('classifications/stars.txt',star_dids, fmt='%.10i')
np.savetxt('classifications/galaxies.txt',gal_dids, fmt='%.10i')
np.savetxt('classifications/quasars.txt',qso_dids, fmt='%.10i')
np.savetxt('classifications/bad.txt',bad_dids, fmt='%.10i')
np.savetxt('classifications/anomalies.txt',anom_dids, fmt='%.10i')





