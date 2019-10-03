"""
Reads generated fonts (.xbm) into a single string and renames variables to be valid in C language
"""
import os
import io
import re
import glob

INPUT_DIR = 'output/'
OUTPUT_FILE = 'font.h'

RE_MATCH = re.compile(r'(\d+)_bits')

os.chdir(INPUT_DIR)
out_str = '// Font file generated with fontcompile.py\n'
for file in glob.glob("*.xbm"):
    with io.open(file, 'r') as xbm_file:
        l = xbm_file.readlines()
        if len(l) is not 6:
            print("ERROR", file)
        # Merge lines 2..6 and prefix the variable with "c_" to be valid in the C language
        str_merged = re.sub(RE_MATCH, r'c_\1', ''.join(l[2:6]))
        out_str += str_merged

with io.open(OUTPUT_FILE, 'w') as out_file:
    out_file.write(out_str)
