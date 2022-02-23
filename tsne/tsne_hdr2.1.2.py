from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
import mpld3

data = np.load('../pca/principal_continuua_hdr2.1.2.npy')
filenames,pca_components = data[:,0],data[:,1:].astype('float')

tsne = TSNE(n_components=2,random_state=27,perplexity=150)

transformed = tsne.fit_transform(pca_components)
np.save('tsne_components_hdr2.1.2_p150.npy',np.column_stack((filenames,transformed)))
fig,ax = plt.subplots()
scatter = ax.scatter(transformed[:,0],transformed[:,1],s=3,color='k')

plt.show()
