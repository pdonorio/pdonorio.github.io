#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Who am i? """

name = 'Paolo'
surname = "D'Onorio De Meo"
work = 'Cineca'
domain = 'Italy'

DOT = '.'
AT = '@'
SPACE = ' '
EMPTY = ''
QUOTE = "'"

mydata = {}

# Argh
clean_surname = surname.replace(QUOTE, EMPTY)

# Email address @work
mydata['email'] = name[0].lower() + DOT + clean_surname.lower().replace(SPACE, EMPTY) + \
    AT + work.lower() + DOT + domain[:2].lower()
# Twitter account
mydata['twitter'] = AT + name.lower() + DOT + \
    clean_surname[:clean_surname.find(SPACE)].lower()
# Github account
mydata['github'] = AT + name[0].lower() + \
    clean_surname[:clean_surname.find(SPACE)].lower()

# Print 'em all
for account, value in mydata.iteritems():
    print(account + ': ' + value)

