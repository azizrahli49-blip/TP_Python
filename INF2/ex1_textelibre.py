from math import pi

# Question 1 :
def ouverture(chemin):
    '''
    Ouverture du fichier poème, dont le chemin d'accès est renseigné en paramètre,  afin de copier son
    contenu qui sera alors retourné à l'utilisateur.
    L'ajout du paramètre encoding avec la fonction open permet de s'assurer que l'ensemble des caractères
    spéciaux soient copiés correctement dans la variable contenu.
    '''
    with open(chemin,encoding='utf-8') as f :
        contenu=f.read()
    return contenu


# Question 2 :
def separation(contenu):
    '''
    Suppression de la ponctuation d'une chaine de caractère (contenu), de manière à créer une
    liste où un élément correpond à un mot et qui est ensuite retournée.
    '''
    for element in contenu:
        if element in "?./,;:!'\n":
            contenu=contenu.replace(element, " ")
    '''
    Remplacement des espaces doubles ou triples par des simples de manière à les utiliser comme 
    sépérateur pour la fonction split qui suit.
    '''
    contenu=contenu.replace("   ", " ")
    contenu=contenu.replace("  ", " ")
    mots=[mot for mot in contenu.split(" ")]
    return mots


# Question 3 :
def suite_chiffres(mots):
    '''
    Création d'une chaine de caractère où chaque chiffre représente la longueur des
    chaines de caractères composant la liste mots,
    Le retourne correspond donc à un suite de chiffres.
    '''
    long_mots=""
    for element in mots :
        long_mots+=str(len(element))
    return long_mots
def comparaison(chiffre):
    '''
    Chacun de ces chiffres contenu dans la cahine de caratère en paramètre (chiffre) est ensuite
    comparé un à un à PI pour vérifier leur égalité.
    Résultat obtenu : Les digits obtenus correspondent complètement à pi
    Avec la suite de chiffres provenant du poème : 31415926535897932384626433832795102884197169399375110582109749445923100
    '''
    valeur_pi=str(pi).replace(".", "")
        # retrait de la virgule à pi de manière à obtenir une suite de chiffre qui pourront être comparé à celle que nous avons crée
    correct=[]
    for i in range (0, len(valeur_pi)) :
        if int(valeur_pi[i])!=int(chiffre[i]) :
            correct.append(False)
        else :
            correct.append(True)
    if False in correct :
        print("Les digits obtenus ne correspondent pas à pi")
    else :
        print("Les digits obtenus correspondent complètement à pi")


# Question 4 :
def ecriture(texte, chemin):
    '''
    Ecriture d'un texte (ici en STR) obtenu à partir du poème dans un fichier texte dont le chemin est connu (effacé à chaque nouvelle inscription)
    '''
    with open(chemin,'w') as file :
        file.write(texte)


def main():
    poeme=ouverture("poème.txt")    # ouverture du fichier contenant le poème
    liste_mots_poeme=separation(poeme)  # création d'une liste où chaque élément est un mot
    chiffre_poeme=suite_chiffres(liste_mots_poeme)  # chaque mot de la liste devient un chiffre, ils sont ajoutés pour former une suite de chiffres
    comparaison(chiffre_poeme)  # le chiffre obtenu est comparé avec pi
    ecriture(chiffre_poeme, "chiffre.txt") # inscription du chiffre obtenu dans un fichier texte

main()