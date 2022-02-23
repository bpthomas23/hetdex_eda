import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.pipeline import make_pipeline
path = '/Users/benjamin/Documents/postdoc/hetdex/'

data =  np.load(path+'hdr2.1.2/preprocess/pp_continuua_hdr2.1.2.npy')
filenames,spectra = data[:,0],data[:,1:].astype('float')

#spectra = np.loadtxt('pp_spectra.txt')

#scaler = StandardScaler()
#scaler = Normalizer()
#pca = PCA()
pca = PCA(n_components=.8,svd_solver='full')
#pipeline = make_pipeline(scaler,pca)

#pipeline.fit_transform(spectra.T)
pca.fit(spectra.T)

np.save('principal_continuua_hdr2.1.2.npy',np.column_stack((filenames,pca.components_.T)))

#uncomment to select number of components
"""
varc = pca.explained_variance_ratio_

cumulative = np.array([np.sum(varc[:n])/np.sum(varc) for n in range(varc.shape[0])])

import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(1,pca.n_components_+1),cumulative)
#plt.yscale('log')
plt.ylabel('Cumulative variance contribution')
plt.xlabel('PCA feature')
plt.axhline(0.7,ls='--',lw=1,color='k',alpha=.7)
plt.axhline(0.8,ls='--',lw=1,color='k',alpha=.7)
plt.axhline(0.9,ls='--',lw=1,color='k',alpha=.7)
#plt.text(40,0.79,r'80%',verticalalignment='top')
#plt.text(40,0.89,r'90%',verticalalignment='top')
plt.xlim(-30,320)
plt.ylim(0.5,1.01)
plt.savefig('cumulative_variance.pdf')
plt.show()
"""
