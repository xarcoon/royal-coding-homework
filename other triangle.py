# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GnUU7kCNLR8kJ__4JN6LmsDkDvHGbt3m
"""

x = "*"
space = " "
n = int(input('number of asterisks at top::'))
r1= n*x
r2= (n-2)*x
r3= (n-4)*x
r4= (n-6)*x
r5= (n-8)*x
r6= (n-9)*x
triangle = [r1,space+r2,space+space+r3,space+space+space+r4,space+space+space+space+r5,space+space+space+space+space+r6+space]

if (n%2)!= 0 and n>=3 and n<=11:
     for y in triangle:
      print(y)

elif (n%2)==0:
  print('triangle cannot be formed')
else:
  print('triangle not possible due to lack of space')

