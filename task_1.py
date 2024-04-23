from pathlib import Path

def total_salary(path):
  file_path = Path(path)
  
  if file_path.exists():
    try:
      with open(file_path) as fh:
        total_salary = 0
      
        lines = [el.strip() for el in fh.readlines()]
        
        for line in lines:
          res = line.split(',')
          for el in res:
            if (el.isdigit()):
              total_salary += int(el)

        average_salary = int(total_salary / len(lines))
        print(f"Total salaries: {total_salary}, Average salary: {average_salary}")

        return (total_salary, average_salary)
    except:
      print("Oops, something went wrong")  # пустий файл кинула :)
  else:
    print("File does not exist in this directory!")



total_salary(r'C:\Users\Comp100\Desktop\New Text Document.txt')