#Introduction of the code
"""The aim of this script is to organize your download folder by placing files in sub-folder regarding of their extension"""
import os
import shutil
import getpass

def dot_exe_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Installer/" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    print(a)
    shutil.move(a,destination) #move the file to the destination

def dot_msi_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Installer/" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    print(a)
    shutil.move(a,destination) #move the file to the destination

def dot_rmskin_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Rainmeter/" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    print(a)
    shutil.move(a,destination) #move the file to the destination

def dot_otf_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Polices/" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    print(a)
    shutil.move(a,destination) #move the file to the destination

def dot_ttf_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Polices/" #destination of the file
    a=path_download_directory+x #recreate the path of the file*
    print(a)
    shutil.move(a,destination) #move the file to the destination

def archives_dir_installer(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Fichiers archives/" #destination of the file
    print(destination)
    a=path_download_installer+x #recreate the path of the file
    print(a)
    shutil.move(a,destination) #move the file to the destination




#Main part
#Part 1

USER_ID=r'{}'.format(getpass.getuser())
while True:
    yes_or_no=str(input('Is your download directory is C:/Users/'+ str(USER_ID) +'/Downloads ? \nwrite yes or no: '))
    if yes_or_no == "yes":
        path_download_directory="C:/Users/"+ str(USER_ID) +"/Downloads/"
        print("------------")
        break
    elif yes_or_no == "no":
        path_download_directory=(str(input(r"Please write down the exact path of the 'Download' directory:")))+"/"
        path_download_directory.replace("\\" , "/" )
        print("------------")

        break
    else:
        print("That answer was not expected. Please write yes or no")
        print("------------")




file_list=os.listdir(path_download_directory) # in the directory "Downloads"
print(path_download_directory)
print(file_list)
print("------")

for file in file_list:
    file_Name, file_Extension = os.path.splitext(file)
    print(file_Extension)

    if file_Extension == ".exe":
        dot_exe_dir_download(file,path_download_directory)
        print("---")

    if file_Extension == ".msi":
        dot_msi_dir_download(file,path_download_directory)
        print("---")

    if file_Extension == ".rmskin":
        dot_rmskin_dir_download(file,path_download_directory)
        print("---")

    if file_Extension == ".ttf":
        dot_ttf_dir_download(file,path_download_directory)
        print("---")

    if file_Extension == ".otf":
        dot_otf_dir_download(file,path_download_directory)
        print("---")
print("------")

#Part 2
path_download_installer=path_download_directory+"Installer/"
file_list=os.listdir(path_download_installer)# in the directory "Downloads/Installer"
print(path_download_installer)
print(file_list)
print("------")

for file in file_list:
    file_Name, file_Extension = os.path.splitext(file)
    print(file_Extension)

    if file_Extension == ".zip":
        archives_dir_installer(file,path_download_installer)
        print(file_Name)
        print("---")

    if file_Extension == ".rar":
        archives_dir_installer(file,path_download_installer)
        print(file_Name)
        print("---")

    if file_Extension == ".7z":
        archives_dir_installer(file,path_download_installer)
        print(file_Name)
        print("---")

    if file_Extension == ".iso":
        archives_dir_installer(file,path_download_installer)
        print(file_Name)
        print("---")
print("------")