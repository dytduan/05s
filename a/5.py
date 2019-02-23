#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
s=s.replace(".","")
print(s)
ss=s.rsplit(" ")
print(ss)
di={}
for i in ss:
    key=di.get(i);
    if(key==None)