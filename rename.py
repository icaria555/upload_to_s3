from os import listdir
from os.path import isfile, join
import os, time

path = "output/"
path_files = [path + f for f in listdir(path) if isfile(join(path, f))]
all_rows = 0

for p in path_files:
  name, ftype = p.split('/')[1].split('.')
  year, month = name.split('_')
  new_name_path = path +  year + (('0' + month) if len(month) == 1 else month)  + '.' + ftype
  os.rename(p, new_name_path)
  time.sleep(1) # 1 secound