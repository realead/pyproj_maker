import os
import pathlib
import argparse

def write_content(file_name, content):
    with open(file_name,'w') as f:
        f.write(content)

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, type=str, help='name of the project')
parser.add_argument('--targetfolder', default='.', type=str, help='folder where the project will be created')

arguments = parser.parse_args()

my_name = arguments.name
my_target_folder = arguments.targetfolder

# create directory:
print("creating root folder:", my_target_folder + "/" + my_name)
pathlib.Path(my_target_folder, my_name).mkdir(parents=True, exist_ok=True) 



## from _TEMPLATE folder:    
rootdir = '_TEMPLATE'
name_place_holder='__NAME__'
def process_path(current_path):
    for child in current_path.iterdir():
        target_parts = [ x.replace(name_place_holder, my_name) for x in child.relative_to(rootdir).parts]
        target = pathlib.Path(my_target_folder, my_name, *target_parts)
        print("Job: ", child,"=>",target)
        if child.is_dir():
            print("\tcreating folder:", target)
            target.mkdir(parents=True, exist_ok=True) 
            process_path(child)
        else:
            text = child.read_text()
            text = text.format(name=my_name)
            print("\twriting file:", target)
            target.write_text(text)


process_path(pathlib.Path(rootdir))



