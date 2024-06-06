import os
os.chdir("Details/")
for x in range(1,16):
    with open(f"{x}({x}).txt","w") as f1:
        f1.write(f"This is some text about the photo {x}")