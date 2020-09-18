import os
import shutil


def move_file_to_directory(name, extensions, source, destination):
    print(name+extensions)
    dest_path = destination + name + extensions
    copy=2
    while os.path.exists(dest_path) == True:
        new_name = source + name + "_" + copy + extensions
        os.rename(r'source',r'new_name')
        copy =+1
    else:
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(source, destination)
        print("{} has been moved to: {}".format(os.path.basename(source), destination))
        return 0
        
        return


def organize_folder(folder):
    counter = 0
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(filename)
        d = {
            ".exe": "Installer/Download",
            ".msi": "Installer",
            ".doc": "Documents",
            ".docx": "Documents",
            ".pdf": "Documents",
            ".zip": "Archives",
            ".rar": "Archives",
            ".7z": "Archives",
            ".iso": "Archives",
            ".rmskin": "Skins/Rainmeter/",
            ".ttf": "Fonts",
            ".otf": "Fonts",
            ".mp4": "Videos/Downloaded video's",
        }
        sub_path = d.get(extension)

        if sub_path is not None:
            destination = folder + "/" + sub_path
            source = folder + "/" + filename
            move_file_to_directory(name, extension, filename, source, destination)
            print("FOLDER",folder)
            print("SUBPATH",sub_path)
            print("DESTINATION",destination)
            print("SOURCE",source)
            print("------")
            if move_file_to_directory == 0:
                counter += 1
            
    if counter == 0:
        print("It's already organized :)")
    else:
        print("We have moved {} files".format(counter))