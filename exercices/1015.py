# -*- coding: utf-8 -*-
# 1015 Distância Entre Dois Pontos
import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
p1 = x2 - x1
p2 = y2 - y1
r1 = p1 * p1
r2 = p2 * p2
z = math.sqrt(r1 + r2)
print("%.4f" % z)
