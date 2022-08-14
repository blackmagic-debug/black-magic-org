#!/usr/bin/env python3

import glob
import os.path
from pathlib import PurePath

import sys
import os

# Find all the pinout data directories
# independent from our current working directory
script_dir = os.path.dirname(sys.argv[0])
for path in glob.glob(script_dir + '/**/pinout_diagram.py'):
    p = PurePath(path).parts
    diagram_name = p[-2]
    print("diagram script: " + path)
    print("diagram_name: " + diagram_name)

    # run pinout diagram generator
    # (we can't just import manager and run it from here
    #  as it contaminates the environment and
    #  only one diagram comes out right...)
    os.system('python3 -m pinout.manager -o --export ' +
              path + ' ' +
              os.path.join(script_dir, diagram_name + "-legend.svg"))