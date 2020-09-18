#Introduction of the code
"""The aim of this script is to organize your download folder by placing files in a sub-folder regarding of their extension"""
import os
import shutil
import getpass

def dot_exe_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Installer\\" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    #print(a)
    test=os.path.exists(destination) #check if the folder exist or not
    if test == True:
        shutil.move(a,destination) #move the file to the destination
    else:
        os.mkdir(destination) # create the folder that doesn't exist
        shutil.move(a,destination) #move the file to the destination
    print(x," has been moved to:",destination,)

def dot_rmskin_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Skins\\Rainmeter\\" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    #print(a)
    test=os.path.exists(destination) #check if the folder exist or not
    if test == True:
        shutil.move(a,destination) #move the file to the destination
    else:
        os.mkdir(destination) # create the folder that doesn't exist
        shutil.move(a,destination) #move the file to the destination
    print(x," has been moved to:",destination,)

def dot_fonts_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Fonts\\" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    #print(a)
    test=os.path.exists(destination) #check if the folder exist or not
    if test == True:
        shutil.move(a,destination) #move the file to the destination
    else:
        os.mkdir(destination) # create the folder that doesn't exist
        shutil.move(a,destination) #move the file to the destination
    print(x," has been moved to:",destination,)

def dot_video_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=path_raw+"Videos\\Downloaded video's" #destination of the file
    a=path_download_directory+x #recreate the path of the file*
    #print(a)
    test=os.path.exists(destination) #check if the folder exist or not
    if test == True:
        shutil.move(a,destination) #move the file to the destination
    else:
        os.mkdir(destination) # create the folder that doesn't exist
        shutil.move(a,destination) #move the file to the destination
    print(x," has been moved to:",destination,)

def archives_dir_download(x,y): # x is the complete name of the file and y is the current folder
    destination=y+"Archives\\" #destination of the file
    a=path_download_directory+x #recreate the path of the file
    #print(a)
    test=os.path.exists(destination) #check if the folder exist or not
    if test == True:
        shutil.move(a,destination) #move the file to the destination
    else:
        os.mkdir(destination) # create the folder that doesn't exist
        shutil.move(a,destination) #move the file to the destination
    print(x," has been moved to:",destination,)



#Main body

#Part 1 (Main)
USER_ID=r'{}'.format(getpass.getuser())
USER_ID_MANUEL=""
while True:
    yes_or_no=str(input('Is your download directory is C:\\Users\\'+ str(USER_ID) +'\\Downloads ? \nwrite yes or no: '))
    if yes_or_no == "yes":
        path_raw="C:\\Users\\"+ str(USER_ID) +"\\"
        path_download_directory="C:\\Users\\"+ str(USER_ID) +"\\Downloads\\"
        print("------------")
        break
    elif yes_or_no == "no":
        USER_ID_MANUEL=(str(input(r"Please write down your exact user ID:")))
        path_raw="C:\\Users\\"+ str(USER_ID) +"\\"
        path_download_directory="C:\\Users\\"+ str(USER_ID_MANUEL) +"\\Downloads\\"
        path_download_directory.replace('\\', '\\\\')
        print("------------")

        break
    else:
        print("That answer was not expected. Please write yes or no")
        print("------------")

counter=0


#Part 2 (in \\Download)
file_list=os.listdir(path_download_directory) # in the  workspace directory "\\Downloads"
#print(path_download_directory)# print the current workspace path
#print(file_list)
print("---------")

for file in file_list:
    file_Name, file_Extension = os.path.splitext(file)
    #print(file_Extension)

    if file_Extension == ".exe":
        dot_exe_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".msi":
        dot_exe_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".zip":
        archives_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".rar":
        archives_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".7z":
        archives_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".iso":
        archives_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".rmskin":
        dot_rmskin_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".ttf":
        dot_fonts_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".otf":
        dot_fonts_dir_download(file,path_download_directory)
        counter+=1
        print("---")

    if file_Extension == ".mp4":
        dot_video_dir_download(file,path_download_directory)
        counter+=1
        print("---")

if counter==0:
    print("It's already organized :)")
else:
    print("We have moved",counter,"files")

print("---------")

print("------------")

input("Press Enter to finish")