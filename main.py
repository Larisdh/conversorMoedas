#janela => 500 x 500
#janela
#titulo
#campos para selecionar as moedas de origem e destino #botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela= customtkinter.CTk()
janela.geometry("500x500")

#criar os botões, textos e demais elementos
titulo= customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 28)) 
texto_moeda_origem= customtkinter.CTkLabel(janela, text="SELECIONE A MOEDA DE ORIGEM", font=("", 18))
texto_moeda_destino= customtkinter.CTkLabel(janela, text="SELECIONE A MOEDA DE DESTINO", font=("", 18))
campo_moeda_origem= customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], fg_color=("#F65AC2"))
campo_moeda_destino= customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], fg_color=("#F65AC2"))

def converter_moeda(): 
    print("Converter moeda")

botao_converter= customtkinter.CTkButton (janela, text= "Converter", command= converter_moeda, font=("", 16), hover_color="red")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis= ["USD: dólar americado", "EUR: euro", "BRL; real brasileiro", "BCT: Bitcoin"]
for moeda in moedas_disponiveis:
    texto_moeda= customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()


#colocar os elementos criados na tela
titulo.pack(padx= 10, pady= 10)
texto_moeda_origem.pack(padx= 10, pady= 0)
campo_moeda_origem.pack(padx= 10, pady= 0)
texto_moeda_destino.pack(padx= 10, pady= 0)
campo_moeda_destino.pack(padx= 10, pady= 10)
botao_converter.pack(padx= 10, pady= 10)
lista_moedas.pack(padx= 10, pady= 10)

#rodar a janela
janela.mainloop()