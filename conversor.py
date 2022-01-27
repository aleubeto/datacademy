menu = '\n💰Bienvenidx al conversor de monedas💰\n1.-Pesos colombianos\n2.-Pesos argentinos\n3.-Pesos mexicanos\n👉 '
opcion = int(input(menu))
pesos = float(input('\n¿Cuántos pesos tienes?\n👉 '))

if opcion == 1:
    dolar = 3930.00
    print(f'🤑Tienes ${round(pesos/dolar,2)}')

elif opcion == 2:
    dolar = 104.70
    print(f'🤑Tienes ${round(pesos/dolar,2)}')

elif opcion == 3:
    dolar = 20.81
    print(f'🤑Tienes ${round(pesos/dolar,2)}')

else:
    print('\n😔Por favor, ingresa una opción válida.')
