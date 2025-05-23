import tkinter as tk
from tkinter import scrolledtext
import base64

# Fonction pour encoder le texte en base64
def encode_to_base64(event=None):  # Permet de l'appeler avec un événement (comme la touche Entrée)
    text = input_text.get("1.0", tk.END).strip()
    if text:
        encoded_bytes = base64.b64encode(text.encode("utf-8"))
        encoded_str = encoded_bytes.decode("utf-8")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encoded_str)

# Fonction pour copier le texte sélectionné dans le presse-papiers
def copy_to_clipboard(text_widget):
    text = text_widget.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

# Fonction pour effacer les zones de texte
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Fonction pour copier le texte encodé dans le presse-papiers avec Ctrl + B
def copy_encoded_text(event=None):
    copy_to_clipboard(output_text)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Encodeur Base64")
root.geometry("600x500")
root.configure(bg="#E8F0FE")

# Frame pour l'entrée de texte
input_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RAISED)
input_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

input_label = tk.Label(input_frame, text="Texte à encoder:", bg="#ffffff", font=("Arial", 14, "bold"))
input_label.pack(pady=(10, 5))

input_text = scrolledtext.ScrolledText(input_frame, height=10, width=70, font=("Arial", 12), wrap=tk.WORD, bg="#F0F4FF")
input_text.pack(pady=10, padx=10)

# Frame pour les boutons
button_frame = tk.Frame(root, bg="#E8F0FE")
button_frame.pack(pady=10)

# Réorganisation des boutons pour la disposition d'origine
encode_button = tk.Button(button_frame, text="Encoder en Base64", command=encode_to_base64, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, bd=0)
encode_button.grid(row=0, column=0, padx=5)

copy_input_button = tk.Button(button_frame, text="Copier Texte à Encoder", command=lambda: copy_to_clipboard(input_text), font=("Arial", 12), bg="#2196F3", fg="white", padx=10, bd=0)
copy_input_button.grid(row=0, column=1, padx=5)

copy_output_button = tk.Button(button_frame, text="Copier Texte Encodé", command=lambda: copy_to_clipboard(output_text), font=("Arial", 12), bg="#2196F3", fg="white", padx=10, bd=0)
copy_output_button.grid(row=0, column=2, padx=5)

# Bouton "Effacer"
clear_button = tk.Button(button_frame, text="Effacer", command=clear_text, font=("Arial", 12, "bold"), bg="#FF5722", fg="white", padx=10, bd=0)
clear_button.grid(row=0, column=3, padx=5)

# Frame pour la sortie de texte
output_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RAISED)
output_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

output_label = tk.Label(output_frame, text="Texte encodé:", bg="#ffffff", font=("Arial", 14, "bold"))
output_label.pack(pady=(10, 5))

output_text = scrolledtext.ScrolledText(output_frame, height=10, width=70, font=("Arial", 12), wrap=tk.WORD, bg="#F0F4FF")
output_text.pack(pady=10, padx=10)

# Lier la touche Entrée à la fonction d'encodage
root.bind('<Return>', encode_to_base64)

# Lier Ctrl + B à la fonction de copie du texte encodé
root.bind('<Control-b>', copy_encoded_text)

# Lancer la boucle principale de l'application
root.mainloop()
