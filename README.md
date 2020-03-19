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

Provided files per language include:

* sph/ (script to convert .sph to .wav format: `scripts/sph_to_wav.sh`)
* .uem file (Un-partitioned Evaluation Map--determine the regions to be analyzed in each recording; see [description](https://github.com/nryant/dscore#uem))


## Track 1: Speaker Diarization

Who spoke when, and where else did they speak again?
This task takes raw audio as input and attempts to detect speech and cluster groups of speech from the same speaker together under one label.


### 1.1 Baseline System

We use the lightweight system from [LIUM](https://github.com/StevenLOL/LIUM) that uses ILP clustering techniques.
Download the code from that repository and follow their installation instructions.
If you are using JDK 1.8, replace their jar file in the `LIUM/` folder with the jar found in this repository (then rename it or change its call from their `go.sh` script: `baseline/diar/lium-diarization-200129.jar` (compiled on Jan 29, 2020).
Instructions to compile this JDK 1.8 compatible version on your own machine are [here](https://github.com/ahmetaa/lium-diarization).


#### Expected Results


### 1.2 Similar Work

The DIHARD Challenge I (2018, [site](https://coml.lscp.ens.fr/dihard/2018/index.html)) and Challenge II (2019, [site](https://coml.lscp.ens.fr/dihard/), [paper](https://coml.lscp.ens.fr/dihard/2019/dh2019_is_overview.pdf)) have focused on robust speaker diarization.
Their second challenge [baseline](https://github.com/iiscleap/DIHARD_2019_baseline_alltracks) involes the Kaldi toolkit.


## Next Tracks TBD...

Possibly: Speaker Identification, Genre Identification