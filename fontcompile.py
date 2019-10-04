"""
Reads generated fonts (.xbm) into a single string and renames variables to be valid in C language
"""
import os
import io
import re
import glob

INPUT_DIR = 'font_monospaced_16px/'
OUTPUT_FILE = 'font_monospaced16px.h'

os.chdir(INPUT_DIR)
files = 0
out_str = ''
for n in range(33, 126):
    try:
        with io.open('{}.xbm'.format(n), 'r') as xbm_file:
            ln = xbm_file.readlines()
            # Merge lines 3..6 and prefix the variable with "c_" to be valid in the C language
            str_merged = r''.join(ln[3:6]).replace('\n', '').replace('   ', '').replace(' };', '')
            out_str += '{' + str_merged + '},\n'
            files += 1
    except FileNotFoundError:
        print("File not found", n)
        out_str += '{' + '0x00, ' * 34 + '},\n'
        files += 1

begin_str = '''// Font file generated with fontcompile.py
#define FONT_WIDTH ((uint32_t)11)
#define FONT_HEIGHT ((uint32_t)17)
#define FONT_CHAR_START ((uint32_t)33)
#define FONT_CHAR_END ((uint32_t)126)

static unsigned char chars[''' + str(files) + '''][''' + str(34) + '''] = {
'''

end_str = '\n};'

with io.open(OUTPUT_FILE, 'w') as out_file:
    out_file.write(begin_str)
    out_file.write(out_str)
    out_file.write(end_str)
