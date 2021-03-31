# -*- coding: utf-8 -*-
# 1020 Idade em Dias
a = int(input()) 
x = a / 365
a = a % 365
y = a /30
a = a % 30
z = a
print("%d ano(s)" % x)
print("%d mes(es)" % y)
print("%d dia(s)" %z)