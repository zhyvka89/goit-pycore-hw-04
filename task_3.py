import sys
from colorama import Fore, Back, Style
from pathlib import Path

def parse_folder(path, tab=0):
  tab += 1
  margin = '\t' * tab

  for el in path.iterdir():
    if el.is_dir():
        print(Fore.BLUE + f"{margin} {el.name}")
        parse_folder(el, tab)
    else:
        print(Fore.YELLOW + f"{margin} {el.name}")
   

dir = Path(sys.argv[1]).parent

if (dir.exists()):
  parse_folder(dir)
else:
  print(Back.GREEN + 'File not Found!')