#组  ()
import re

a='pythonpythonpython222'

r = re.findall('(python){3}',a)

print(r)