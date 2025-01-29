# Classe de base
class Personne:
    def _init_(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Classe dérivée : Etudiant
class Etudiant(Personne):
    def _init_(self, nom, prenom, filiere):
        super()._init_(nom, prenom)
        self.filiere = filiere

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis étudiant en {self.filiere}."

# Classe dérivée : Enseignant
class Enseignant(Personne):
    def _init_(self, nom, prenom, matiere):
        super()._init_(nom, prenom)
        self.matiere = matiere

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis enseignant en {self.matiere}."

# Création des objets
personne = Personne("Dupont", "Jean")
etudiant = Etudiant("Martin", "Alice", "Informatique")
enseignant = Enseignant("Bernard", "Paul", "Mathématiques")

# Affichage des présentations
print(personne.se_presenter())
print(etudiant.se_presenter())
print(enseignant.se_presenter())# Classe de base
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Classe dérivée : Etudiant
class Etudiant(Personne):
    def __init__(self, nom, prenom, filiere):
        super()._init_(nom, prenom)
        self.filiere = filiere

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis étudiant en {self.filiere}."

# Classe dérivée : Enseignant
class Enseignant(Personne):
    def __init__(self, nom, prenom, matiere):
        super()._init_(nom, prenom)
        self.matiere = matiere

    def se_presenter(self):
        base_presentation = super().se_presenter()
        return f"{base_presentation} Je suis enseignant en {self.matiere}."

# Création des objets
personne = Personne("Dupont", "Jean")
etudiant = Etudiant("Martin", "Alice", "Informatique")
enseignant = Enseignant("Bernard", "Paul", "Mathématiques")

# Affichage des présentations
print(personne.se_presenter())
print(etudiant.se_presenter())
print(enseignant.se_presenter())