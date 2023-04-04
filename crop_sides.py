from PIL import Image
import os
import re
import random
import tkinter as tk
from tkinter import filedialog


directory_from = ''
directory_to = ''
percent = 0



def crop_image(filename: str, new_file_directory: str, crop_size: int):
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

def startcropping():
    global file_list

    for path in os.listdir(directory_from):
        # check if current path is a file
        if os.path.isfile(os.path.join(directory_from, path)):
            file_list.append(path)

    for file in file_list:
        #number of file in queue
        image_name = file
        crop_image(os.path.join(directory_from, image_name), directory_to, int(percent))        
    file_list = []


def entry_directory_from():
    global directory_from
    directory_from = entry1.get()
    print(directory_from)
    

def select_directory_from():
    global directory_from
    directory_from = filedialog.askdirectory()
    print(directory_from)

def entry_directory_to():
    global directory_to
    directory_to = entry2.get()
    print(directory_to)

def select_directory_to():
    global directory_to
    directory_to = filedialog.askdirectory()
    print(directory_to)

def entry_percent ():
    global percent
    percent = entry3.get()
    print(percent)

def creckprint():
    print(directory_from)
    print(directory_to)
    print(percent)


root = tk.Tk()
root.title("Crop images")
root.geometry("400x160")

label1 = tk.Label(root, text="Enter directory path:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

button1 = tk.Button(root, text="Accept directory", command=entry_directory_from)
button1.grid(row=0, column=2, sticky="we")

button2 = tk.Button(root, text="Select directory", command=select_directory_from)
button2.grid(row=1, column=2, sticky="we")

label2 = tk.Label(root, text="Enter folder path to save:")
label2.grid(row=2, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

button3 = tk.Button(root, text="Accept directory to save", command=entry_directory_to)
button3.grid(row=2, column=2, sticky="we")

button4 = tk.Button(root, text="Select directory to save", command=select_directory_to)
button4.grid(row=3, column=2, sticky="we")

label3 = tk.Label(root, text="How much to crop?:")
label3.grid(row=4, column=0)

entry3 = tk.Entry(root)
entry3.grid(row=4, column=1)

button7 = tk.Button(root, text="OK", command=entry_percent)
button7.grid(row=4, column=2, sticky="we")

button5 = tk.Button(root, text="Crop the images", command=startcropping)
button5.grid(row=5, column=2, sticky="we")

root.mainloop()


