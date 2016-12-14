#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import threading
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", help="a base config file")
parser.add_argument("-s", "--suqare", type = int, help = "back a square nmber you give")
parser.add_argument('--base', dest='base_config', default=None,
                        help='''Specify a file that holds the base execution
                                configuration.''')
args = parser.parse_args()


print args
print args.a
print "the sum is %d" % args.suqare
print "base config is %s" % args.base_config

