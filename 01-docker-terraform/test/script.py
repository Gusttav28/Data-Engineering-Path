from pathlib import Path
from datetime import datetime

now = datetime.now()


current_dir = Path.cwd() # getting the current working directory (cwd)
current_file = Path(__file__).name # getting the name of all the files that are there
print("\n")
print(f"files in {current_dir}: ") # showing the directory in where we are

for file_path in current_dir.iterdir():   # iterdir works to make the iteration of the dir
    if file_path.name == current_file:
        continue                          # if on of the one files match with the what is inside of the dir
    
    print(f" - {file_path.name}")        # show them
    
    if file_path.is_file():                 # if the files has something inside lets read them and show the content
        content = file_path.read_text(encoding='utf-8')
        print(f"   Content: {content}")
        

print("Currently time and date: ", now)
print("\n")