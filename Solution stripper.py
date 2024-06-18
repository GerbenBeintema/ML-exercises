import json
import re
import os

def strip(dirname, filename):

    name = os.path.join(dirname, filename)
    with open(name,'rb') as f:
        s = f.read().decode('utf-8')
    out = json.loads(s)
    #Code
    cells = [o for o in out['cells'] if o['cell_type']=='code']
    for cell in cells:
        cell['execution_count'] = None #remove count
        cell['outputs'] = [] #remove output
        outlines = []
        ident = None
        for line in cell['source']:
            # print(line)
            #if an identifier has been used
            result = re.search("#[a-z]=\)", line)
            if result: 
                outlines.append(line[:line.find('=')+1] + ' # ' + result.group()[1] + ') Fill this\n')
                continue

            if ident and line.strip()=='':
                continue
            if ident:
                if not re.search(f"#{ident}\)", line):
                    ident = None
            #check if an identifier is present
            if ident is None:
                result = re.search("#[a-z]\)", line)
                if result:
                    
                    # print(dir(result))
                    ident = result.group()[1]
                    indent = re.match('[ ]{1,}', line)
                    indent = '' if indent is None else indent.group()
                    outlines.append(indent + '# ' + result.group()[1] + ') Fill this\n')
                else:
                    outlines.append(line)

        cell['source'] = outlines

    #markdown
    cells = [o for o in out['cells'] if o['cell_type']=='markdown']
    for cell in cells:
        outlines = []
        for line in cell['source']:
            result = re.search('\*\*Answer [a-z]\):\*\*', line )
            if result:
                outlines.append(result.group() + ' fill by student\n')
            else:
                outlines.append(line)

        cell['source'] = outlines

    name = os.path.join(dirname, filename[4:])
    json.dump(out, open(name,'w'))
 
# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        if filename[:4]=='sol_' and filename.endswith('.ipynb') and len(dirName.split('\\'))<=2:
            print('dir =',dirName,', name =',filename)
            strip(dirName,filename)

import subprocess
subprocess.run(['mdpdf','-o','Lecture 1 Python and ML intro/Install-python-anaconda-markdown.pdf',\
    'Lecture 1 Python and ML intro/Install-python-anaconda.md'])
subprocess.run(['rm','mdpdf.log'])
