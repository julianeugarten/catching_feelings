# Catching Feelings
This repo contains code and supplementary data for the _Catching Feelings_ Project.

Specifically, it contains:

  - the Python code used to scrape the dataset.
  - the noun chunks in the comment data as identified with SpaCy, sorted by frequency in a csv-file.
  - an anonymized version of the annotation guidelines used to create the annotation-set in a pdf.
  - the Jupyter notebook used for pre-processing and exploring the comment data.
  - the Jupyter notebook used to analyze the annotations and calculate inter-annotator agreement.
  - Two confusion matrices visualizing the confusion for aspects and sentiments between the two annotators.
  - A zipped annotations file from Inception, which you would need to run the inter_annotator_agreement notebook, is available [on Google Drive](https://drive.google.com/file/d/1KBzhly5fSLNOvyPsUbeC4DX2Z1D27Vse/view?usp=sharing). 
  - The annotations of aspects and evaluations in two csv files.
  - Results from the three models for aspect extraction: RoBERTa-base, Twitter-RoBERTa and NuNER
