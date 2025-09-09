def nb_min(password):
    '''
    Fonction qui compte le nombre de lettre minuscule dans un mot de passe
    entrée : mot de passe --> chaine de caractères
    sortie : nombre de lettres minuscules --> entier
    >> nb_min("dejCHkjs76") retourne 6
    >> nb_min("HDéjd6-ZZ*") retourne 3
    '''
    return sum(c.islower() for c in password)

def nb_maj(password):
    '''
    Fonction qui compte le nombre de lettre majuscule dans un mot de passe
    entrée : mot de passe --> chaine de caractères
    sortie : nombre de lettres majuscules --> entier
    >> nb_maj("dejCHkjs76") retourne 2
    >> nb_maj("HDéjd6-ZZ*") retourne 4
    '''
    return sum(c.isupper() for c in password)

def nb_non_alpha(password):
    '''
    Fonction qui compte le nombre de caractères non inclus dans l'alphabet
    entrée : mot de passe --> chaine de caractères
    sortie : nombre de caractère --> entier
    >> nb_maj("dejCHkjs76") retourne 2
    >> nb_maj("HDéjd6-ZZ*") retourne 3
    '''
    return sum(not c.isalpha() for c in password)

def long_min(password):
    '''
    Fonction qui compte le nombre de minuscules successives et retourne le maximum
    entrée : mot de passe --> chaine de caractères
    sortie : maximum de lettres minuscules successives --> entier
    >> nb_maj("HDeygHed65/ejshdI") retourne 5
    >> nb_maj("*szsHSZZSsèD1") retourne 3
    '''
    longueur=0
    l=[]
    for cara in password:
        if cara.islower() :
            longueur+=1
        else :
            l.append(longueur)
            longueur=0
    l.append(longueur)
    return max(l)

def long_maj(password):
    '''
    Fonction qui compte le nombre de majuscules successives et retourne le maximum
    entrée : mot de passe --> chaine de caractères
    sortie : maximum de lettres majuscules successives --> entier
    >> nb_maj("HDeygHed65/ejshdI") retourne 2
    >> nb_maj("*szsHSZZSsèD1") retourne 5
    '''
    longueur = 0
    l = []
    for cara in password:
        if cara.isupper():
            longueur += 1
        else:
            l.append(longueur)
            longueur = 0
    l.append(longueur)
    return max(l)

def score(password):
    '''
    Fonction qui mesure la force/complexité d'un mot de passe sous la forme d'un score
    entrée : mot de passe --> chaine de caractères
    sortie : différence entre les bonus et pénalités --> entier
    >> score("JShdeuKJJ8767è") retourne 104
    >> score("jdUS") retourne 16
    '''
    l=len(password)
    bonus=l*4+(l-nb_maj(password))*2+(l-nb_min(password))*3+nb_non_alpha(password)*5
    penalites=long_min(password)*2+long_maj(password)*3
    return bonus-penalites
def main():
    '''
    Fonction principale qui demande le mot de passe à l'utilisateur et qui, en faisant appel aux autres fonctions, l'informe de la complexité de ce dernier
    entrée : demande un mot de passe par le biai d'un input --> chaine de caractères
    sortie : 'Très faible', 'Faible, 'Fort' ou 'Très fort' --> cahine de caractères
    >> score("JShdeuKJJ8767è") retourne 'Très fort'
    >> score("jdUS") retourne 'Très faible'
    '''
    mdp=input("Votre mot de passe : ").replace(" ","")     # la fonction replace permet d'éliminer les espaces
    print(f"Pour le mot de passe '{mdp}', le niveau de sécurité est :", end=" ")
    if score(mdp)<20:
        print("Très faible")
    elif score(mdp)<40:
        print("Faible")
    elif score(mdp)<80:
        print("Fort")
    else :
        print("Très fort")

main()
