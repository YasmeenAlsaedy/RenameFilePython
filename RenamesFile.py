import os

def rename_file():
    file_list = os.listdir(r"/Users/jasmine/Desktop/prank")
    #print(file_list)
    os.chdir(r"/Users/jasmine/Desktop/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(r"/Users/jasmine/Desktop/prank")
        

rename_file()
