#Pide una frase y responda cuántas veces está la letra que hayas elegido

def actividad2():
    frase = input('Dime una frase: ')
    letra = input('Dime la letra que quieres contar: ')
    print(f"La frase tiene {frase.count(letra)}")
#actividad2()

def archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\PycharmProjects\\actividad15\\indicator.csv")
    df = datos[["Resumen de datos", "Código comarca"]]

    # Grafico circular
    df.Resumen de datos.value_counts().plot.pie()
    plt.show()
archivo()
