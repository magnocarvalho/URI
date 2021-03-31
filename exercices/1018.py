# -*- coding: utf-8 -*-
# 1018 cédulas
n = int(input())
if n > 0 and n < 1000000:
    print(n)
    print("%d nota(s) de R$ 100,00" % int(n / 100))
    n = n % 100
    print("%d nota(s) de R$ 50,00" % int(n / 50))
    n = n % 50
    print("%d nota(s) de R$ 20,00" % int(n / 20))
    n = n % 20
    print("%d nota(s) de R$ 10,00" % int(n / 10))
    n = n % 10
    print("%d nota(s) de R$ 5,00" % int(n / 5))
    n = n % 5
    print("%d nota(s) de R$ 2,00" % int(n / 2))
    n = n % 2
    print("%d nota(s) de R$ 1,00" % int(n))
