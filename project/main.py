print("🌡️ Conversor de Temperatura")
print("=" * 30)
print("Escolha o tipo de conversão:")
print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

opcao = input("Digite sua opção (1 ou 2): ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")

elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C")

else:
    print("❌ Opção inválida. Tente novamente.")
