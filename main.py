def calcular_juros(valor, taxa, tempo):
    return valor * (1 + taxa/100) ** tempo

print("💬 Assistente Financeiro IA")
print("Digite 'sair' para encerrar\n")

while True:
    pergunta = input("Você: ").lower()

    if pergunta == "sair":
        print("Encerrando...")
        break

    elif "juros" in pergunta:
        try:
            valor = float(input("Valor inicial: "))
            taxa = float(input("Taxa (%): "))
            tempo = float(input("Tempo: "))
            resultado = calcular_juros(valor, taxa, tempo)
            print(f"Resultado: R$ {resultado:.2f}")
        except:
            print("Erro ao calcular.")

    elif "cartão" in pergunta:
        print("Assistente: O cartão de crédito permite compras com pagamento futuro.")

    elif "investimento" in pergunta:
        print("Assistente: Investimentos podem gerar rendimentos ao longo do tempo.")

    else:
        print("Assistente: Desculpe, não entendi. Pode reformular?")
