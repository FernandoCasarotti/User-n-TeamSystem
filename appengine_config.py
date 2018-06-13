# -*- coding: utf-8 -*-
import os
from google.appengine.ext import vendor

libpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
vendor.add(libpath)
