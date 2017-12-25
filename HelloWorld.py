#!/Python27/python
# -*- coding:utf_8 -*-;

print "hello,python";
print "today is friday,i want to go home";
family = "father " + "and " + "mother " + "i " + "love " + "you ";
print family;

print family,"!";

a = b = c = 3;
x,y,z = 1,2,3;

print a,b,c;
print x,y,z;

s = 'ifuckeep';
print s[1:5];

print 5//2;
print 3**3;
if (5 != 3):
    print 1;
else:
    print 0;
print "----------------抢镜的分割线--------------------------------";

a = 1;
b = 1;
if(a and b):
    print "true";
else:
    print "false";

if(a or b):
    print "true";
else:
    print "false";

if not(a and b):
    print "true";
else:
    print "false";

print "----------------抢镜的分割线又来了--------------------------------";

if(a is b):
    print "a = b";
else:
    print "a != b";

if(a == b):
    print "a = b";
else:
    print "a != b";
x = "1";
y = "1";
c = 5000;
d = 5000;

if(c is d):
    print "c is d";
else:
    print "c is not d"

if(c == d):
    print "c == d";
else:
    print "c != d";

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

numbers = [3,12,57,34,1,69,34,2];

while len(numbers) > 0:
    print numbers.pop();

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

for i in [1,2,3,4,5]:
    print i;


print "\n\n\n----------------抢镜的分割线再次出现-------------------";

numbers = [3,12,57,34,1,69,34,2];
for i,j in enumerate(numbers):
    print i, "-", j;

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

arrays = [3,12,57,34,1,69,34,2];
for i in range(len(arrays)):
    for j in range(i+1):
        if(arrays[i] > arrays[j]):arrays[i],arrays[j] = arrays[j],arrays[i];
        print i,j,arrays[i],arrays[j];
print arrays;

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
for j in "fuck":
    for i in letters:
        if(j is i):
            print i;

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

arrays = [3,12,57,34,23,2,1,69,34,2];
list.sort(arrays);
print arrays;
list.reverse(arrays);
print arrays
print arrays.count(3);
print len(arrays),"-",max(arrays),"-",min(arrays);


print "\n\n\n----------------抢镜的分割线再次出现-------------------";

import time;

currentTime = time.localtime(time.time());
print currentTime;
print time.asctime(currentTime);

import calendar;


cal = calendar.month(2017,11);
print cal;

print bin(8)

print "\n\n\n----------------抢镜的分割线再次出现-------------------";


class Bill:
    a = 0;
    def __init__(self):
        Bill.a = 10;

    def get(self):
        print Bill.a;


bill = Bill();
bill.get();

print "\n\n\n----------------抢镜的分割线再次出现-------------------";

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1
del pt2
del pt3

print "\n\n\n----------------抢镜的分割线再次出现-------------------";


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

print "\n\n\n\n\n----------------抢镜的分割线再次出现-------------------";












