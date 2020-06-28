# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# regex that matches file name with america style date:  MM-DD-YYYY
datePattern = re.compile(
    r""" 
      ^(.*?)                           # anything before date
      (0?[1-9]|1[0-2])-                # Month
      (0?[1-9]|[12][0-9]|3[01])-       # Date
      (19[5-9][0-9]|20[0-4][0-9])      # year [1950 - 2049]
      (.*?)$                           # anything after date 
  
    """,
    re.VERBOSE,
)

# Loop over files in wordking directory
for americanFile in os.listdir("c:/Users/Jai/Desktop/Docs/"):
    mo = datePattern.search(americanFile)
    if mo == None:  # skip files without date
        continue
    # get the different parts of filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    datePart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    # form the european style filename
    europeanFile = f"{beforePart}{datePart}-{monthPart}-{yearPart}{afterPart}"

    # get the full absolute path
    absworkingdir = os.path.abspath("c:/Users/Jai/Desktop/Docs/")
    americanFile = os.path.join(absworkingdir, americanFile)
    europeanFile = os.path.join(absworkingdir, europeanFile)

    # TODO : rename the files
    print(f"renaming {americanFile} --> {europeanFile}...")
    shutil.move(americanFile, europeanFile)
