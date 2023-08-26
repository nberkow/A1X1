
#### NewCo Endomitriosis product


## Problem Summary

PLS is evaluating a company called NewCo in the endometriosis space. They are focusing on the gene A1X1. The investment team would like to know about pathogenesis, development and progression as well as important biological pathways, clinical history, etc.

## Overall Approach

### Background

My first step was to read about endometriosis in some high level sources (e.g. Wikipedia, review articles). My goal was to get familiar with the disease and the state of research into it. I found some key takeaways:

#### Endometriosis

Endometriosis is a disease of the female reproductive system where endometrial tissue that normally grows inside the uterus grows outside the uterus (or on a part of the uterus that doesn't normally contain those cells).
- The range of symptoms is wide. Some people experience a lot pain, other are asymptomatic
- It can cause infertility even when it doesn’t cause pain or other symptoms. Some patients are diagnosed for the first time during infertility treatment
- Endometriosis is at "the extreme end of diagnostic inefficiency" (wiki). People see 7 doctors on average before a correct diagnosis
- There were no good biomarkers as of 2016 - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6953323/
- There is no cure and treatment options are limited. Many patients are given NSAIDs

#### Molecular Causes

- There is strong evidence that it is heritable
    - Children or siblings of women with endometriosis are at higher risk of developing endometriosis themselves
    - There is an approximate six-fold increased incidence in individuals with an affected first-degree relative
- There are 9 GWAS loci of interest including 8 protein coding genes
- There are many proposed mechanism, but no general agreement
    - It could be a genetic difference in the affected cells
    - Or it could be in a hormone producing tissue elsewhere
    - Possible autoimmune component. It’s loosely linked to Graves disease
    - Rogue stem cells developing the wrong way in the wrong place

I drew a cartoon to summarize my thoughts on potentially relevant cell types. Because of the disease process, I might expect to find important genes in the endomitriosis cells themselves. There may also be factors in the healthy endometrium that pre-dispose it to form ectopically. The host tissue where the endometriosis grows may also have sucesptibility factors.

Because there is some suspicion that autoimmunity is involved, important factors may exist in one or more immune cells.

Healty endometrium and endometriosis are both hormone sensitive tissues, so hormone producing tissue may play a role. The picture doesn't include possible factors in stem cells. These both seem plausible, but neither are well studied.

![cartoon](./figures/cartoon.png)


Sources
- https://en.wikipedia.org/wiki/Endometriosis
- https://www.womenshealth.gov/a-z-topics/endometriosis
- https://emedicine.medscape.com/article/271899-overview
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5737931/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6953323/

### Genese of Interest

I wanted to create a list of candidate genes that might be involved for downstream analysis. In a real situation, this would include A1X1 and any other genes of interest to NewCo's approach. For this exercize, I started with a list of published GWAS hits for the disease. I used these to search a database of protein functional interactions (https://string-db.org/). This found some additional genes as well as a proposed interaction network.

![network](./figures/network.png)

Gene interactions are challenging to construct and are often full of spurious interactions. Even the starting set only has GWAS evidence, which isn't strong on its own. Keeping those caveats in mind, I planned to use these as a starting point to guide analysis. 

Database interaction code:
- get_gene_interactions.py


### Single Cell Gene Expression

Endometriosis is an ectopic growth of one cell type in the tissue of a different cell type. This suggested to me that samples of endometriosis tissue probably contain a mixture of cell types. There may also be more than one cell type in each of the tissue types. I also expect to potentially find mobile cell types from blood.

Single Cell RNA-Sequencing give an expression profile of a large number of cells from the sample. It might be possible to use expression to resolve cell types and find genes involved in the disease. 

I would expect A1X1 to be expressed in at least one of these tissue types. Expression isn't a perfect indicator of protein level and important genes can have a large effect without being expressed, but some level of expression would support its selection as a target. Differential expression of important genes is also not gauranteed depending on the mechanism, but it is often a clue so seeing A1X1 expressed differently between cell types would also support it as a target.

#### Single Sample Analysis

A single sample likely has a mixture of cell types from the same patient. It might be possible to resolve cell types and find expression patterns just using one endometriosis sample. Some questions that could be pursued in this way are:
- what cell types are present?
- does gene expression distinguish endometriosis tissue different from normal endometrium?


#### Cross Sample Analysis

Studies that collect endometriosis samples sometimes also collect healthy samples from the same patient. These could be used to help resolve cell types by comparing expression clusters. It might also be possible to label the different samples and combine them before looking for clusters.

Comparing samples from multiple patients could be done in a similar way, either by calling clusters in each sample and combining them or by labeling them and clustering them together. One possible effect it that patient-specific genetic effects would be obscured leaving more universal signals about the disease. It might also get at some questions about the disease process:
- Is endometriosis a single disease process or are their subtypes?
- Which expression patterns seem consistent across patients?
- Is A1X1 a general target or is it specific to a sub-population?

#### Cross Study Analysis

I could also do the above analysis separately across multiple data sets to see how robust any finding are. This might also reveal platform/lab specific biases.

## Datasets

#### Single Cell RNA-Seq (GEO)
There are a number of single cell RNA-Seq datasets available. Some studies focus on drug treatments or co-morbidities which are probably out of scope. I looked for datasets with a straightforward study design.

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213216
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203191
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE179640

#### Bulk RNA-Seq of cultured cells
Bulk RNA-Seq has limited value for samples with a mixture of cells. I found an interesting data set where RNA-Seq was done on organoids from patient cells. It has pairs of samples from healthy endometrial tissue as well as endometriosis from the same patients. The organoids probably have expression patterns different from cells in vivo, but they can be compared to the single cell clusters to help identify them.

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE118928

## Analysis

## Technology Stack