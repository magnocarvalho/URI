# -*- coding: utf-8 -*-
# 1019 Conversão de Tempo

a = int(input())
x = a / 3600
a = a % 3600
y = a /60
a = a % 60
z = a
print("%d:%d:%d\n" % (x,y,z))