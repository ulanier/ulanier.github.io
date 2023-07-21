import os
import re

c = 0
os.chdir("D:\Rainier Online Class\sir bino message\gallery")
list = os.listdir()
list.sort(key=int)
print(list)
for i in list:
    _, ext = i.split(".")
    if ext == "jpg":
        os.rename(i,f"{c}.jpg")

    c+=1