# Imports
import os
import shutil

# variables and the special terms list
special_terms = ["tax","finance","personal","passwords","medical"]
topleveldirpath = "C:\\test_folder"
copytopath = "C:\\test_dest\\"

# error handler (by default os.walk trys to ignore the errors)
def error_handler(exception_instance):
    print(f"Error: {exception_instance.filename}") 

# walk through the dir logic 
def browsefiles(topdir,terms,cpto):
    for (folder,sub_folders,files) in os.walk(topdir, onerror=error_handler):
        print("Currently folder: "+ folder)
        for name in files:
            if any(filename in name.lower() for filename in terms) == True:
                getfiles((os.path.join(folder, name)),(os.path.join(cpto, name)))
            else:
                print("\t File does not match the search criteria: "+folder+name)
        print('\n')

# copy files to our location logic
def getfiles(src,dest):
    try:
        shutil.copy(src,dest)
        print("\t Grabbed a file and sent it to your destination: "+src)
    except shutil.SameFileError:
        print("\t Source and destination represents the same file.")
        print("\t File: "+src)
    except PermissionError:
        print("\t Permission denied. Unable to copy "+src)
    except:
        print("\t"+" "+src+" "+dest)
        print("\t Error occurred while copying file: "+src)


if __name__ == "__main__":
    browsefiles(topleveldirpath,special_terms,copytopath)
