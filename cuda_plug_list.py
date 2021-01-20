#!/usr/bin/env python3.7

import sys
import os
import zipfile
import configparser
import json
 
PRE = """# CudaText Plugins List (WIP)
<details><summary>How to install</summary>  
  Copy plugin directory to <code>py</code> directory that lives:
  
  * on portable version - alongside CudaText executable.      
  * on non-portable:
      * Linux, *BSD, Solaris: in <code>~/.config/cudatext</code>, or <code>$XDG_CONFIG_HOME/cudatext</code> if this OS variable is set
      * macOS: in <code>~/Library/Application Support/CudaText</code>
</details>  
  
  
TODO:  
* ~~fix formatting~~
* ~~add list ordered by popularity~~ (Medals on top plugins instead)
* ~~table of contents~~
---


"""

output = "README.md"
add_readmes = False
categories = True
add_medal = True # for top 40
add_table_of_content = True


toskip = set()
 
 
def main():
  if len(sys.argv) == 2:
    zipsdir = sys.argv[1]
  else:
    zipsdir = input('Enter folder where plugin zips lie: ')
    
  zipnames = sorted(os.listdir(zipsdir))
  
  load_toskip()
  
  if add_medal:
    topzips = get_top(40) # zip names of top plugins
  
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
        
        if name in toskip:
          continue
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
      
      medaled = add_medal and zipname in topzips
      
      res.append(format(name, descr, readmetxt, git, medaled=medaled))
      
      efs += 1
  print(f'efs:{efs}')
  
  table_of_contants = ''
  if categories:
    res = categorize(res)
    
    if add_table_of_content:
      with open('tags.json', 'r', encoding='utf-8') as f:
        tags = json.load(f)
      for tag in tags:
        if tag == 'Plugin/Dev': continue # empty category
        if tag == '?': continue 
        table_of_contants += f'* [{tag}](#{tag.lower().replace(" ", "-").replace("/", "")})  \n'    
      table_of_contants += '\n  \n---\n'
  
  
  utf2file(PRE + table_of_contants + '\n   \n   \n'.join(res), output)
      
      
def format(name, descr, readme, git, medaled):
  res = f'* [{name}]({git})' # depends_A
  if medaled:
    res += f' [🥇](a "Top Downloaded")'
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
    
    tag_present = False
    for name in names:
      tofind = f'* [{name}](' # depends_A
      # find plugin item
      item = None
      for tmpitem in l:
        if tofind in tmpitem:
          item = tmpitem
          tag_present = True
          break
      else:
        if name not in toskip:
          print(f'~ Couldnt find item in formatteds: <{tag}>.<{name}>')
        continue
      
      # list subitems indetation
      item = '    '+item.replace('\n', '\n    ')+'    '
      result.append(item)
    
    if not tag_present:
      del result[-1]
    
  return result

    
def get_top(count):
  # file is copied from sourceforge plugin lists: downloads last week
  with open('plugins_dls_week.csv', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
    
  nth_dls = sorted([int(line.split()[-1]) for line in lines])[-count]  # extract last column - dls and sort

  topNthZips = set(line.split()[0] for line in lines  if int(line.split()[-1]) >= nth_dls)  # zip names of top
  return topNthZips
  
  
def load_toskip():
  global toskip
  
  with open('plugins_to_skip.txt', 'r', encoding='utf-8') as f:
    lines = set(line.strip() for line in f.readlines()  if line.strip())
  toskip = lines
  
  
def utf2file(ustr, filepath):
  with open(filepath, 'w', encoding='utf-8') as text_file:
    text_file.write(ustr)
 
if __name__ == '__main__':
  main()
    