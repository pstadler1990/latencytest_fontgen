"""
Simple script to automatically convert all printable ASCII characters
to bitmap font arrays via imagemagick
"""
import os

FONT = 'FreeMono'
SIZE = '16'
OUTPUT_DIR = 'output/'

# Printable (visible) ascii range is 33..126
# http://facweb.cs.depaul.edu/sjost/it212/documents/ascii-pr.htm
for c in range(33, 126):
    if c is 92:
        # skip \
        continue
    if c in [34, 39, 62, 96]:
        # Escape those chars
        use_esc = str("\\")
    else:
        use_esc = ''
    os.system('convert -font {font} -pointsize {size} label:"{esc}{char}" {dir}tmp.xbm'
              .format(font=FONT, size=SIZE, char=chr(c), esc=use_esc, num=c, dir=OUTPUT_DIR))

