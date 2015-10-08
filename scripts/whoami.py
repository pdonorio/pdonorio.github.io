#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Who am i? """

################################
name = 'Paolo'
surname = "D'Onorio De Meo"
work = 'Cineca'
domain = 'Italy'
################################

DOT = '.'
AT = '@'
SPACE = ' '
EMPTY = ''
QUOTE = "'"
mydata = {}

# In case you have a surname with quotes...!
clean_surname = surname.replace(QUOTE, EMPTY)

#################################################
# Email address @work
mydata['email'] = name[0].lower() + DOT + clean_surname.lower().replace(SPACE, EMPTY) + \
    AT + work.lower() + DOT + domain[:2].lower()
# Twitter account
mydata['twitter'] = AT + name.lower() + DOT + \
    clean_surname[:clean_surname.find(SPACE)].lower()
# Github account
mydata['github'] = AT + name[0].lower() + \
    clean_surname[:clean_surname.find(SPACE)].lower()


#################################################
""" Defining a simple ipython extension """
import six
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class HelloWorldMagics(Magics):
    """ An extension about my (ego) self """
    DEFAULT = 42

    @line_magic
    @cell_magic
    def helloworld(self, line='', cell=None):
        print("Hello World!\n\tWho am i?\n")
        for account, value in six.iteritems(mydata):
            print(account + ': ' + value)
        return self.DEFAULT

def load_ipython_extension(ip):
    ip.register_magics(HelloWorldMagics)
