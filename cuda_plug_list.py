#!/usr/bin/env python3.7

import sys
import os
import zipfile
import configparser
 
PRE = """# CudaText Plugins List (WIP)
<details><summary>How to install</summary>  
Copy plugin directory to _py_ directory that lives alongside CudaText executable.  
</details>  
  
  
TODO:  
* ~~fix formatting~~
* add list ordered by popularity  
---


"""

add_readmes = True
 
 
def main():
  if len(sys.argv) == 2:
    zipsdir = sys.argv[1]
  else:
    zipsdir = input('Enter folder where plugin zips lie: ')
    
  zipnames = sorted(os.listdir(zipsdir))
  
  res = []
  
  efs = 0
  for zipname in zipnames:
    zippath = os.path.join(zipsdir, zipname)
    with zipfile.ZipFile(zippath, 'r') as zipf:
      try:
        readmetxt = zipf.read('readme/readme.txt').decode('utf-8')
      except:
        print(f'no readme:{os.path.split(zippath)[1]}')
      
      inf = zipf.read('install.inf').decode('utf-8')
      try:
        # clip to avoid configparser error
        name,descr = get_name_descr('\n'.join(inf.split('\n')[:10]))
      except Exception as ex:
        print(f'error:{os.path.split(zippath)[1]} ({ex})')
        continue
        
      try:
        # clip to avoid configparser error
        git = get_git('\n'.join(inf.split('\n')[:10]))
      except Exception as ex:
        print(f'error git:{os.path.split(zippath)[1]} ({ex})')
        continue
      
      if not name:
        folder,filename = os.path.split(zippath)
        name,ext = os.path.spliext(filename)
      
      res.append(format(name, descr, readmetxt, git))
      
      efs += 1
  print(f'efs:{efs}')
  
  utf2file(PRE + '\n   \n   \n'.join(res), 'plugins_with_readmes.md')
      
      
def format(name, descr, readme, git):
  res = f'* [{name}]({git})'
  if descr:
    res += f' - {descr}  '
  if add_readmes  and  readme:
    readme = '    '+readme.replace('\n', '\n    ')+'    ' # markdown demands indentation
    res += f'\n    <details><summary>readme</summary>\n    \n    ```  \n    {readme}    \n    ```  \n    </details>\n    '
  return res
      

def get_name_descr(txt):
  if not txt:
    return '', ''
  config = configparser.ConfigParser()
  config.read_string(txt)
  
  return config['info']['title'], config['info']['desc']
  

def get_git(txt):
  if not txt:
    return '', ''
  config = configparser.ConfigParser()
  config.read_string(txt)
  
  return config['info']['homepage']
  
  
def utf2file(ustr, filepath):
  with open(filepath, 'w', encoding='utf-8') as text_file:
    text_file.write(ustr)
 
if __name__ == '__main__':
  main()
    