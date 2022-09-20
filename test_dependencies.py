import os

for dirpath, dirnames, filenames in os.walk("."):
    for f in filenames:
        print(os.path.join(dirpath, f))
