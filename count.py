from os import listdir
from os.path import isfile, join
path = "output/"
path_files = [path + f for f in listdir(path) if isfile(join(path, f))]
all_rows = 0

for p in path_files:
  with open(p, 'r', encoding="utf8") as f:
    c = 0
    for x in f:
      c = c + 1
    print("{0} has {1} rows".format(p, c))
    all_rows = all_rows + c

print("total rows: {0}".format(all_rows))