import os
import shutil


def move_file_to_directory(name, extensions, source, destination):
    dest_path = destination + "/" + name + extensions
    copy=2
    print("FINAL PATH STEP #2:", destination)
    print("FINAL PATH STEP #3:", dest_path)
    if os.path.exists(dest_path) == True:
        print ("DESTPATH ALREADY EXIST (NOT GOOD)")
        while os.path.exists(dest_path) == True:
            new_name = destination + "/" + name + "_" + str(copy) + extensions
            os.rename( source, new_name)
            copy =+1
    else:    
        print ("DESTPATH DOESN'T EXIST (GOOD) ")
        print("---")
        if not os.path.exists(destination):
            print("destination: ", destination)
            os.mkdir(destination)
        print("shutil.move 1:", source)
        print("shutil.move 2:", destination)
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
        print("FILENAME:", filename)
        sub_path = d.get(extension)
        print("PATH EXTENSION:",sub_path)
        print("-")

        if sub_path is not None:
            ante_dest = folder + "/" + "Organize Folder" 
            destination = ante_dest + "/" + sub_path
            source = folder + "/" + filename
            print("FOLDER:",folder)
            print("SOURCE:",source)
            print("FINAL PATH STEP #1:", ante_dest)
            
            move_file_to_directory(name, extension, source, destination)
            if move_file_to_directory == 0:
                counter += 1
            print("------")
        else:
            print("------")
            
    if counter == 0:
        print("It's already organized :)")
    else:
        print("We have moved {} files".format(counter))
