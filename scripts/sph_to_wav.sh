#!/bin/bash
# sph_to_wav.sh

sph_dir=$1
wav_dir=$2

for f in `ls -1 ${sph_dir}`; do sox -t sph "${wav_dir}/$f" -b 16  -t wav "${wav_dir}/${f%.*}.wav"; done
