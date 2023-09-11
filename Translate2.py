from tkinter import *
import googletrans
import textblob as Blob
from tkinter import messagebox

def translate(event=None):
    try: 
        # limpa a caixa de texto de saida
        text_translated.delete("1.0", END)
        # identifica o idioma de entrada
        for key, value in language.items():
            if value == language_selected.get():
                from_language = key
        # identifica o idioma de saida
        to_language = "pt" if from_language == "en" else "en"
        # traduz o texto
        words = Blob.TextBlob(text_to_translate.get("1.0", END))
        words = words.translate(from_lang=from_language, to=to_language)
        # exibe o texto traduzido
        text_translated.insert("1.0", words)

    except Exception as e:
        messagebox.showerror("Error", e)


def clear():
    text_to_translate.delete("1.0", END)
    text_translated.delete("1.0", END)

def open_help():
    help_text = "To choose the input language, select the desired option between 'Portuguese' and 'English'. \
The output language will be automatically defined based on the selected input language. \
Enter the text to be translated into the text box on the left side of the window and click the 'Translate' button or press Enter to start the translation. \
The translated text will be displayed in the text box on the right side of the window. To clean the text fields, click the 'Clear' button. \n\n" \
"Para escolher o idioma de entrada, selecione a opção desejada entre 'Portuguese' e 'English'. \
O idioma de saída será automaticamente definido com base no idioma de entrada selecionado. \
Digite o texto a ser traduzido na caixa de texto na lateral esquerda da janela e clique no botão 'Translate' ou pressione Enter para iniciar a tradução. \
O texto traduzido será exibido na caixa de texto na lateral direita da janela. Para limpar os campos de texto, clique no botão 'Clear'."
    messagebox.showinfo("Help", help_text)

language = {"pt": "Portuguese", "en": "English"}

app = Tk()
app.title("Translator")
app.iconbitmap('C:\\Users\\PC\\Documents\\pythonProject\\Tkinter\\Tranlate\\Images\\translate.ico')
app.geometry("880x300")
app.config(bg="#F6F6F6")


# Texto para traduzir
text_to_translate = Text(app, width=46, height=10, wrap=WORD)
text_to_translate.config(bg="#F6F6F6", fg="#0072C6")
text_to_translate.grid(row=0, column=0, padx=10, pady=20)

# atalho para traduzir 
text_to_translate.bind("<Return>", translate)

# Botao para traduzir
translate_button = Button(app, text="Translate", font=("Arial", 12), command=translate, bg="#0072C6", fg="white")
translate_button.grid(row=0, column=1, padx=10)

# texto traduzido
text_translated = Text(app, width=46, height=10, wrap=WORD)
text_translated.config(bg="#F6F6F6", fg="#0072C6")
text_translated.grid(row=0, column=2, padx=10, pady=20)

# Botao para limpar
clear_button = Button(app, text="Clear", font=("Arial", 12), command=clear, bg="#0072C6", fg="white")
clear_button.grid(row=1, column=1, padx=10)

# Botao de ajuda
help_button = Button(app, text="Help", font=("Arial", 12), command=open_help, bg="#0072C6", fg="white")
help_button.grid(row=2, column=1)

# Opções de idioma
language_selected = StringVar()
language_selected.set("Portuguese")

pt_rb = Radiobutton(app, text="Portuguese", font=("Arial", 10),variable=language_selected, value="Portuguese", fg="#0072C6")
pt_rb.grid(row=2, column=0)

en_rb = Radiobutton(app, text="English", font=("Arial", 10), variable=language_selected, value="English", fg="#0072C6")
en_rb.grid(row=2, column=2)

app.mainloop()
