# Catching Feelings
This repo contains code and supplementary data for the _Catching Feelings_ Project. The paper associated with that project is now [available here](https://ceur-ws.org/Vol-3834/paper23.pdf). If you use this repo, please cite:

Neugarten, Julia, et al. “Catching Feelings: Aspect-Based Sentiment Analysis for Fanfiction Comments about Greek Myth.” 	
	2024, *CHR2024: Computational Humanities Research*, pp. 217–31, https://ceur-ws.org/Vol-3834/paper23.pdf.


Specifically, it contains:

  - the Python code used to scrape the dataset.
  - the noun chunks in the comment data as identified with SpaCy, sorted by frequency in a csv-file.
  - an anonymized version of the annotation guidelines used to create the annotation-set in a pdf.
  - the Jupyter notebook used for pre-processing and exploring the comment data.
  - the Jupyter notebook used to analyze the annotations and calculate inter-annotator agreement. A zipped annotations file from Inception, which you need to replicate this notebook, is available [on Google Drive](https://drive.google.com/file/d/1KBzhly5fSLNOvyPsUbeC4DX2Z1D27Vse/view?usp=sharing).
  - The Jupyter notebook used to evaluate the differences and overlaps between NuNER, the best model for aspect extraction, and our gold standard annotations. This notebook includes the code to create the confusion matrix from the paper.
  - Two confusion matrices visualizing the confusion for aspects and sentiments between the two annotators.
  - The annotations of aspects and evaluations in two csv files.
  - Results from the three models for aspect extraction: RoBERTa-base, Twitter-RoBERTa and NuNER.
