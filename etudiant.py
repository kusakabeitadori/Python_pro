import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class Personne:
    def __init__(self, nom, cin, annee_naiss):
        self.nom = nom
        self.cin = cin
        self.annee_naiss = annee_naiss

class Etudiant(Personne):
    def __init__(self, nom, cin, annee_naiss, filiere, note1, note2):
        super().__init__(nom, cin, annee_naiss)
        self.filiere = filiere
        self.note1 = note1
        self.note2 = note2

    def moyenne(self):
        return (self.note1 + self.note2) / 2

def valider():
    nom = entry_nom.get()
    cin = entry_cin.get()
    annee_naiss = entry_annee.get()
    filiere = filiere_var.get()
    note1 = entry_note1.get()
    note2 = entry_note2.get()
    
    try:
        annee_naiss = int(annee_naiss)
        note1 = float(note1)
        note2 = float(note2)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")
        return
    
    age = datetime.now().year - annee_naiss
    etudiant = Etudiant(nom, cin, annee_naiss, filiere, note1, note2)
    moyenne = etudiant.moyenne()
    
    table.insert("", tk.END, values=(nom, cin, filiere, note1, note2, f"{moyenne:.2f}", age))

def annuler():
    entry_nom.delete(0, tk.END)
    entry_cin.delete(0, tk.END)
    entry_annee.delete(0, tk.END)
    entry_note1.delete(0, tk.END)
    entry_note2.delete(0, tk.END)
    filiere_var.set(options_filiere[0])

def rechercher():
    nom_recherche = entry_nom.get().strip().lower()
    for row in table.get_children():
        values = table.item(row, "values")
        if values and values[0].lower() == nom_recherche:
            for col in range(len(columns)):
                table.item(row, tags=("found",))
            messagebox.showinfo("Résultat de la recherche", f"Nom: {values[0]}\nCNI: {values[1]}\nFilière: {values[2]}\nNote 1: {values[3]}\nNote 2: {values[4]}\nMoyenne: {values[5]}\nÂge: {values[6]}")
            return
    messagebox.showwarning("Résultat de la recherche", "Aucun étudiant trouvé avec ce nom.")

# Création de la fenêtre
root = tk.Tk()
root.title("Formulaire Étudiant")
root.geometry("900x700")
root.configure(bg="#212121", padx=20, pady=20)
root.eval('tk::PlaceWindow . center')

# Styles
style = ttk.Style()
style.configure("Treeview", rowheight=30, font=("Arial", 12), background="#424242", foreground="white")
style.configure("Treeview.Heading", font=("Arial", 13, "bold"), background="#1565C0", foreground="white")
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
style.map("Treeview", background=[("selected", "#FFEB3B")])

# Widgets
frame = tk.Frame(root, bg="#333333", bd=3, relief="ridge")
frame.pack(pady=10, padx=10, fill=tk.X)

fields = ["Nom", "CNI", "Année de naissance", "Note 1", "Note 2"]
entries = []

for i, field in enumerate(fields):
    tk.Label(frame, text=field+":", font=("Arial", 12, "bold"), bg="#333333", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(frame, width=30, font=("Arial", 12), bg="#424242", fg="white", bd=2, relief="solid")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_nom, entry_cin, entry_annee, entry_note1, entry_note2 = entries

# Liste déroulante pour la filière
options_filiere = ["Informatique", "Mathématiques", "Physique", "Chimie", "Biologie"]
filiere_var = tk.StringVar()
filiere_var.set(options_filiere[0])

tk.Label(frame, text="Filière:", font=("Arial", 12, "bold"), bg="#333333", fg="white").grid(row=len(fields), column=0, padx=10, pady=5, sticky="w")
filiere_menu = ttk.Combobox(frame, textvariable=filiere_var, values=options_filiere, font=("Arial", 12), width=28, state="readonly", style="TCombobox")
filiere_menu.grid(row=len(fields), column=1, padx=10, pady=5)

btn_frame = tk.Frame(root, bg="#212121")
btn_frame.pack(pady=10)

btn_valider = tk.Button(btn_frame, text="Valider", command=valider, font=("Arial", 12, "bold"), width=15, bg="#388E3C", fg="white")
btn_valider.grid(row=0, column=0, padx=10)

btn_annuler = tk.Button(btn_frame, text="Annuler", command=annuler, font=("Arial", 12, "bold"), width=15, bg="#D32F2F", fg="white")
btn_annuler.grid(row=0, column=1, padx=10)

# Tableau pour afficher les informations
columns = ("Nom", "CNI", "Filière", "Note 1", "Note 2", "Moyenne", "Âge")
table_frame = tk.Frame(root, bd=2, relief="solid", bg="#424242")
table_frame.pack(pady=20, fill=tk.BOTH, expand=True)

table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120, anchor="center")

table.pack(pady=10, fill=tk.BOTH, expand=True)

# Bouton de recherche
btn_rechercher = tk.Button(root, text="Rechercher", command=rechercher, font=("Arial", 12, "bold"), width=15, bg="#1976D2", fg="white")
btn_rechercher.pack(pady=10)

# Lancement de l'interface
tk.mainloop()
