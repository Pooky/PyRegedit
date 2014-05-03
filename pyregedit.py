#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

#sys.path.insert(0, '/usr/share/pyregedit')

from Controllers import Controller

def main():
	controller = Controller()
	controller.initApp() # Init app

if __name__ == "__main__":
    main()



