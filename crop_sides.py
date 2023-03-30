from PIL import Image
import os
import re
import random

directory_from = "C:/practice/"
directory_to = "C:/saveimages/"


def сrop_image(filename: str, new_file_directory: str):
    """
    filename parameter of the function is filename (string)
    new_file_directory parameter of the function is final directory (string)
    """
    image = Image.open(filename)

    cropp = 10
    width, height = image.size
    cropped_image = image.crop((cropp, cropp, width-cropp, height-cropp))


    cropped_filename = re.match(r"(.+?)\..+", os.path.basename(filename)).group(1)

    path = "{}/{}.jpg".format(directory_to, cropped_filename)
    random_number = random.randrange(1, 100000000000000)
    extra_path = "{}/{}_{}.jpg".format(new_file_directory, cropped_filename, str(random_number))

    check_file = os.path.isfile(path)

    if check_file is False:
        cropped_image.save(path)
        print("the file is saved at "+path)    
    else:
        cropped_image.save(extra_path)
        extra_path_variable =+ 1
        print("the file is saved at "+extra_path)

# list to store files
file_list = []

# Iterate directory
for path in os.listdir(directory_from):
    # check if current path is a file
    if os.path.isfile(os.path.join(directory_from, path)):
        file_list.append(path)

for file in file_list:
    #number of file in queue
    image_name = file
    сrop_image(os.path.join(directory_from, image_name), directory_to)
