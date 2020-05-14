# commandline tool for organising folder
# Options: Uses

# --ext or -e : arrange according to extension

# --name or -n : arrange according to name

# --pat or -p : arrange according to pattern

# --deep or -d : deep arrangement [ subfolders in folders ]. It has 2 arguments:
# 1 -> name->pat->ext
# 2 -> ext->pat->name

# --compress or -c : converts the folder to zip file (default). It has the following arguments:
# tar-> tar.xz ( only linux and mac )
# zip-> zip format (compatible with all platforms )
# 7z-> .7z format (must be installed in mac and windows. Present in linux)

# --lock or -l : encrypts the folder or file with password. It takes 1 arguments password.
# Warning: losing password would cause you to loose data

import argparse
import folder_manager_functions as fm
from time import time

start_time= time()

deep_info= '''
    --deep or -d : deep arrangement [ subfolders in folders ]. It has 2 arguments:
        1 -> name->ext\n
        2 -> ext->name
'''

compress_info= '''
    --compress or -c : converts the folder to zip file (default). It has the following arguments:
        xztar-> tar.xz ( only linux and mac )\n
        gztar-> tar.gz ( only linux and mac )\n
        zip-> zip format (compatible with all platforms )\n
'''

lock_info= '''
    --lock or -l : encrypts the folder or file with password. It takes 1 arguments password.
    Warning: losing password would cause you to loose data
    Default password: 'password'
'''



def main():
    # parser object
    parser= argparse.ArgumentParser(description="Python based folder manager CLI Tool.\nPython3.x required.\n --help for more information")

    # commandline arguments
    parser.add_argument('-e', '--ext', default = None, metavar="path", nargs = 1, help="arrange according to extension")
    parser.add_argument('-n', '--name', default = None, metavar="path", nargs = 1, help="arrange according to name")
    parser.add_argument('-p', '--pat', default = None, metavar="path", nargs = 1, help="arrange according to common pattern")

    parser.add_argument('-d', '--deep', default= [1, None], nargs= 2, metavar=('type', 'path'), help= deep_info)
    parser.add_argument('-c', '--compress', default= ['zip', None], nargs= 2, metavar=('format', 'path'), help= compress_info)
    parser.add_argument('-l', '--lock', default= ['password', None], nargs= 2, metavar=('password', 'path'), help= lock_info)

    # parsing arguments from parser object
    args = parser.parse_args()

    # calling functions defined in folder_manager_functions module
    if args.ext != None:
        fm.ext_arrange(args.ext)
    
    if args.name != None:
        fm.name_arrange(args.name)
    if args.deep[1] !=None:
        fm.deep_arrange(args.deep)
    if args.compress[1] != None:
        fm.compress(args.compress)

if __name__== '__main__':
    main()