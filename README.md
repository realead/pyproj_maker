# pyproj_maker
template for my python projects

## Usage:

To create a project sceleton call:

    python pyproj_make.py --name <lib_name> --targetfolder <path/to/lib>

to check the result:

    (cd <path/to/lib>/<lib_name>/tests && sh test_install.sh)

in this case a new virtual environment is created, the needed libraries are installed and the created library is build/installed. Also unit tests are run. The environment is deleted afterwards.

Call `sh test_install.sh from-github` to check the installation from github.

Call `sh test_install.sh local keep` to keep the virtual environment after the run.

A less costly alternative is to use `test_in_active_env.sh` which installs the library in developer-mode in the active environment and runs unit tests.

### Adjustments

It is possible to add further files to the created project by adding files to `_TEMPLATE` folder.

The string `__NAME__` will be replaced by the lib_name (i.e. name passed via argument `--name`). Only text file are possible. On the content of these files `.format(name=lib_name)` is applied. That means

   * "my name is {name}" becomes "my name is XXX" if XXX is the given name
   * "my name is {{name}} becomes "my name is {name}"
`

## Requirements:

   * For Linux (sh)
   * Python>=3.5

