# import os

# files = os.listdir("c:\\Users\Jai\Desktop\\Docs")
# for i in files:
#     size = os.path.getsize(f"c:\\Users\Jai\Desktop\\Docs\\{i}")
#     print(f"{i}:\t{size//1024} MB")

# using glob which is much better

import os
from pathlib import Path

files = Path("c:\\Users\Jai\Desktop\\Docs")
all_files = files.glob("*")

for i in list(all_files):
    print(f"{Path(i).name}: {os.path.getsize(i)//1024} MB")
