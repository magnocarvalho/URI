# -*- coding: utf-8 -*-,
# 1035 - Teste de Seleção 1
a, b, c, d = map(int, input().split())
if((b > c) and (d > a) and ((c + d) > (a + b)) and (a > 0) and (b > 0) and (c > 0) and (d > 0) and (a % 2 == 0) ):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")