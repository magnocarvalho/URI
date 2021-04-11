# -*- coding: utf-8 -*-
# 1036 - Fórmula de Bhaskara
import math
v1, v2, v3 = map(float, input().split())
delta = (v2 * v2) - (4 * v1 * v3)
if(delta > 0 and v1 != 0):
    raiz = math.sqrt(delta)
    r1 = ((-v2)+raiz)/(2 * v1)
    r2 = ((-v2)-raiz)/(2 * v1)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)
else:
    print("Impossivel calcular")
