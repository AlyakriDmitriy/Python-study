from PIL import Image
import os
import re
import random

directory_from = "C:/practice/"
directory_to = "C:/saveimages/"


def сrop_image(filename: str, new_file_directory: str, crop_size: int):
    """
    filename parameter of the function is filename (string)
    new_file_directory parameter of the function is final directory (string)
    crop_size parameter of the function is how much persent do you want to crop (int)
    """
    image = Image.open(filename)

    #we can't cut more the 50% from each side, if I set a limit of 50 %.

    width, height = image.size
    if crop_size > 50:
        crop_size = 50

    #count how much we need to cut
    cropp_w = int(width*(crop_size*0.01))
    cropp_h = int(height*(crop_size*0.01))
    


    
    


    cropped_image = image.crop((cropp_w, cropp_h, width-cropp_w, height-cropp_h))


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


#directories = ['dir1', 'dir2']
#file_list = get_files_from_directories(directories)



#def get_files_from_directories(directories):
#    file_list = []
#
#    # Iterate over all directories
#    for directory_from in directories:
#        # Iterate over all files in the directory
#        for path in os.listdir(directory_from):
#            # Check if current path is a file
#            if os.path.isfile(os.path.join(directory_from, path)):
#                file_list.append(os.path.join(directory_from, path))
#
#    return file_list




#def add_to_directories(event=None):
#    if event and event.widget == add_button:
#        directories.append(my_entry.get())
#    elif not event or event.keysym == 'Return':
#        directories.append(my_entry.get())
#    my_entry.delete(0, END)
#    print(directories)

#my_entry = Entry(root)
#my_entry.pack()

#add_button = Button(root, text='Add a path', command=add_to_directories)
#add_button.pack()

#my_entry.bind("<Return>", add_to_directories)

#root.mainloop()


for file in file_list:
    #number of file in queue
    image_name = file
    сrop_image(os.path.join(directory_from, image_name), directory_to)
