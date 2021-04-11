# -*- coding: utf-8 -*-
# 1021 - Notas e Moedas
t = input()
if(float(t) >= 0 and float(t) <= 1000000):
    s = t.split(".")
    n = int(s[0])
    c = int(s[1])
    print("NOTAS:")
    print("%d notas(s) de R$ 100.00" % int(n // 100))
    n = n % 100
    print("%d notas(s) de R$ 50.00" % int(n // 50))
    n = n % 50
    print("%d notas(s) de R$ 20.00" % int(n // 20))
    n = n % 20
    print("%d notas(s) de R$ 10.00" % int(n // 10))
    n = n % 10
    print("%d notas(s) de R$ 5.00" % int(n // 5))
    n = n % 5
    print("%d notas(s) de R$ 2.00" % int(n // 2))
    n = n % 2
    print("MOEDAS:")
    print("%d moedas(s) de R$ 1.00" % n)
    print("%d moedas(s) de R$ 0.50" % int(c // 50))
    c = c % 50
    print("%d moedas(s) de R$ 0.25" % int(c // 25))
    c = c % 25
    print("%d moedas(s) de R$ 0.10" % int(c // 10))
    c = c % 10
    print("%d moedas(s) de R$ 0.05" % int(c // 5))
    c = c % 5
    print("%d moedas(s) de R$ 0.01" % c)
