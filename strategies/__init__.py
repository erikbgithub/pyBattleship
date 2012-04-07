# -*- coding: utf-8 -*-

from os import listdir
from os.path import dirname

all = [x.replace(".py", "") for x in
       filter(lambda x: x.endswith(".py") and not x.startswith("Abstract") and not x.startswith("_"),
           listdir(dirname(__file__)))]