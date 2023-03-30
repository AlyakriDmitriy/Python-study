from PIL import Image
import os
import re
import random

directory_from = "C:/practice/"
directory_to = "C:/saveimages/"

def crop_image(filename: flt, new_file_directory: flt, block_size: int):
    
    """
    the first parameter of the function is directory of the file + filename (string)
    the second parameter of the function is final directory (string)
    the third parameter is what is the size of blocks in pixel to you want to divide the image (int)
    """
    image = Image.open(filename)
    
    block = block_size
    width, height = image.size

    #number of blocks we need, we divide width by 10, divide height by 10, multiply first result and second
    #we need +1 because some parts might be left not counted
    width_blocks = (width//block)+1
    height_blocks = (height//block)+1
    
    cropped_filename = re.match(r"(.+?)\..+", os.path.basename(filename)).group(1)
    #output "file1"
    #this checks if the directory to save is exist, if it doesn't, it creates one.
    check_file = os.path.exists(new_file_direc)
    if check_file is False:
        os.makedirs(new_file_direc)

    #file_path_variable = random.randrange(1, 100000000000000)
    #file_path = "{}/{}_{}.jpg".format(new_file_direc, cropped_filename, str(file_path_variable))
    #print("the original file_path is " + str(file_path_variable))

    
    # I made while loop in while loop , this one is vertical.
    top_parameter = 0
    bottom_parameter = block
    i_vertical = 1
    while i_vertical < height_blocks:
        # I made while loop in horizontal 
        i_horizontal = 1
        left_parameter = 0
        right_parameter = block
    

        while i_horizontal < width_blocks:
            file_path_variable = random.randrange(1, 100000000000000)
            file_path = "{}/{}_{}.jpg".format(new_file_directory, cropped_filename, str(file_path_variable))


            #if by small chance the random file name exists, 
            check_file2 = os.path.isfile(file_path)
            if check_file2 is True:
                file_path_variable += random.randrange(10000000000, 10000000000000000)
                file_path = "{}/{}_{}.jpg".format(new_file_directory, cropped_filename, str(file_path_variable))


            cropped_image = image.crop((left_parameter, top_parameter, right_parameter, bottom_parameter))
            cropped_image.save(file_path)
            
            i_horizontal += 1
            left_parameter += block
            right_parameter += block
            file_path_variable = random.randrange(1, 100000000000000)
            print("file is save in "+file_path)


        
        i_vertical += 1
        top_parameter += block
        bottom_parameter += block

# folder path

# list to store files
file_list = []

# Iterate directory
for path in os.listdir(dir_from):
    # check if current path is a file
    if os.path.isfile(os.path.join(directory_from, path)):
        file_list.append(path)
print(file_list)

for file in file_list:
    #number of file in queue
    image_name = file
    crop_image(os.path.join(directory_from, image_name), directory_to, 100)
