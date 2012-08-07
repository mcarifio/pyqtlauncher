#!/usr/bin/python3
# -*- Mode: python; indent-tabs-mode: nil; tab-width: 4 -*- # for emacs

import sys
import os
import string
import logging
import argparse
import pickle




# in case you're running in place
sys.path.insert(0, os.path.dirname(__file__))
logging.basicConfig(level = logging.DEBUG)

if '__main__' == __name__:
    try:
        logging.debug(' '.join(sys.argv))


        # Let's use argparse to parse an example set of args
        parser = argparse.ArgumentParser()
        # add args here

        parser.parse_args()
        pickle.dump(parser, sys.stdout)



    except Exception as e:
        logging.error(e)
