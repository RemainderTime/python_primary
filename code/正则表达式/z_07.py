#组  ()
import re

a='pythonpythonpython'

r = re.findall('(python){3}',a)

print(r)