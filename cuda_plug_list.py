#!/usr/bin/env python3.7

import sys
import os
import zipfile
import configparser
import json
 
PRE = """# CudaText Plugins List (WIP)
<details><summary>How to install</summary>  
Copy plugin directory to _py_ directory that lives alongside CudaText executable.  
</details>  
  
  
TODO:  
* ~~fix formatting~~
* add list ordered by popularity
---


"""

output = "README.md"
add_readmes = False
categories = True
 
 
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
  
  if categories:
    res = categorize(res)
  
  utf2file(PRE + '\n   \n   \n'.join(res), output)
      
      
def format(name, descr, readme, git):
  res = f'* [{name}]({git})' # depends_A
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
  

#FIXME handle plugins with the same name (Find in files)
def categorize(l):
  with open('tags.json', 'r', encoding='utf-8') as f:
    tags = json.load(f)
    
  result = []
  for tag,names in tags.items(): # dict preserves order since python3.7
    result.append(f'* ## {tag}')
    
    for name in names:
      tofind = f'* [{name}](' # depends_A
      # find plugin item
      item = None
      for tmpitem in l:
        if tofind in tmpitem:
          item = tmpitem
          break
      else:
        print(f'~ Couldnt find item in formatteds: <{tag}>.<{name}>')
        continue
      
      # list subitems indetation
      item = '    '+item.replace('\n', '\n    ')+'    '
      result.append(item)
      
  return result

    

  
  
def utf2file(ustr, filepath):
  with open(filepath, 'w', encoding='utf-8') as text_file:
    text_file.write(ustr)
 
if __name__ == '__main__':
  main()
    