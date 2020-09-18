import getpass
import os
import sys


from lib import organize_folder


def build_name_of_directory(id_):
    return os.path.join("C:/Users", id_, "Downloads")


def main():
    USER_ID = r"{}".format(getpass.getuser())
    download_path = build_name_of_directory(USER_ID).replace("\\","/")
    
    while True:
        print("By default, we clean your download directory but you can use for whatever folder you want ! ")
        start=input("press 'enter' to continue")
        yes_or_no = input(
            "Do you confirm that your download directory is {} ? \nwrite yes or no: ".format(
                download_path
            )
        )

        if yes_or_no in ("yes", "no"):
            if yes_or_no == "no":
                custom_id = str(input(r"Please write down your exact user ID:"))
                download_path = build_name_of_directory(custom_id)
            break
        elif yes_or_no == "stop":
            sys.exit()
        else:
            print("That answer was not expected. Please write yes or no")
            print("------------")
    organize_folder(download_path)
    end=input("press 'enter' to finish")


if __name__ == "__main__":
    main()