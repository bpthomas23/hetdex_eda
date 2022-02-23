import numpy as np
from astropy.io import fits
#import pandas as pd

aux = np.load('auxillary_data.npy')
aux_detect_id = aux[:,0].astype('int')
aux_ra = aux[:,1]
aux_dec = aux[:,2]
aux_gmag = aux[:,3]

#aux_detect_id_pd = pd.DataFrame({'detectid': aux_detect_id})

hdu = fits.open('source_catalog_2.1.2.fits')
head = hdu[1].header
sc = hdu[1].data

sc_detect_id = sc.detectid
sc_source_id = sc.gaia_match_id
sc_z_guess = sc.z_guess

#sc_detect_id_pd = pd.DataFrame({'detectid': sc_detect_id,
#                                    'sourceid': sc_source_id})

#aux_source_id = aux_detect_id_pd.detectid.map(sc_detect_id_pd.set_index('detectid').sourceid)
#aux_z_guess
#crossmatch auxdata & sc on detectid
#retain z_guess

addcols = np.zeros((len(aux_detect_id),2))
addcols[:] = -99.
for idx,did in enumerate(aux_detect_id):
    ind = np.where(sc_detect_id == did)[0]
    
    try:
        addcols[idx] = np.array((sc_source_id[ind[0]], sc_z_guess[ind[0]]))

    except: continue


hdu = fits.open('HDR2.1_Gaia_final_table.fits')
head = hdu[1].header
ga = hdu[1].data

ga_source_id = ga.source_id
ga_colour = ga.bp_rp

#crossmatch result & ga on source_id
#retain bp-rp
addgcols = np.zeros((len(aux_detect_id)))
addgcols[:] = -99.
for idx,sid in enumerate(addcols[:,0].astype('int')):
    ind = np.where(ga_source_id == sid)[0]

    try:
        addgcols[idx] = ga_colour[ind[0]]
    except: continue

arr = np.column_stack((aux_detect_id,addcols[:,0],aux_ra,aux_dec,aux_gmag,addgcols,addcols[:,1]))
np.save('auxillary_data_zc.npy',arr)

