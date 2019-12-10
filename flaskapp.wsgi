#!/usr/bin/python
import os
import sys
import logging

directory = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,directory)
sys.path.insert(1,directory + "/app/")

from app import app as application