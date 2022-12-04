import PySimpleGUI as sg

def juros_simples(c, i, t): 
    resultado = (i / 100) * c * t
    montante = c + resultado
    return resultado

def montante(c, i, t): 
    resultado = (i / 100) * c * t
    montante = c + resultado
    return montante
       
def juros_compostos(c, i, t):
    compostos = c * (1 + i /100) ** 4
    return compostos

sg.theme("DarkGreen5")

layout = [
    [sg.Text("Digite o capital inicial:")],
    [sg.Input(key="c")],
    [sg.Text("Digite a taxa aplicada:")],
    [sg.Input(key="i")],
    [sg.Text("Digite o tempo:")],
    [sg.Input(key="t")],
    [sg.Button("Calcular"), sg.Button("Cancelar")],
    [sg.Text("", key="text_result")],
    [sg.Text("", key="text_montante")],
    [sg.Text("", key="text_composto")],
]

janela = sg.Window("Calculadora juros By Caio Roque", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Calcular":
        c = float(valores["c"])
        i = float(valores["i"])
        t = float(valores["t"])
        resultado = juros_simples(c, i, t)
        valor_montante = montante(c, i, t)
        valor_composto = juros_compostos(c, i, t)
        janela["text_result"].update(f"O valor dos juros simples é R${resultado:.2f}")
        janela["text_montante"].update(f"O montante é R${valor_montante:.2f}")
        janela["text_composto"].update(f"O valor dos juros compostos é R${valor_composto:.2f}")


janela.close()
