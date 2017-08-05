# -*- coding: utf-8 -*-
import re
log_file = open('exemplos_de_log.xml', 'r')


id_perm = "60160399#perm!terra"
regex_01 = re.compile(ur'delete|expunge')

count = 0
log_list = []
for line in log_file:
	if id_perm in line and "expunge" in line or id_perm in line and "delete" in line or id_perm in line and "save" in line:
		#print '%s' %w
		log_list.append(line)
		count += 1


#for item in log_list:
#	print '%r' % item

count = 0
while count < len(log_list):
	print log_list[count]
	count += 1
	if len(log_list) == count:
		print "O n de linhas da log_list eh %r" % count












    

#import re
#
#idlist = []
#
#file = open('Log.txt','r')
#for line in file:
#	if 'expunge' in line:
#		idlist.append(re.search(r'msgid=.*?,',line).group(0))
#file.close()
#
#
#count = 0 
#count2 = 0
#
#line_list = []
#
#file = open('Log.txt','r')
#for line in file:
#	line_list.append(line)
#
#
#
#for id in idlist:
#	print '---------------'
#	for line in line_list:
#		if id in line:
#			print line





#count = 0
#for line in log_file:
#	if re.search(regex1, line):
#		print line
#		count += 1
#print count


#regex1 = re.compile(ur'(6543405#perm!terra)|(out=18337)')
#regex2 = re.compile(ur'6543405#perm')
#regex3 = re.compile(ur'(6543405#perm!terra)|(out=[\w\d]+,)')


#frog = """10.235.200.26 dovecot: imap[3800]: user santanna.roberto!terra (6543405#perm!terra) 177.212.37.214: folder=[INBOX]=444 time=327 CLOSE=1/167/24/0/0 SELECT=1/29226/388 UID MOVE=1/72597/49/1 UID SEARCH=1/12144/16 UID STORE=1/65/0/0"""
#frog = "SELECT=1/3666/388/68/89"
#http://www.gossamer-threads.com/lists/python/python/375364
#Exemplos de como fazer tratar colunas nas linhas de logs tipo o awk
#print frog
#print frog.split()[0,7]
#print "frog cru: ", frog
#frog2 = frog.split("=")
#print frog2
#for i in frog2:#
#	print i

#stri = frog2[1]
#print stri
#stri = stri.split("/")[0:4]
#print stri
#print len(frog2)
