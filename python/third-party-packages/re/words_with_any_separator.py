import re

line = 'aut	1;4;1'

text = re.compile('\w+').findall(line)