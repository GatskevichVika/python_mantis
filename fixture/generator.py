from model.project import Project
import random
import string
import os.path
import getopt
import sys

class GeneratorHelper:

    def __init__(self, app):
        self.app = app


    def random_string(self):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(10)])
