import re

words = 'werwl4o242wde]w[dlwf\t\tdsds:s,a.a'

words = re.sub(r'[^a-zA-Z0-9]', ' ', words)
print(words)