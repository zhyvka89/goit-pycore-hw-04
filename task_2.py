from pathlib import Path


def get_cats_info(path):
  file_path = Path(path)

  if file_path.exists():
    try:
      with open(file_path) as fh:
        cat_list = []
        cat_lines = [el.strip() for el in fh.readlines()]

        for cat_el in cat_lines:
          res = cat_el.split(',')
          cat_dict = dict()
          for el in res:
            if(el.isdigit()):
              cat_dict["age"] = el
            elif(any(chr.isdigit() for chr in el)):
              cat_dict["id"] = el
            else:
              cat_dict["name"] = el
          cat_list.append(cat_dict)
          
        return cat_list
    except:
      print("Oops, something went wrong")
  else:
    print("File does not exist!")


cats_info = get_cats_info(r'C:\Users\Comp100\Desktop\New Text Document.txt')
print(cats_info)