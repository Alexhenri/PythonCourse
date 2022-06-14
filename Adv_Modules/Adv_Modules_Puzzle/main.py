'''

In this project we should unzip a file and inside it, we see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-####
We use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.

'''

import os
import re
import shutil

'''
os module to open the files
re to create a regular expression to find the phone numbers
shutil to extract all 
'''



def unzip_origin_file(filename = '', filepath = '', output = ''):

    if filename == '':
        filename = 'unzip_me_for_instructions.zip'
    elif '.zip' not in filename:
        filename = filename + '.zip'

    full_filename = filepath + filename
    output_file = 'puzzle_adv_files'
    format = 'zip'

    try:
        shutil.unpack_archive( full_filename, output_file, format)
    except:
        print("Sorry but wasn't possible to extract {}! Please check the name and the path".format(full_filename))
        return

    print("File successfully unzipped")
    return

def find_phone_re(content):
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
    phone = re.findall(phone_pattern, content)
    return phone

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Pass a file to unzip, path and ouput, otherwise will get the unzip_me_for_instructions.zip and set output to puzzle_adv_files
    unzip_origin_file()

    # Set unzipped dir
    unzipped_dir = 'puzzle_adv_files'

    #initializate telephone list - [ (file, number) ]
    phone_list = []

    # Used os.walk to get folders recursively
    for root, sub_folders, files in os.walk(unzipped_dir):
        for file in files:
            full_path_file = os.path.join(root, file)
            print(full_path_file)
            # Reading Files
            with open(full_path_file, 'rb') as f:
                f_content = f.read().decode('utf-8')

                # Check with regular expressions if has any phone
                phone = find_phone_re(f_content)

                # If found any phone, add to phone list with the respective file
                if phone:
                    phone_list.append((full_path_file, phone))


    for file, phone in phone_list:
        print("File:{} PhoneNumber:{}".format(file, phone))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
