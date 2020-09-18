import os
import shutil


def move_file_to_directory(file, destination):
    print(file)
    if not os.path.exists(file):
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(file, destination)
        print("{} has been moved to: {}".format(os.path.basename(file), destination))
    else:
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
            destination = os.path.join(folder, sub_path)
            source = os.path.join(folder, filename)
            move_file_to_directory(source, destination)
            counter += 1
    if counter == 0:
        print("It's already organized :)")
    else:
        print("We have moved {} files".format(counter))