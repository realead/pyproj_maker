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
my_path = os.path.join(arguments.targetfolder, my_name)

# create directory:
pathlib.Path(my_path).mkdir(parents=True, exist_ok=True) 


# create setupfile
setup_file_content = """
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

extensions = Extension(
            name='{name}.{name}',
            sources = ["src/{name}/{name}.pyx"]
    )
extensions = cythonize(extensions, compiler_directives={{'language_level' : 3}})

kwargs = {{
      'name':'{name}',
      'version':'0.1.0',
      'description':'a project',
      'author':'Egor Dranischnikow',
      'url':'https://github.com/realead/{name}',
      'packages':find_packages(where='src'),
      'package_dir':{{"": "src"}},
      'license': 'MIT',
      'ext_modules':  extensions,

       #ensure pxd-files:
      'package_data' : {{ '{name}': ['*.pxd','*.pxi']}},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}}
setup(**kwargs)
""".format(name=my_name)


setup_file = os.path.join(my_path, "setup.py")
write_content(setup_file, setup_file_content)

#sources:
src_folder = os.path.join(my_path, 'src', my_name)
pathlib.Path(src_folder).mkdir(parents=True, exist_ok=True) 

init_file_content = """
__version__ =  (0,1,0)
"""
init_file = os.path.join(src_folder, '__init__.py')
write_content(init_file, init_file_content)

pyx_file_content = """
def test_me():
    return 42
"""
pyx_file = os.path.join(src_folder, my_name+'.pyx')
write_content(pyx_file, pyx_file_content)


#tests:
tests_folder = os.path.join(my_path, 'tests')
pathlib.Path(tests_folder).mkdir(parents=True, exist_ok=True) 


test_install_file = os.path.join(tests_folder, 'test_install.sh')
test_install_content = """
set -e

ENV_DIR="../p3"
virtualenv -p python3 "$ENV_DIR"

#activate environment
. "$ENV_DIR/bin/activate"

#install needed packages:
pip install cython


if [ "$1" = "from-github" ]; then
    echo "Installing setup.py from github..."
    pip install https://github.com/realead/{name}/zipball/master
else
    echo "Installing local setup.py..."
    for dir_name in "build" ".eggs" "dist"
    do
        if [ -d "../$dir_name" ]; then
           echo "clean build, deleting ../$dir_name directory"
           rm -r "../$dir_name"
        fi; 
    done  
    (cd .. && python setup.py install)
fi;

echo "Installed packages:"
pip freeze

#tests:
sh run_unit_tests.sh

#clean or keep the environment
if [ "$2" = "keep" ]; then
   echo "keeping enviroment $ENV_DIR"
else
   rm -r "$ENV_DIR"
fi;
""".format(name=my_name)

write_content(test_install_file, test_install_content)


run_unittests_file = os.path.join(tests_folder, 'run_unit_tests.sh')
run_unittests_content = """
(cd unit_tests && python -m unittest discover -s . -v)
"""
write_content(run_unittests_file, run_unittests_content)


test_active_file = os.path.join(tests_folder, 'test_in_active_env.sh')
test_active_content = """
pip install -e ../.
sh run_unit_tests.sh 
"""
write_content(test_active_file, test_active_content)


##unit tests
unittests_folder = os.path.join(tests_folder, 'unit_tests')
pathlib.Path(unittests_folder).mkdir(parents=True, exist_ok=True)

version_test_file = os.path.join(unittests_folder, 'test_version.py')
version_test_content = """
import unittest

import {name}


class VersionTester(unittest.TestCase): 

   def test_major(self):
      self.assertEqual({name}.__version__[0], 0)

   def test_minor(self):
      self.assertEqual({name}.__version__[1], 1)

   def test_last(self):
      self.assertEqual({name}.__version__[2], 0)
""".format(name=my_name)

write_content(version_test_file, version_test_content)


unittests_folder = os.path.join(tests_folder, 'unit_tests')
pathlib.Path(unittests_folder).mkdir(parents=True, exist_ok=True)

pyx_test_file = os.path.join(unittests_folder, 'test_'+my_name+'.py')
pyx_test_content = """
import unittest

import {name}.{name} as t


class {name}Tester(unittest.TestCase): 

   def test_test_me(self):
      self.assertEqual(t.test_me(), 42)
""".format(name=my_name)

write_content(pyx_test_file, pyx_test_content)




