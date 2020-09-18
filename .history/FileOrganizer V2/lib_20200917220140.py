import os
import shutil


def move_file_to_directory(name, extensions, source, destination):
    dest_path = destination + "/" + name + extensions
    copy=2
    print(dest_path)
    print(destination)
    if os.path.exists(dest_path) == True:
        print ("DESTPATH = TRUE")
        while os.path.exists(dest_path) == True:
            new_name = destination + "/" + name + "_" + str(copy) + extensions
            os.rename( source, new_name)
            copy =+1
    else:    
        print ("DESTPATH = FALSE")
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(source, destination)
        print("{} has been moved to: {}".format(os.path.basename(source), destination))
        return 0
        


def organize_folder(folder):
    counter = 0
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(filename)
        d = {
            ".exe": "Installer/Download",
            ".msi": "Installer",
            ".doc": "Documents",
            ".docx": "Documents",
            ".rtf": "Documents",
            ".pdf": "Documents",
            ".zip": "Archives",
            ".rar": "Archives",
            ".7z": "Archives",
            ".iso": "Archives",
            ".rmskin": "Skins/Rainmeter/",
            ".ttf": "Fonts",
            ".otf": "Fonts",
            ".mp4": "Videos/Downloaded video's",
            ".jpg": "Image/Photos",
            ".jpeg": "Image/Photos",
            ".png": "Image/Photos",
            ".svg": "Image/Vector",
        }
        print(filename)
        print(name)
        print(extension)
        print(d.get(extension))
        sub_path = d.get(extension)
        print("subpath: ", sub_path)
        print("-----")
        

        if sub_path is not None:
            destination = folder + "/" + "Organize Folder"+ "/" + sub_path
            source = folder + "/" + filename
            print("FOLDER",folder)
            print("SUBPATH",sub_path)
            print("DESTINATION",destination)
            print("SOURCE",source)
            move_file_to_directory(name, extension, source, destination)
            if move_file_to_directory == 0:
                counter += 1
            print("------")
            
    if counter == 0:
        print("It's already organized :)")
    else:
        print("We have moved {} files".format(counter))