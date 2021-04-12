# -*- coding: utf-8 -*-
# 1038 Lanche
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

count, quantidade = map(int, input().split())
valor = 0
if(count == 1):
    valor = quantidade * 4
elif(count == 2):
    valor = quantidade * 4.50
elif(count == 3):
    valor = quantidade * 5
elif(count == 4):
    valor = quantidade * 2
elif(count == 5):
    valor = quantidade * 1.5

print("Total: R$ %.2f" % valor)
