

import os
from PyPDF2 import PdfMerger

source_dir = os.getcwd()

merger = PdfMerger()
name = ""

for item in [f for f in os.listdir(source_dir) if (f.endswith('pdf') or f.endswith('PDF'))][:9]:
    if item.endswith('pdf') or item.endswith('PDF'):
        print(item)
        name += item[:item.find('.')] + " "
        merger.append(item)

merger.write('{0}-merged.pdf'.format(name[:4].rstrip()))
merger.close()