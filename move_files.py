import os 
import shutil
from_dir = "C:\\Users\\abbas\\Downloads"
to_dir = "A:\\New1"
list_files = os.listdir(from_dir)
for file_name in list_files:
    name, extension = os.path.splitext(file_name)
    if(extension == ""):
        continue
    if(extension in [".txt",".doc",".docx",".pdf"]):
        path1 = from_dir + "\\" + file_name
        path2 = to_dir + "\\" + "Image_file"
        path3 = to_dir + "\\" + "Image_file" + "\\" + file_name
        if(os.path.exists(path2)):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)