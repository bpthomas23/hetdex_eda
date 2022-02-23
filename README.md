# hetdex_eda

This project investigated the HETDEX continuum catalogue; a dataset of ~70K astronomical spectra that all show significant continuum emission.
The criterion that selects this data-set means that objects must be bright, else they would not show continuum emission. This data-set contains all such
bright astronomical objects, from stars to galaxies, from white dwarfs to accretion disks around black holes. I found that the majority of the data-set is
about 50% galactic objects and 50% stellar objects, with some minority classes of interesting anomalies. 

The workflow for this project proceeds as follows: first, some routine preprocessing of the data. This included aggregating tens of thousands of ASCII files
into a single binary numpy file, and then performing basic sklearn preprocessing steps (data cleaning) such as imputation of missing values and normalization.
Once the spectra were preprocessed, I then performed a PCA (principle component analysis) to vastly reduce the dimensionality of the data. The PCA was performed
iteratively, first running it with the same number of dimensions in the output as the input, and inspecting the cumulative variance per dimension to find a point
where the information gain per dimension significantly decreased, thus implying an obvious point to cut the dimensionality. Secondly it was re-run with this 
dimensionality and these principal continuua (38 dimensions, down from 1036) were saved for further analysis. 

The next step was to perform a t-distributed stochastic neighbor embedding (t-SNE) analysis (see more info on t-SNE here: https://lvdmaaten.github.io/tsne/). 
t-SNE again reduces the dimensionality of the data, but meanwhile preserves information on the similarity of the samples within the reduced dimensions. The data
is reduced to just 2 dimensions--each spectrum is now represented as a single point on a 2D plot. Spectra bearing similarity to one another are close to each other
on the t-SNE plot, while spectra that are dissimilar are further apart. This produces a natural clustering of the data which is extremely useful to visualise
unlabelled structure in the data. I found that t-SNE produced many distinct clusters of spectra, naturally separating the stars from the galaxies. In the large
star cluster, the stars were ordered by their spectral type (luminsoity and temperature), effectively making a transformed Hertzsprung-Russel diagram. The galaxies,
on the other hand, were sorted by their redshift (radial distance from the Milky Way) and emission line properties (degree of star formation). In addition to these
striking results, there were a number of other, smaller clusters containing more unusual objects, such as high redshift quasars (very distant accreting black holes),
white dwarf stars (nearby stellar corpses supported by quantum pressure), and other unusual objects. Another distinct cluster contained primarily bad data, which
helped to re-calibrate and improve the survey reduction pipeline.

Finally, I set up a tool to interatively visualise this result using the Python library holoviews. This tool showed the t-SNE clusters in the bottom sub-panel,
and the full astronomical spectrum from HETDEX in the top sub-panel. Users could click on a point in the t-SNE clusters, and the spectrum corresponding to that
point would display in the top panel. This helped enormously in investigating the nature of the t-SNE clusters. By thoroughly investigating the clusters I was able
to classify the vast majority of the data-set into either stars, galaxies, quasars, meteors, asteroids and bad data.
