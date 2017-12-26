# -*- coding:utf-8 -*-
import re;
key = r"javahtmlpythonswiftkotlin"
p1 = r"python"
pattern = re.compile(p1)
matcher = re.search(pattern,key)
print matcher.group()