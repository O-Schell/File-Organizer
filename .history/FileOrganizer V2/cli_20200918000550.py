"""
import sys
import os
from inspect import currentframe, getframeinfo
from pathlib import Path
filename = getframeinfo(currentframe()).filename
parent = Path(filename).resolve().parent
if parent in sys.path:
    print("current path is already in sys.path")
else:
    print("current path isn't already in sys.path and is added")
    sys.path.append(parent)


from pprint import pprint as p
print(sys.path)
print(os.getcwd())
a='lib.py' in os.listdir()
print(a)
"""


import getpass
import os

from lib import organize_folder


def build_name_of_directory(id_):
    return os.path.join("C:/Users", id_, "Downloads")


def main():
    USER_ID = r"{}".format(getpass.getuser())
    download_path = build_name_of_directory(USER_ID).replace("\\","/")
    
    while True:
        print("\r")
        start=input("By default, we clean your download directory but you can use for whatever folder you want !\r press 'enter' to continue")
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
        else:
            print("That answer was not expected. Please write yes or no")
            print("------------")
    organize_folder(download_path)
    end=input("press 'enter' to finish")


if __name__ == "__main__":
    main()