import os
import shutil


def move_file_to_directory(name, extensions, source, destination):
    dest_path = destination + name + extensions
    copy = 2
    print("FINAL PATH STEP #2:", destination)
    print("FINAL PATH STEP #3:", dest_path)
    if (name + extensions) == "Organize Folder":
        print("I DON'T WHY BUT IT DOESN'T FEEL RIGHT TO MOVE THIS FOLDER...\nI WILL NOT MOVE IT")
        return
    elif os.path.exists(destination) != True:
        print("DESTINATION DOESN'T EXIST (NOT GOOD)")
        print("destination:", destination)
        os.makedirs(str(destination))
        print("SITUATION IS UNDER CONTROL")
    elif os.path.exists(dest_path) == True:
        print("DESTPATH ALREADY EXIST (NOT GOOD)")
        try:
            while os.path.exists(dest_path) == True:
                new_name = destination + "/" + \
                    name + "_" + str(copy) + extensions
                os.rename(source, new_name)
                copy = +1
        except:
            print("I GUESS I KINDA BREAK ?...")
        else:
            print("SITUATION IS UNDER CONTROL")
    else:
        print("DESTPATH DOESN'T EXIST (GOOD) ")
        print("-")
        print("BEGINNING:", source)
        print("END:", destination+name+extensions)
        shutil.move(source, destination)
        print("{} has been moved in {} ".format(
            os.path.basename(source), destination))
        return 0


def organize_folder(folder):
    counter = 0
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(filename)

        installer = "Installers"
        font = "Fonts"
        documents = "1 - 📄 Documents/"
        code = documents + "Code/"
        js = code + "JS/"
        htmlcss = code + "HTML-CSS"
        python = code + "Python"
        android = code + "Android"
        doc = documents + "Doc"
        sheet = documents + "Sheet"
        slides = documents + "Slides"
        google = documents + "Google/"
        g_doc = google + "Doc"
        g_sheet = google + "Sheet"
        g_slides = google + "Slides"
        images = "2 - 🖼 Images/"
        saves = images + "Saves"
        vector = images + "Vector"
        photos = images + "Photos"
        web = images + "Web"
        music = "3 - 🎵Music"
        videos = "4 - 🎬Videos"
        archives = "5 - 📚 Archives"
        arch_images = archives + "Images"
        skin = "Skins/"
        rainmeter = skin + "Rainmeter"
        d = {
            # "": "Folders",
            ".exe": installer,
            ".msi": installer,
            ".html": htmlcss,
            ".css": htmlcss,
            ".py": python,
            ".js": js,
            ".json": js,
            ".apk": android,
            ".txt": doc,
            ".md": doc,
            ".doc": doc,
            ".docx": doc,
            ".rtf": doc,
            ".odt": doc,
            ".pdf": doc,
            ".gdoc": g_doc,
            ".csv": sheet,
            ".xlsx": sheet,
            ".xls": sheet,
            ".gsheet": g_sheet,
            ".pptx": slides,
            ".ppt": slides,
            ".gslides": g_slides,
            ".zip": archives,
            ".rar": archives,
            ".7z": archives,
            ".gz": archives,
            ".tar": archives,
            ".iso": arch_images,
            ".rmskin": rainmeter,
            ".ttf": font,
            ".otf": font,
            ".mp4": videos,
            ".mp3": music,
            ".m4a": music,
            ".gif": web,
            ".tif": web,
            ".jpg": photos,
            ".jpeg": photos,
            ".png": photos,
            ".svg": vector,
            ".eps": vector,
            ".psd": saves,
            ".ai": saves,

        }
        print("FILENAME:", filename)
        sub_path = d.get(extension.lower())
        print("PATH EXTENSION:", sub_path)
        print("-")

        if sub_path is not None:
            ante_dest = folder + "/" + "↪ Organize Folder ↩"
            destination = ante_dest + "/" + sub_path + "/"
            source = folder + "/" + filename
            print("FOLDER:", folder)
            print("SOURCE:", source)
            print("FINAL PATH STEP #1:", ante_dest)
            move_file_to_directory(name, extension, source, destination)
            
            if move_file_to_directory == 0:
                counter += 1
            print("------")
        else:
            print("The extention file {} as not been yet implemented".format(extension))
            print("------")

    if counter == 0:
        print("It's already organized :)")
    else:
        print("We have moved {} files".format(counter))
