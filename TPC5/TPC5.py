import re 
import ply.lex as lex
import json
import datetime as datetime

def verificar_data():
    data = datetime.datetime.now().strftime("%Y-%m-%d")
    padrao = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    if  padrao.match(data):
        return data
    else:
        print("Data não aceite")

with open("stock.json", "r", encoding="utf-8") as f:
    stock = json.load(f)

print(f"{verificar_data()}. Stock carregado, Estado atualizado.")
print("Bom dia. Estou disponível para atender o seu pedido.")
budget = 0

def t_LISTAR():
    print("----------------------------------------------")
    print("COD    |  NOME      |  QUANTIDADE  |  PRECO ")
    print("----------------------------------------------")
    for item in stock["stock"]:
        print(f"{item['cod']:<6} | {item['nome']:<10} | {item['quant']:<12} | {item['preco']:<6.2f}")
        print("====================================")

def t_MOEDA(escrita):
    global budget
    dinheiro = escrita[6:].strip()
    verifica_saldo = re.compile(r"^(\d+[ec])*(,\s*\d+[c])*\.?$")
    if verifica_saldo.fullmatch(dinheiro):
        moedas = re.findall(r"\d+[ec]", dinheiro, flags = re.IGNORECASE)
        for m in moedas:
            if m.endswith("e"):
                budget += int(m[:-1])*100
            elif m.endswith("c"):
                budget += int(m[:-1])
        euro = budget//100
        centimo = budget % 100
        print(f"maq: Saldo = {int(euro)}e{int(centimo)}c")


def t_SELECIONAR(escrita):
    global budget
    segunda_palavra = escrita.split()[1]
    for produto in stock["stock"]:
        if produto["cod"] == segunda_palavra:
            if produto["quant"] >= 1:
                preco_real = produto["preco"]*100
                if preco_real <= budget:
                    print(f"Pode retirar o produto dispensado {produto["nome"]}")
                    budget = budget - preco_real
                    euro = budget//100
                    centimo = budget % 100
                    print(f"maq: Saldo = {int(euro)}e{int(centimo)}c")
                    produto["quant"] -= 1
                    break
                else:
                    print("Saldo insufuciente para satisfazer o seu pedido")
                    euro = budget//100
                    centimo = budget % 100
                    euro_pedido = preco_real//100
                    centimo_pedido = preco_real % 100
                    print(f"maq: Saldo = {int(euro)}e{int(centimo)}c, Pedido = {int(euro_pedido)}e{int(centimo_pedido)}c")
                    break
            else:
                print("Esse produto já não está disponível")
    else:
        print("O produto que procura não está disponível")

def t_SAIR():
    global budget
    budget_euros = budget//100
    budget_centimos = budget%100
    conta2e = conta1e = conta50 = conta20 = conta10 = conta5 = conta2 = conta1 = 0
    while budget_euros > 0:
        if budget_euros > 1:
            budget_euros = budget_euros -2
            conta2e +=1
        else:
            conta1e +=1
            budget_euros -=1
    while budget_centimos > 0:
        if budget_centimos >= 50:
            budget_centimos = budget_centimos - 50
            conta50 += 1
        elif budget_centimos >= 20:
            budget_centimos = budget_centimos - 20
            conta20 += 1
        elif budget_centimos >= 10:
            budget_centimos = budget_centimos - 10
            conta10 += 1
        elif budget_centimos >= 5:
            budget_centimos = budget_centimos - 5
            conta5 += 1
        elif budget_centimos >= 2:
            budget_centimos = budget_centimos - 2
            conta2 += 1
        elif budget_centimos >= 1:
            budget_centimos = budget_centimos - 1
            conta1 += 1

    partes = []
    if conta2e: partes.append(f"{conta2e}x 2e")
    if conta1e: partes.append(f"{conta1e}x 1e")
    if conta50: partes.append(f"{conta50}x 50c")
    if conta20: partes.append(f"{conta20}x 20c")
    if conta10: partes.append(f"{conta10}x 10c")
    if conta5:  partes.append(f"{conta5}x 5c")
    if conta2:  partes.append(f"{conta2}x 2c")
    if conta1:  partes.append(f"{conta1}x 1c")

    if partes:
        print("Pode retirar o troco: " + ", ".join(partes))
        print("Até à próxima")
    else:
        print("Sem troco a devolver.")
        print("Até à próxima")


while True:
    escrita = input(">>")
    if not escrita:                      
        t_SAIR()
        break
    primeira_palavra = escrita.split()[0]
    if primeira_palavra == "MOEDA":
        t_MOEDA(escrita)
    elif primeira_palavra == "LISTAR":
        t_LISTAR()
    elif primeira_palavra == "SELECIONAR":
         t_SELECIONAR(escrita)
    elif primeira_palavra == "SAIR":
        t_SAIR()
        with open('stock.json', 'w', encoding='utf-8') as f:
            json.dump(stock, f ,indent=4)
        break
    else:
        t_SAIR()
        with open('stock.json', 'w', encoding='utf-8') as f:
            json.dump(stock, f ,indent=4)
        break
