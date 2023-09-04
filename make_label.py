import os

# origin_dir = "./CACD2000_crop/"
origin_dir = "./UTKFace/"
des_dir = "./data_train_2/"
imgFiles = [file for file in os.listdir(origin_dir)]

# origin_dir = "./FG-NET_224/"
# des_dir = "./data_FG/"
# imgFiles = [file for file in os.listdir(origin_dir)]


def encodeAge(n):
    if n<=10:
        return 0
    elif n<=20:
        return 1
    elif n<=30:
        return 2
    elif n<=40:
        return 3
    elif n<=50:
        return 4
    elif n<=60:
        return 5
    elif n<=70:
        return 6
    else:
        return 7


def makeDir():
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)

    for i in range(8):
        new_folder = os.path.join(des_dir, format(i, "<01"))
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

def moveFiles():
    for file in imgFiles:
        lst = file.split("_")

        age = int(lst[0])

        folder = format(encodeAge(age), "<01")
        origin_file = os.path.join(origin_dir, file)
        des_file = os.path.join(des_dir, folder, file)
        os.rename(origin_file, des_file)

def encodeAgeTest(n):
    if 14<=n<=30:
        return 0
    else:
        return 1

def moveFiles_test():
     for file in imgFiles:
        age = int(os.path.basename(file)[4:6])
        folder = format(encodeAgeTest(age), "<01")
        origin_file = os.path.join(origin_dir, file)
        des_file = os.path.join(des_dir, folder, file)
        os.rename(origin_file, des_file)

makeDir()
moveFiles()
# moveFiles_test()