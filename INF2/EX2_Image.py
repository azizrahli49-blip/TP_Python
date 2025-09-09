import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np

def convertir (image):
    '''
    Cette fonction permet de convertir une image RGB (paramètre d'entrée) en une nouvelle image HSV. Pour cela, le ndarray
    de l'imgae d'origine est copié puis modifié en fonction des valeurs de R,G et B de chaque pixel.
    Entrée : une image RGB en ndarray
    Sortie : une image HSV en ndarray
    '''
    conv=np.copy(image/255)
    for i in range(0,len(conv)):
        for j in range(0,len(conv[i])):
            a,b,c=conv[i][j]
            Cmin=min(a,b,c)
            Cmax=max(a,b,c)
            delta=Cmax-Cmin
            np.seterr(divide='ignore', invalid='ignore') #permet d'éviter l'affichage d'erreur lié au division par zéro pour resultH et resultS
            condH = [delta==0, Cmax==a, Cmax==b, Cmax==c]
            resultH = [0, (1/6)*(((b-c)/delta)%6), (1/6)*((c-a)/delta+2), (1/6)*((a-b)/delta+4)]
            condS = [Cmax == 0, Cmax !=0]
            resultS = [0, delta/Cmax]
            V=Cmax
            conv[i][j]=[np.select(condH, resultH),np.select(condS, resultS),V]
    return conv

def creer_masque (image):
    '''
    L'objectif de cette fonction est de créer un masque pour un élément spécifique dans une image. Ici, on cherche à obtenir
    la voiture. Pour cela, la fonction prend l'image HSV en entrée puis l'affiche selon les trois canaux H, S et V, ce qui nous
    permet d'estimer les intervalles de valeurs à conserver pour chacun d'eux. Ensuite le ndarray masque est créé à partir de
    la copie de l'image d'origine. Si les valeurs HSV rentrent dans les intervalles définis alors elles sont remplacées par
    TRUE, sinon par FALSE.
    Entrée : ndarray de l'image en HSV
    Sortie : ndarray du masque contenant les booléens True et False
    '''
    plt.imshow(image[:, :, 0], cmap='Reds_r')
    plt.title("Photographie avec le premier canal H")
    plt.colorbar()
    plt.show()
    plt.imshow(image[:, :, 1], cmap='Greens_r')
    plt.title("Photographie avec le deuxième canal S")
    plt.colorbar()
    plt.show()
    plt.imshow(image[:, :, 2], cmap='Blues_r')
    plt.title("Photographie avec le troisième canal V")
    plt.colorbar()
    plt.show()
    masque=np.copy(image)
    for i in range(0, len(masque)):
        for j in range(0, len(masque[i])):
            if 0.9>masque[i][j][0]>0.4 and masque[i][j][1] > 0.3 and masque[i][j][2]>0.45 :
                masque[i][j]=True
            else:
                masque[i][j] = False
    return masque

def modifier_teinte(image, masque):
    '''
    Cette fonction perd d'appliquer le masque sur une image afin de modifier la coleur de l'objet visé. Puisque le masque
    contient uniquement des valeurs booléennes, la coloration de la nouvelle image sont faites en RGB. La modification de
    la couleur est permise dès que la fonction rencontre un TRUE, cela change pixel par pixel la coloration de la voiture
    dans notre cas.
    Entrée : ndarray de l'image d'origine en RGB, et le masque composé de booléen
    Sortie : ndarray de la nouvelle image après application du masque en RGB
    '''
    teinte=np.copy(image)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            a,b,c=masque[i][j]
            A,B,C=image[i][j]
            if a==True :
                A=210
                C-=110
                B-=60
            teinte[i][j]=[A,B,C]
    return teinte


def main():
    img = plt.imread('citroen.jpg')
    conv=convertir(img)
    plt.imshow(conv)
    plt.title("Photographie en HSV")
    plt.show()
    plt.imshow(clr.hsv_to_rgb(conv))
    plt.title("Photographie en RGB (vérification)")
    plt.show()
    masq=creer_masque(conv)
    plt.imshow(masq)
    plt.title("Masque de la voiture")
    plt.show()
    new_img=modifier_teinte(img,masq)
    plt.imshow(new_img)
    plt.title("Photographie en RGB et avec la nouvelle coloration")
    plt.show()


main()
