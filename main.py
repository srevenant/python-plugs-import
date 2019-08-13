#!/usr/bin/env python3

import sys
import os
import re
import importlib
from dictlib import Dict

# the entrypoint of this stack

PLUG_DIR = '.'

def load_plug(plug, pkg, server):
    mod = importlib.import_module(pkg + '.' + plug)
    print("==> creating instance of plug " + plug)
    return Dict(
      mod=mod,
      instance=mod.Handler(server),
      name=plug
    )

def main(plugs_package):
    plugs = list()
    for fname in os.listdir(os.path.join(PLUG_DIR, plugs_package)):
        if not os.path.isfile(os.path.join(PLUG_DIR, plugs_package, fname)):
           continue
        if not re.search(r'^[a-z0-9]+.py$', fname):
            print("skipping file in plugs folder: " + fname)
            continue
        plug = re.sub(r'\.py$', '', fname)
        plugs.append(load_plug(plug, plugs_package, {}))

    print("==> As sample, calling .hello on each plug now")
    for plug in plugs:
        print("--- " + plug.name)
        plug.instance.hello("from main")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please include a plugs folder as an argument")
    main(sys.argv[1])
