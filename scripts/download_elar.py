#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv


''' download .wav and .eaf files from ELAR, using cookies and filelist (tsv)
	TO RUN:
		python download_elar.py {lang.tsv} {cookies.txt} {data_dir}
'''


# download .wav and .eaf files from ELAR, using cookies and filelist (tsv)
def get_elar_links(download_tsv, cookies_txt, out_folder):

	# create eaf and wav subdirectories
	os.system('mkdir -p {}/eaf'.format(out_folder))
	os.system('mkdir -p {}/wav'.format(out_folder))

	with open(download_tsv, 'r') as csvfile:
		tsv_lines = csv.DictReader(csvfile, delimiter='\t')
		for row in tsv_lines:
			ext = row['file_url'][-3:].lower()  # in case of 'WAV' -> 'wav'
			outfile = os.path.join(out_folder, ext, '{}.{}'.format(row['id'], ext))
			print(outfile)

			# download via curl
			os.system('curl {} --output {} --cookie {}'.format(row['file_url'], outfile, cookies_txt))


if __name__ == '__main__':

	download_tsv = sys.argv[1]
	cookies_txt = sys.argv[2]
	out_folder = sys.argv[3]
	get_elar_links(download_tsv, cookies_txt, out_folder)
