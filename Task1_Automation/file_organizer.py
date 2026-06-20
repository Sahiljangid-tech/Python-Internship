import os
import shutil
from datetime import datetime

folder_path = input("Enter folder path: ")

try:
    files = os.listdir(folder_path)

    documents_folder = os.path.join(folder_path, "Documents")
    images_folder = os.path.join(folder_path, "Images")
    videos_folder = os.path.join(folder_path, "Videos")

    os.makedirs(documents_folder, exist_ok=True)
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)

    log_path = os.path.join(folder_path, "log.txt")

    with open(log_path, "a") as log:

        image_count = 1

        for file in files:

            source = os.path.join(folder_path, file)

            if os.path.isdir(source):
                continue

            # PDF
            if file.endswith(".pdf"):
                destination = os.path.join(documents_folder, file)
                shutil.move(source, destination)

                print(file, "moved to Documents")
                log.write(f"{datetime.now()} - {file} moved to Documents\n")

            # Images
            elif file.endswith(".png") or file.endswith(".jpg"):

                extension = os.path.splitext(file)[1]
                new_name = f"image_{image_count}{extension}"

                destination = os.path.join(images_folder, new_name)

                shutil.move(source, destination)

                print(file, "renamed and moved to Images")

                log.write(
                    f"{datetime.now()} - {file} renamed to {new_name} and moved to Images\n"
                )

                image_count += 1

            # Videos
            elif file.endswith(".mp4") or file.endswith(".mkv"):

                destination = os.path.join(videos_folder, file)

                shutil.move(source, destination)

                print(file, "moved to Videos")

                log.write(
                    f"{datetime.now()} - {file} moved to Videos\n"
                )

    print("\nTask Completed Successfully!")

except Exception as e:
    print("Error:", e)