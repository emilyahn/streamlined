import glob
import os
import sys


''' convert LIUM output into rttm and write file.
	assume {lium_dir} has folders (1 per wav file)
	TO RUN:
		python lium_to_rttm.py {lium_dir} {out_dir}
'''


def lium_to_rttm(sys_txt_infile, sys_rttm_outfile, file_basename):

	with open(sys_txt_infile, 'r') as f:
		# format lium output ex: svtmg001 1 67281 310 F S U S107
		# assuming timestamp units are in 10milliseconds
		sys_lines = [line.strip().split() for line in f.readlines() if ';;' not in line]

	with open(sys_rttm_outfile, 'w') as w:
		for line in sys_lines:
			spkr_name = line[7]
			onset = float(line[2])/100
			duration = float(line[3])/100
			outline = 'SPEAKER {} 1 {} {} <NA> <NA> {} <NA> <NA>\n'.format(file_basename, onset, duration, spkr_name)
			w.write(outline)


if __name__ == '__main__':

	lium_dir = sys.argv[1]
	sys_dir = sys.argv[2]

	for lium_file in glob.glob('{}/*/*.ev_is.120.txt'.format(lium_dir)):
		basename = os.path.basename(lium_file).split('.')[0]
		out_file = '{}/{}.rttm'.format(sys_dir, basename)
		lium_to_rttm(lium_file, out_file, basename)
