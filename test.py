class Personne:
    def __init__(self, nom, prenom, CIN, anneeNaiss):
        self.nom = nom
        self.prenom = prenom
        self.CIN = CIN
        self.anneeNaiss = anneeNaiss

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}."

    def age(self):
        calAg = int(2025 - int(self.anneeNaiss))
        return f"j'ai {calAg}"

# Classe dérivée : Etudiant
class Etudiant(Personne):
    def __init__(self, nom, prenom, filiere, CIN, anneeNaiss, note1, note2):
        super().__init__(nom, prenom, CIN, anneeNaiss)
        self.filiere = filiere
        self.note1 = note1
        self.note2 = note2

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis étudiant en {self.filiere}."

    def age(self):
        calAg = int(2025 - int(self.anneeNaiss))
        return f"j'ai {calAg}"

    def moyenne(self):
        moy = float((self.note1 + self.note2) /2)
        return f"j'ai une moyenne de {moy}"

# Classe dérivée : Employer
class Employer(Personne):
    def __init__(self, nom, prenom, matiere,CIN, anneeNaiss, prixHeure, nbreHeure):
        super().__init__(nom, prenom,CIN, anneeNaiss)
        self.matiere = matiere
        self.prixHeure = prixHeure
        self.nbreHeure = nbreHeure

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis enseignant en {self.matiere}."

    def age(self):
        calAg = int(2025 - int(self.anneeNaiss))
        return f"j'ai {calAg}"

    def salaire(self):
        sal = int(self.prixHeure * self.nbreHeure)
        return f"j'ai un salaire de {sal}"

# Création des objets
personne = Personne("wadja", "norbert", "carte", 2006)
etudiant = Etudiant("Martin", "Alice", "Informatique","carte d'identité",2005,15,12)
employer = Employer("Bernard", "Paul", "Mathématiques","carte d'identité",2007,1500,5)

# Affichage des présentations
print(personne.se_presenter())
print(personne.age())
print(etudiant.se_presenter())
print(etudiant.age())
print(etudiant.moyenne())
print(employer.se_presenter())
print(employer.age())
print(employer.salaire())






# import tkinter as tk
# from tkinter import ttk
#
# # Classe de base
# class Personne:
#     def __init__(self, nom, prenom, CIN, anneeNaiss):
#         self.nom = nom
#         self.prenom = prenom
#         self.CIN = CIN
#         self.anneeNaiss = anneeNaiss
#
#     def se_presenter(self):
#         return f"Je suis {self.prenom} {self.nom}."
#
#     def age(self):
#         return f"J'ai {2025 - self.anneeNaiss} ans."
#
# # Classe dérivée : Etudiant
# class Etudiant(Personne):
#     def __init__(self, nom, prenom, filiere, CIN, anneeNaiss, note1, note2):
#         super().__init__(nom, prenom, CIN, anneeNaiss)
#         self.filiere = filiere
#         self.note1 = note1
#         self.note2 = note2
#
#     def se_presenter(self):
#         return f"{super().se_presenter()} Je suis étudiant en {self.filiere}."
#
#     def moyenne(self):
#         return f"J'ai une moyenne de {(self.note1 + self.note2) / 2}."
#
# # Classe dérivée : Employer
# class Employer(Personne):
#     def __init__(self, nom, prenom, matiere, CIN, anneeNaiss, prixHeure, nbreHeure):
#         super().__init__(nom, prenom, CIN, anneeNaiss)
#         self.matiere = matiere
#         self.prixHeure = prixHeure
#         self.nbreHeure = nbreHeure
#
#     def se_presenter(self):
#         return f"{super().se_presenter()} Je suis enseignant en {self.matiere}."
#
#     def salaire(self):
#         return f"J'ai un salaire de {self.prixHeure * self.nbreHeure}."
#
# # Création des objets
# personne = Personne("GALE", "George", "CIN12345", 2006)
# etudiant = Etudiant("Martin", "Alice", "Informatique", "CIN67890", 2005, 15, 12)
# employer = Employer("Bernard", "Paul", "Mathématiques", "CIN54321", 2007, 1500, 5)
#
# # Création de l'interface Tkinter
# root = tk.Tk()
# root.title("Informations des Personnes")
# root.geometry("400x250")
#
# frame = ttk.Frame(root, padding=10)
# frame.pack(fill="both", expand=True)
#
# info_label = ttk.Label(frame, text="Sélectionnez une personne", font=("Arial", 12))
# info_label.pack(pady=10)
#
# text_display = tk.Text(frame, height=5, width=50)
# text_display.pack()
#
# def afficher_infos(objet):
#     info = f"{objet.se_presenter()}\n{objet.age()}"
#     if isinstance(objet, Etudiant):
#         info += f"\n{objet.moyenne()}"
#     elif isinstance(objet, Employer):
#         info += f"\n{objet.salaire()}"
#     text_display.delete("1.0", tk.END)
#     text_display.insert(tk.END, info)
#
# btn_frame = ttk.Frame(frame)
# btn_frame.pack(pady=10)
#
# btn_personne = ttk.Button(btn_frame, text="Afficher Personne", command=lambda: afficher_infos(personne))
# btn_personne.grid(row=0, column=0, padx=5)
#
# btn_etudiant = ttk.Button(btn_frame, text="Afficher Etudiant", command=lambda: afficher_infos(etudiant))
# btn_etudiant.grid(row=0, column=1, padx=5)
#
# btn_employer = ttk.Button(btn_frame, text="Afficher Employer", command=lambda: afficher_infos(employer))
# btn_employer.grid(row=0, column=2, padx=5)
#
# root.mainloop()