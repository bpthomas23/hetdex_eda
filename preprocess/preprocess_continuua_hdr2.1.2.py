import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,Normalizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

data = np.load('../hdr2.1.2_contspec.npy')
#data = np.load('../cns/filtered_sources.npy')
filenames,spectra = data[:,0],data[:,1:].astype('float')

wavelength = np.arange(3470,5542,2) #read from first file column 1

inds = np.random.randint(spectra.shape[0],size=35)
random_spectra = spectra[inds]

plt.figure(figsize=(6,7))
k = 0
for spectrum in random_spectra:
        plt.plot(wavelength,spectrum+k*.05,lw=1)
        k += 1
#plt.tight_layout()
plt.xlabel(r'Observed wavelength (${\rm \AA}$)')
plt.ylabel('Measured flux')

#preprocess by replacing nan values and normalising
imputer = SimpleImputer(missing_values=np.nan,strategy='median')
#scaler = StandardScaler()
scaler = Normalizer()
pipeline = make_pipeline(imputer,scaler)
tspectra = pipeline.fit_transform(spectra)
#tspectra = scaler.transform(spectra[inds])

#save preprocessed
np.save('pp_continuua_hdr2.1.2.npy',np.column_stack((filenames,tspectra)))

#plot a random subset
#inds = np.random.randint(spectra.shape[0],size=100)
random_spectra = tspectra[inds]

plt.figure(figsize=(6,7))
k = 0
for spectrum in random_spectra:
	plt.plot(wavelength,spectrum+k*.05,lw=1)
	k += 1
#plt.tight_layout()
plt.xlabel(r'Observed wavelength (${\rm \AA}$)')
plt.ylabel('Normalised flux + constant')

plt.show()
