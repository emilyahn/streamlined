# STREAMLInED

Shared Tasks for Rapid, Efficient Analysis of Many Languages in Emerging Documentation.

Research @ University of Washington.

Contact Emily Ahn with questions: eahn [at] uw [dot] edu


## Prerequisites

* python 3
* [dscore](https://github.com/nryant/dscore)
* java JDK 1.7 or 1.8


## Data

Our data originates from the Endangered Languages Archive ([ELAR]( http://elar.soas.ac.uk/)).

Selected languages for this task span a wide range of language families and typological groups.

* Sakun
* Cicipu
* Effutu

#### Instructions to download from ELAR:

1. Create an online account profile (free [here](https://lat1.lis.soas.ac.uk/ds/RRS_V1/RrsRegistration))
2. Login and downlaod your cookies as a txt file (browser extensions can handle this well)
3. Run our script to curl (download) the data: `scripts/download_elar.py`

#### Provided files per language include:

* elar\_{lang}\_links.tsv (to be used by script when downloading files from ELAR)
* .uem file (Un-partitioned Evaluation Map--determines the regions to be analyzed in each recording; see [description](https://github.com/nryant/dscore#uem))
* ref/ (rttm files)


## Track 1: Speaker Diarization

Who spoke when, and where else did they speak again?
This task takes raw audio as input and attempts to detect speech and cluster groups of speech from the same speaker together under one label.


### 1.1 Baseline System

We use the lightweight system from [LIUM](https://github.com/StevenLOL/LIUM) that uses ILP clustering techniques.
Download the code from that repository and follow their installation instructions.
If you are using JDK 1.8, replace their jar file in the `LIUM/` folder with the jar found in this repository (then rename it or change its call from their `go.sh` script: `baseline/diar/lium-diarization-200129.jar` (compiled on Jan 29, 2020).
Instructions to compile this JDK 1.8 compatible version on your own machine are [here](https://github.com/ahmetaa/lium-diarization).

We provide a script to convert LIUM output into rttm format: `scripts/lium_to_rttm.py`

### 1.2 Evaluation

Assuming you have your system output as .rttm files in the folder `data/{lang}/sys/`, run dscore on this folder with the `data/{lang}/ref/` folder, and output to `data/{lang}_dev.stdout`.

`dscore/score.py -r data/{lang}/ref/*.rttm -s data/{lang}/sys/*.rttm > data/{lang}/{lang}_dev.stdout 2> ccp/{lang}_dev.stderr -u data/{lang}/{lang}.uem`

#### Expected Results

| Language     | DER                |
|--------------|--------------------|
| Cicipu       | 44.54           |
| Effutu       | 34.65        |
| Sakun        | 62.55      |

### 1.2 Similar Work

The DIHARD Challenge I (2018, [site](https://coml.lscp.ens.fr/dihard/2018/index.html)) and Challenge II (2019, [site](https://coml.lscp.ens.fr/dihard/), [paper](https://coml.lscp.ens.fr/dihard/2019/dh2019_is_overview.pdf)) have focused on robust speaker diarization.
Their second challenge [baseline](https://github.com/iiscleap/DIHARD_2019_baseline_alltracks) involes the Kaldi toolkit.


## Next Tracks TBD...

Possibly: Speaker Identification, Genre Identification