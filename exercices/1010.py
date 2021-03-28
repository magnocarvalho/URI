# -*- coding: utf-8 -*-
# Cálculo Simples

codigo_p1, qtd_p1, vlr_p1 = map(float, input().split())

codigo_p2, qtd_p2, vlr_p2 = map(float, input().split())

f = (qtd_p1* vlr_p1) + (qtd_p2 * vlr_p2)
print("VALOR A PAGAR: R$ %.2f" % f)