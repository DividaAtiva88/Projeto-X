import math
from datetime import date, time, datetime, timedelta


tributo = int(input("Tributo"))
certificadoDA = int(input("CDA"))
valorImposto = float(input("Valor do imposto"))
valorTaxa = float(input("Valor da taxa"))

reduz = valorImposto - valorTaxa
print(f"O valor do imposto real é de R${reduz}")
base = float(input("Ano base"))

venc01 = input()