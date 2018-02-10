import os

def rename_file():
    # (1) Get all files by using os.listdir("PathOfthefile")
    file_list = os.listdir(r"/Users/jasmine/Desktop/prank")
    print(file_list)
    # (2) Because the path may change use os.chdir("samepath")
    os.chdir(r"/Users/jasmine/Desktop/prank")
    for file_name in file_list:
        # (3) Get all files and rename it by using os.rename(old file,new file name)
        # I used file_name.translate to remove all the numbers form the old name
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(r"/Users/jasmine/Desktop/prank")
        

rename_file()
