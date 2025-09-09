import os
import sqlite3
import pandas as pd

def creer_tables():
    """Créer les tables si elles n'existent pas"""
    connexion = None  # S'assurer que la connexion est définie
    try:
        # Connexion à la BDD (création si elle n'existe pas)
        connexion = sqlite3.connect("alesc.sqlite")
        curseur = connexion.cursor()

        # Script de création de la table logeur
        requete_logeur = '''CREATE TABLE IF NOT EXISTS logeur (
               id_logeur INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nom TEXT NOT NULL,
               prenom TEXT NOT NULL,
               numero_rue TEXT,
               nom_rue TEXT,
               code_postal TEXT,
               ville TEXT)'''

        curseur.execute(requete_logeur)  # Exécution de la requête

        requete_logement = '''CREATE TABLE IF NOT EXISTS logement (
                id_logement INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                numero_rue TEXT,
                nom_rue TEXT,
                code_postal TEXT,
                ville TEXT,
                label TEXT NOT NULL,
                nom_logeur TEXT NOT NULL,
                prenom_logeur TEXT NOT NULL,
                type_logement TEXT NOT NULL,
                id_logeur INTEGER,
                FOREIGN KEY (id_logeur) REFERENCES logeur(id_logeur))'''

        curseur.execute(requete_logement)

        requete_etudiant = '''CREATE TABLE IF NOT EXISTS etudiant (
               id_etudiant INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nom TEXT NOT NULL,
               prenom TEXT NOT NULL,
               semestre TEXT,
               id_logement INTEGER,
               FOREIGN KEY (id_logement) REFERENCES logement(id_logement))'''

        curseur.execute(requete_etudiant)

        connexion.commit()
        print("Tables créées avec succès !")

    except sqlite3.Error as e:
        print(f"Une erreur est survenue: {e}")
    finally:
       curseur.close()
       connexion.close()

def peupler_tables():
    '''Remplissage des tables créer avec la focntion précédente'''
    connexion = None  # S'assurer que la connexion est définie
    try:
        datalogeur = pd.read_excel("logeurs.xlsx")
        datalogement = pd.read_excel("logements.xlsx")
        dataetudiant = pd.read_excel("etudiants.xlsx")
        connexion = sqlite3.connect("alesc.sqlite")
        curseur = connexion.cursor()

        # Insérer les données dans le tableau du logeur
        for index, row in datalogeur.iterrows():
            requete_logeur = '''INSERT INTO logeur (nom, prenom, numero_rue, nom_rue, code_postal, ville) 
                                VALUES (?, ?, ?, ?, ?, ?)'''
            values_logeur = (
                row['nom'], row['prenom'], row['numero_rue'], row['nom_rue'], row['code_postal'], row['ville'])
            curseur.execute(requete_logeur, values_logeur)

        # Insérer les données dans le tableau des logements
        for index, row in datalogement.iterrows():
            requete_logement = '''INSERT INTO logement (numero_rue, nom_rue, code_postal, ville, label, 
                                nom_logeur, prenom_logeur, type_logement, id_logeur) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 
                                (SELECT id_logeur FROM logeur WHERE nom = ? AND prenom = ?))'''
            values_logement = (
                row['numero_rue'], row['nom_rue'], row['code_postal'], row['ville'], row['label'], row['nom_logeur'],
                row['prenom_logeur'], row['type_logement'], row['nom_logeur'], row['prenom_logeur'])
            curseur.execute(requete_logement, values_logement)

        # Insérer les données dans le tableau des étudiants
        for index, row in dataetudiant.iterrows():
            requete_etudiant = '''INSERT INTO etudiant (nom, prenom, semestre, id_logement) 
                                VALUES (?, ?, ?, 
                                (SELECT id_logement FROM logement WHERE numero_rue = ? AND nom_rue = ? AND code_postal = ?))'''
            values_etudiant = (
                row['nom'], row['prenom'], row['semestre'], row['numero_rue'], row['nom_rue'], row['code_postal'])
            curseur.execute(requete_etudiant, values_etudiant)

        connexion.commit()
        print("Données insérées avec succès !")

    except sqlite3.Error as e:
        print(f"Une erreur est survenue: {e}")

    finally:
        curseur.close()
        connexion.close()


def afficher_logements_logeur():
    """Afficher tous les logements d'un logeur après avoir demandé le nom et prénom à l'utilisateur"""
    connexion = None  # Ensure connexion is defined
    try:
        # Demander le nom et le prénom du logeur
        nom_logeur = input("Entrez le nom du logeur : ").lower().strip()
        prenom_logeur = input("Entrez le prénom du logeur : ").lower().strip()

        # Connexion à la BDD
        connexion = sqlite3.connect("alesc.sqlite")
        curseur = connexion.cursor()

        # Requête pour récupérer les logements du logeur
        requete_logements = '''SELECT l.numero_rue, l.nom_rue, l.code_postal, l.ville, l.label, l.type_logement, l.id_logement
                               FROM logement l
                               JOIN logeur lo ON l.id_logeur = lo.id_logeur
                               WHERE lo.nom = ? AND lo.prenom = ?'''
        curseur.execute(requete_logements, (nom_logeur, prenom_logeur))
        logements = curseur.fetchall()

        if logements:
            print(f"Logements du logeur {prenom_logeur} {nom_logeur} :")
            i=1
            for logement in logements:
                #affichage du logement :
                print(f"Logement {i} : {logement[0]} rue {logement[1]} {logement[2]} {logement[3]} {'*'*int(logement[4])} {logement[5]}")
                #recherche des étudiants dans ce logement :
                requete_etudiants = '''SELECT e.nom, e.prenom
                                      FROM etudiant e 
                                      JOIN logement l ON l.id_logement=e.id_logement
                                      WHERE l.id_logement = ? '''
                curseur.execute(requete_etudiants, (logement[6],))
                etudiants = curseur.fetchall()
                for etudiant in etudiants :
                    #affichage de l'étudiant dans le logement encours :
                    print(f"Nom de l'étudiant : {etudiant[0]} {etudiant[1]}")
                i+=1
        else:
            print(f"Aucun logement trouvé pour le logeur {prenom_logeur} {nom_logeur}")

    except sqlite3.Error as e:
        print(f"Une erreur est survenue: {e}")
    finally:
        curseur.close()
        connexion.close()

def main():
    if os.path.exists("alesc.sqlite") is not True:
        #Afin d'éviter de remplir et recréer le fichier à chaque ouverture
        creer_tables()
        peupler_tables()
    else :
        print("Les tables sont déjà existantes et remplies ! ")
    continuer = True
    while continuer :
        afficher_logements_logeur()
        continuer=(True if input("Continuer ? O/N : ").upper()=="O" else False)

main()