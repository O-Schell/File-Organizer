import getpass
import os
import sys
from lib import organize_folder


def build_name_of_directory(id_):
    return os.path.join("C:/Users", id_, "Downloads")


def main():
    USER_ID = r"{}".format(getpass.getuser())
    path = build_name_of_directory(USER_ID).replace("\\", "/")

    while True:
        print("By default, we clean your download directory but you can use for whatever folder you want ! ")
        input("press 'enter' to continue\n")

        path_choice = input(
            "Choose by typing the number\n1 - (default) Download Folder\n2 - Another folder\nYour choice: ")

        if path_choice == "1" or path_choice == "":
            yes_or_no_dlf = input(
                "Do you confirm that your download directory is {} ? \nwrite yes or no: ".format(path))
            if yes_or_no_dlf in ("yes", "no"):
                if yes_or_no_dlf == "no":
                    custom_id = str(
                        input(r"Please write down your exact user ID: "))
                    path = build_name_of_directory(custom_id)
                break
        elif path_choice == "2":
            path = str(input(r"Please write the exact path of the folder: "))
            break
        elif path_choice == "stop":
            sys.exit()
        else:
            print("That answer was not expected. Please write yes or no")
            print("------------")

    organize_folder(path)
    input("press 'enter' to finish")


if __name__ == "__main__":
    main()
