from PIL import Image
import os
import re
import random

dir_from = "C:/practice/"
dir_to = "C:/saveimages/"

filename1 = "C:/practice/file1.jpg"

print(re.match(r"(.+?)\..+", os.path.basename(filename1)).group(1))

def Crop_image(filename, new_file_direc, cropp_size):

    #the first parameter of the function is filename (string)
    #the second parameter of the function is final directory (string)
    #the third parameter is how much do you want to crop (int)
    im = Image.open(filename)

    cropp = cropp_size
    width, height = im.size
    cropped_im = im.crop((cropp, cropp, width-cropp, height-cropp))


    cropped_filename = re.match(r"(.+?)\..+", os.path.basename(filename)).group(1)

    path = "{}/{}.jpg".format(dir_to, cropped_filename)
    rand_num = random.randrange(1, 100000000000000)
    extra_path = "{}/{}_{}.jpg".format(new_file_direc, cropped_filename, str(rand_num))

    check_file = os.path.isfile(path)

    if check_file is False:
        cropped_im.save(path)
        print("the file is saved at "+path)    
    else:
        cropped_im.save(extra_path)
        extra_path_variable =+ 1
        print("the file is saved at "+extra_path)

# list to store files
file_list = []

# Iterate directory
for path in os.listdir(dir_from):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_from, path)):
        file_list.append(path)

for file in file_list:
    #number of file in queue
    image_name = file
    Crop_image(os.path.join(dir_from, image_name), dir_to, 10)