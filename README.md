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
`

## Requirements:

   * For Linux (sh)
   * Python>=3.5

