# -*- coding: utf-8 -*-
# 1013 - O Maior
a, b, c = map(int, input().split())
aux = ((a+b+abs(a-b))/2)
aux = ((aux+c+abs(aux-c))/2)
print("%d eh o maior" % aux)
