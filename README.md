![Logo Tempviz](/img/tempviz_logo.png)


<h1 align="center">
<span>TempViz: On the Evaluation of Temporal Knowledge in Text-to-Image Models</span>
</h1>

[![ACL Anthology](https://img.shields.io/badge/ACL-Anthology-blue)](https://xxx)

## Paper Abstract

Time alters the visual appearance of entities in our world, like objects, places, and animals. Thus, for accurately generating contextually-relevant images, knowledge and reasoning about time can be crucial (e.g., for generating a landscape in spring vs. in winter). Yet, although substantial work exists on understanding and improving temporal knowledge in natural language processing, research on how temporal phenomena appear and are handled in text-to-image (T2I) models remains scarce. We address this gap with TempViz, the first data set to holistically evaluate temporal knowledge in image generation, consisting of 7.9k prompts and more than 600 reference images. Using TempViz, we study the capabilities of five T2I models across five temporal knowledge categories. Human evaluation shows that temporal competence is generally weak, with no model exceeding 75% accuracy across categories. Towards larger-scale studies, we also examine automated evaluation methods, comparing several established approaches against human judgments. However, none of these approaches provides a reliable assessment of temporal cues - further indicating the pressing need for future research on temporal knowledge in T2I.

------------------------
## Getting Started

We conducted all our experiments with Python 3.10. Before getting started, make sure you install the requirements listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## 📂 Directory/File Structure Overview

This repository contains all the code and data needed to reproduce the experiments and results reported in our paper.

### Data 

A brief description of the files in *data* is:

- **experimental_results.xlsx**
    - Contains all results we produced throughout our experiments.

- **efficiency calculation.xlsx**
    - Contains the results of the efficiency calculations for DeBERTa and GPT-2.



### Code

Includes all python files and notebooks subject to this paper.

A brief description of the files in *code* is:

- **creation_of_paper_plots.ipynb**
    - This notebook can be used to recreate all plots present in the paper, based on the experimental results.


------------------------
## References

Please use the following bibtex entry if you use this model in your project (TBD):
 
```bib
@inproceedings{,
```


---
*Author contact information: carolin.holtermann@uni-hamburg.de*


## License

All source code is made available under a 
