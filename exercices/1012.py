# -*- coding: utf-8 -*-
# 1012 Área 
a, b, c = map(float, input().split())
t = (a * c) / 2
ci = 3.14159 * (c * c)
tr = ((a + b) / 2)*c
print("TRIANGULO: %.3f" % t)
print("CIRCULO: %.3f" % ci)
print("TRAPEZIO: %.3f" % tr)
print("QUADRADO: %.3f" % float(b * b))
print("RETANGULO: %.3f" % float(a * b))