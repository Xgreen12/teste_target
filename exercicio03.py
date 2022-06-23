"""
 Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
 a) Usar o json ou xml disponivel como fonte dos dados do faturamento mensal;

 b) Podem exitir dias sem faturamento, comom nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo
   da média;
"""

import json

with open("dados.json", encoding='utf-8') as dados_json:
     dados = json.load(dados_json)

print(dados)



 #  O menor valor de faturamento ocorrido em um dia do mês;
menor = dados[0]["valor"]
dia = dados[0]["dia"]

for i in dados:
    if i["valor"] != 0.0 and i["valor"] < menor:
        menor = i["valor"]
        dia = i["dia"]

print("Menor dia: " + str(dia) + " valor: " + str(menor))


# O maior valor de faturamento ocorrido em um dia do mês;

maior = dados[0]["valor"]
dia = dados[0]["dia"]

for i in dados:
    if i["valor"] != 0.0 and i["valor"] > maior:
        maior = i["valor"]
        dia = i["dia"]

print("Maior dia: " + str(dia) + " valor: " + str(maior))



# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

soma = 0.0
count = 0.0
for i in dados:
    if i["valor"] != 0.0:
        soma += i["valor"]
        count += 1

media = soma / count

print("Média mensal foi: " + str(media))

for i in dados:
    if i["valor"] > media:
        print("Dia " + str(i["dia"]) + ", valor: " + str(i["valor"]))

