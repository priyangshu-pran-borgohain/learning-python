import os
import shutil

FOLDER_PATH = input("Enter folder path to organize: ")

files = os.listdir(FOLDER_PATH)

for file in files:
    if os.path.isfile(os.path.join(FOLDER_PATH, file)):
        ext = file.split(".")[-1].lower()

        if ext in ["jpg", "png", "jpeg", "gif"]:
            folder = "Images"
        elif ext in ["pdf", "docx", "txt"]:
            folder = "Documents"
        elif ext in ["mp4", "mkv", "avi"]:
            folder = "Videos"
        elif ext in ["mp3", "wav"]:
            folder = "Music"
        else:
            folder = "Others"

        folder_path = os.path.join(FOLDER_PATH, folder)
        os.makedirs(folder_path, exist_ok=True)

        shutil.move(
            os.path.join(FOLDER_PATH, file),
            os.path.join(folder_path, file)
        )

print("Files organized successfully!")
