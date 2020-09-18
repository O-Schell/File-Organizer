import os
import shutil


def move_file_to_directory(filename, file, destination):
    print(filename)
    dest_path = destination + filename
    if not os.path.exists(dest_path):
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(file, destination)
        print("{} has been moved to: {}".format(os.path.basename(file), destination))
        return 0
    else:
        rename *.* *_COPY.*
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
            move_file_to_directory(filename, source, destination)
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