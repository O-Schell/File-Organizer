import getpass
import os

from lib import organize_folder


def build_name_of_directory(id_):
    return os.path.join("C:/Users", id_, "Downloads")


def main():
    USER_ID = r"{}".format(getpass.getuser())
    download_path = build_name_of_directory(USER_ID)
    while True:
        yes_or_no = input(
            "Is your download directory is {}? \nwrite yes or no: ".format(
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


if __name__ == "__main__":
    main()
