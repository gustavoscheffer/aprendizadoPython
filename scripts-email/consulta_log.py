#!/usr/bin/env python
# -*- coding: utf-8 -*-



import re


# extract msgid from file lines which match expunge
idlist = []
file = open('logs/Log_gustavo.txt','r')
for line in file:
	if 'expunge' in line:
		idlist.append(re.search(r'msgid=.*?,',line).group(0))
file.close()

print 'Lista de expunges - %s' % len(idlist)

#convert lines in list 

line_list = []
file = open('logs/Log_gustavo.txt','r')
for line in file:
	line_list.append(line)


# Criação da matriz de ações
matrix_list = []
for id in idlist:
	action_list = []
	action_list.append(id)
	
	for line in line_list:
		if id in line:
			action_list.append(line)
	matrix_list.append(action_list)		

print 'Lista de açoes - %s' % len(matrix_list)


count = 0
# verifying actions and set "True" for it.
for action_list in matrix_list:

	save_action = False
	expunge_action = False
	copy_action = False
	delete_action = False
	
	for line in action_list:
		if re.search(r'delete.*?:',line):
			delete_action = True
		if re.search(r'copy.*?:',line):
			copy_action = True
		if re.search(r'save.*:?,',line):
			save_action = True
		if re.search(r'expunge.*:?,',line):
			expunge_action = True

	if delete_action and expunge_action or expunge_action and not delete_action and not copy_action and not save_action:
		count += 1
		print count
		print action_list
		print "---------------"

