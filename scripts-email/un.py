import re

p = re.compile(ur'60160399#perm!terra|msgid=e')
test_str = u"imap[13744]: user jonatan.vsilva!terra (60160399#perm!terra) from 200.176.1.100: save: box=Lixeira, uid=46, msgid=a, size=5610"
print re.findall(p, test_str)






















