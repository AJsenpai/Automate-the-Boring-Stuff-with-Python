# backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os


def backuptoZip(folder):
    os.chdir(folder)
    os.chdir("..")
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFileName):  # if file already present before creation
            break
        number += 1
    # create a zip file
    print(f"creating a zipfile {zipFileName}...")
    with zipfile.ZipFile(zipFileName, "w") as backupZip:
        for folder, subfolder, files in os.walk(folder):
            print(f"Adding files from folder {folder}...")
            backupZip.write(folder)

            for filename in files:
                newBase = os.path.basename(folder) + "_"
                if filename.startswith(newBase) and filename.endswith(".zip"):
                    continue  # don't back up the backup zip files in folder
                backupZip.write(os.path.join(folder, filename))
        print("backup is complete!")
        print(f"backup is available here {os.path.abspath(os.curdir)}...")


backuptoZip("c:/Users/Jai/Desktop/Docs/mydoc")
