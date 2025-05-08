def TaxaDeCambio(quantosReais, qualMoeda):
    match (qualMoeda):
        case "usd":
            return(quantosReais * 0.17)
        case "eur":
            return(quantosReais * 0.16)
        case "jpy":
            print(f"Seu dinheiro convertido para JPY(Iene Japonês): {quantosReais * 25} ")
            return 0

quantosReai = float(input("Quantia em reais: "))
qualMoed = input("Converter para (USD, EUR ou JPY): ").lower()
TaxaDeCambio(quantosReai, qualMoed)