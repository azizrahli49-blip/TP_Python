import tkinter as tk
import math

class Calculatrice(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        '''
        Nous initialisons ici les différentes variables de la fenêtre calculatrice, et nous créons les boutons et labels 
        qui s'y trouverons, ainsi que d'autres paramètres tel que son emplacement sur l'écran et le nom de la fenêtre.
        '''
        self.nombre1=""
        self.nombre2=""
        self.symbole_operation=""
        self.resultat=""
        self.sous_methode=False
        self.historique=[]
        self.position_historique=0
        self.creation_label()
        self.creation_button_chiffre()
        self.creation_button_operation()
        self.creation_button_autres()
        self.eval('tk::PlaceWindow . center')
        self.title('Calculatrice')

    def creation_label(self):
        '''
        Les labels suivant sont :
            - le titre de la fenêtre,
            - l'affichage du calcul encours (self.calcul) qui pourra être modifié dans la suite du code, il est initialement vide,
            - l'affichage de l'historique (self.label_historique) qui sera également modifiable et initialisé vide, il est accompagné
              d'un label fixe avec la mention 'précédent'.
        '''
        tk.Label(self, text='CALCULATRICE', font=('BOLD', 14), height=2).grid(row=0, column=1, columnspan=5)
        self.calcul=tk.Label(self, text="", bg='white', font=1, width=22, height=2, relief='groove', borderwidth=4)
        self.calcul.grid(row=5, column=1, columnspan=5)
        tk.Label(self, text="Précédent : ").grid(row=1, column=1, columnspan=2)
        self.label_historique=tk.Label(self, text="", bg='white', font=1, width=22, relief='groove', borderwidth=4)
        self.label_historique.grid(row=2, column=1, columnspan=5)
        ''' Les labels suivant sont uniquement présents pour des raisons d'esthétismes de la fenêtre '''
        tk.Label(self,text="").grid(row=1, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=4, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=6, column=1, columnspan=5)
        tk.Label(self,text="").grid(row=12, column=1, columnspan=5)
        tk.Label(self,text="", height=1).grid(row=14, column=1, columnspan=5)
        tk.Label(self,text="", width=2).grid(row=0, column=0, rowspan=15)
        tk.Label(self,text="", width=2).grid(row=0, column=6, rowspan=15)

    def creation_button_chiffre(self):
        '''
        Cette méthode permet de créer tous les boutons de la calculatrice présentant des chiffres de 0 à 9 ainsi que les caractères '.'
        et 'pi'. L'activation de chacun d'entre eux appelle la méthode 'self.nombre' suivante, cependant, elle prend en paramètre le caractère
        correspondant c'est pourquoi la fonction lambda est utilisée ici.
        '''
        tk.Button(self, text='1', command=lambda : self.nombre('1'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=7, column=1)
        tk.Button(self, text='2', command=lambda :self.nombre('2'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=7, column=2)
        tk.Button(self, text='3', command=lambda :self.nombre('3'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=7, column=3)
        tk.Button(self, text='4', command=lambda :self.nombre('4'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=8, column=1)
        tk.Button(self, text='5', command=lambda :self.nombre('5'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=8, column=2)
        tk.Button(self, text='6', command=lambda :self.nombre('6'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=8, column=3)
        tk.Button(self, text='7', command=lambda :self.nombre('7'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=9, column=1)
        tk.Button(self, text='8', command=lambda :self.nombre('8'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=9, column=2)
        tk.Button(self, text='9', command=lambda :self.nombre('9'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=9, column=3)
        tk.Button(self, text='0', command=lambda :self.nombre('0'), bg='tomato', fg='white', font=2, width=2, height=1,borderwidth=5, relief='groove').grid(row=10, column=1)
        tk.Button(self, text='.', command=lambda :self.nombre('.'), bg='darksalmon', fg='white', font=2, width=6, height=1,borderwidth=5, relief='groove').grid(row=10, column=2, columnspan=2)
        tk.Button(self, text='𝝅', command=lambda : self.nombre('pi'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=10, column=5)

    def nombre(self, chiffre):
        '''
        Cette méthode permet de compléter les deux variables 'self.nombre1' et 'self.nombre2' rentrées par l'utilisateur en actionnant les
        boutons souhaités. Elle prend donc en paramètre le chiffre (ou caractère '.' et 'pi') en entrée, et l'ajoute au nombre1 si l'utilisateur
        n'a pas encore sélectionné d'opération (+,-...), sinon au nombre2. Nous noterons que si il entre le paramètre 'pi' alors le nombre entier
        est remplacé. De plus, si une sous méthode (cos, sin...) a été appliquée alors il n'est pas possible de modifier le nombre.
        La première boucle 'if' permet de réinitialiser le calcul précédent, grâce à la fonction self.supprimer.
        Entrée : variable string correspondant au chiffre ou au caractère (pi ou virgule) à ajouter
        Sortie : modification du nombre1 ou du nombre2 (toutes deux des variables str), affichage sur le label self.calcul
        '''
        if self.resultat!="" :
            self.supprimer()
        if self.sous_methode==False:
            if chiffre=='pi' :
                if self.symbole_operation=="" :
                    self.nombre1='𝝅'
                else :
                    self.nombre2='𝝅'
            elif chiffre=='.' and self.symbole_operation=="" and self.nombre1=="":
                self.nombre1='0.'
            elif chiffre=='.' and self.symbole_operation!="" and self.nombre2=="":
                self.nombre2='0.'
            elif self.symbole_operation=="" :
                self.nombre1=self.nombre1+chiffre
            elif self.symbole_operation!="" :
                self.nombre2=self.nombre2+chiffre
            self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2, width=0)

    def creation_button_operation(self):
        '''
        Cette méthode permet de créer les différents boutons :
            - des opérations (addition, soustraction, multiplication et division) qui font ensuite appellent à la méthode self.operation,
              de la même manière que pour les boutons des chiffres,
            - des sous-opérations (cosinus, sinus, racine carrée, tangente et carré) qui font appellent à la méthode self.sous_operation,
            - d'entrée pour effectuer le calcul qui appelle directement la fonction self.calculer.
        '''
        tk.Button(self, text='+', command=lambda : self.operation('+'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=7, column=4)
        tk.Button(self, text='-', command=lambda : self.operation('-'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=8, column=4)
        tk.Button(self, text='*', command=lambda : self.operation('*'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=9, column=4)
        tk.Button(self, text='/', command=lambda : self.operation('/'), bg='forestgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=10, column=4)
        tk.Button(self, text='√x', command=lambda: self.sous_operation('√'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=11, column=4)
        tk.Button(self, text='cos', command=lambda : self.sous_operation('cos'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=7, column=5)
        tk.Button(self, text='sin', command=lambda : self.sous_operation('sin'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=8, column=5)
        tk.Button(self, text='tan', command=lambda: self.sous_operation('tan'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=9, column=5)
        tk.Button(self, text="x²", command= lambda: self.sous_operation('²'), bg='darkgreen', fg='white', font=2, width=3, height=1,borderwidth=5, relief='groove').grid(row=11, column=5)
        tk.Button(self, text='Entrer', command= self.calculer, bg='darkred', fg='white', font=2, width=11, height=1,borderwidth=5, relief='groove').grid(row=11, column=1, columnspan=3)

    def operation(self, symbole):
        '''
        Cette méthode permet d'attribuer l'opération voulue à la variable self.symbole_operation. Elle prend en compte que :
            - si le nombre1 est vide, elle lui attribue le résultat du calcul précédent sinon la valeur '0',
            - si l'opération venant d'être traitée n'a pas été supprimée, elle actionne la méthode self.supprimer,
            - elle réinitialise la variable booléenne self.sous_methode de manière à pouvant entrer le nombre2 ensuite,
            - elle affiche le symbole entré sur le label self.calcul.
        Entrée : variable string correspondant au symbole.
        Sortie : enregistrement du symbole dans la variable correspondante et mise à jour du label et de self.sous_methode.
        '''
        if self.resultat!="" :
            self.supprimer()
        if self.nombre1=="" :
            self.supprimer()
            if self.historique!=[] :
                self.nombre1=self.historique[len(self.historique)-1][4]
            else :
                self.nombre1='0'
        self.symbole_operation=symbole
        self.sous_methode = False
        self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2, width=0)

    def sous_operation(self,sous_op):
        '''
        Cette méthode permet d'entrer des sous-méthodes (cos, sin...), ce qui n'est possible que si la variable nombre a été remplie
        au préalable et s'il n'y a pas déja une autre sous-méthode (il n'est pas possible de faire le cosinus d'un sinus par exemple), ce qui
        signifie qu'au moment où une sous-méthode a été sélectionnée, le nombre n'est plus modifiable.
        Entrée : sous opération en format string
        Sortie : modification du nombre1 ou du nombre2 (toutes deux des variables str), affichage sur le label self.calcul
        '''
        if self.resultat!="" :
            self.supprimer()
        if self.nombre1=="" :
            if self.historique!=[] :
                self.nombre1=self.historique[len(self.historique)-1][4]
            else:
                self.nombre1="0"
        if self.sous_methode==False :
            if sous_op=='²' :
                if self.symbole_operation=="" :
                    self.nombre1=self.nombre1+sous_op
                    self.sous_methode=True
                elif self.nombre2!="":
                    self.nombre2=self.nombre2+sous_op
                    self.sous_methode=True
            elif sous_op=='cos' or sous_op=='sin' or sous_op=='tan' or sous_op=='√' :
                if self.symbole_operation=="" :
                    self.nombre1=sous_op+'('+self.nombre1+')'
                    self.sous_methode=True
                elif self.nombre2!="":
                    self.nombre2=sous_op+'('+self.nombre2+')'
                    self.sous_methode=True
            self.calcul.config(text=self.nombre1+self.symbole_operation+self.nombre2, width=0)

    def calculer(self):
        '''
        Dans cette première partie, la méthode traite le caractère 'pi' en le remplaçant par sa valeur et s'occupe d'effectuer
        toutes les sous-méthodes présentes dans les nombre1 et nombre2. Nous noterons que nous utilisons deux variables de méthodes
        n1 et n2 (pas directement nombre1 et nombre2) afin de garder un affichage plus clair et sans des nombres trop longs.
        Entrée : rien --> s'actionne lorsque l'utilisateur appuie sur ENTER.
        Sortie : des variables string où les sous-méthodes sont remplacées par leur 'vraie' opération.
        '''
        n1=self.nombre1
        n2=self.nombre2
        if '𝝅' in n1 :
            n1=n1.replace('𝝅',str(math.pi) )
        if '𝝅' in n2 :
            n2= n2.replace('𝝅', str(math.pi))
        if '²' in n1 :
            n1=str(float(n1[:len(n1)-1])**2)
        if '²' in n2 :
            n2=str(float(n2[:len(n2)-1])**2)
        if 'tan' in n1 :
            n1=str(math.tan(float(n1[4:len(n1)-1])))
        if 'tan' in n2 :
            n2=str(math.tan(float(n2[4:len(n2)-1])))
        if 'cos' in n1 :
            n1=str(math.cos(float(n1[4:len(n1)-1])))
        if 'cos' in n2 :
            n2=str(math.cos(float(n2[4:len(n2)-1])))
        if 'sin' in n1 :
            n1=str(math.sin(float(n1[4:len(n1)-1])))
        if 'sin' in n2 :
            n2=str(math.sin(float(n2[4:len(n2)-1])))
        if '√' in n1 :
            n1=str(math.sqrt(float(n1[2:len(n1)-1])))
        if '√' in n2 :
            n2=str(math.sqrt(float(n2[2:len(n2)-1])))
        '''
        Cette deuxième partie de la méthode permet d'effectuer les opérations (addition, soustraction...) entre les deux nombres.
        Nous remarquerons qu'elle prend en compte que :
            - si l'utilisateur veut diviser par 0, le calcul s'arrête, 
            - si il n'y a pas de nombre1 (et donc pas de symbole d'opération, cf méthode self.operation) alors rien n'est rentré,
            - si le nombre1 est entré mais pas le deuxième, alors il ne traite que le premier et retire le symbole d'opération s'il
              avait été renseigné
            - modifie le label calcul dans chacun des cas et enregistre dans l'historique s'il y a un résultat.   
        Entrée : rien --> s'actionne lorsque l'utilisateur appuie sur ENTER.
        Sortie : le résultat qui est ensuite affiché et enregistré dans l'historique (sous format str).      
        '''
        if self.nombre1=="":
            self.calcul.config(text="", width=22)
        elif self.nombre2=="" :
            self.resultat = float(n1)
            self.symbole_operation=""
            self.calcul.config(text=self.nombre1 + ' = ' + str(self.resultat), width=0)
            self.historique.append([self.nombre1, self.symbole_operation, self.nombre2,' = ', str(self.resultat)])
        else :
            if self.symbole_operation=='+' :
                self.resultat=float(n1)+float(n2)
            elif self.symbole_operation=='-':
                self.resultat=float(n1)-float(n2)
            elif self.symbole_operation=='*':
                self.resultat=float(n1)*float(n2)
            elif self.symbole_operation=='/':
                if self.nombre2=='0':
                    self.label_historique.config(text='ERREUR : pas de division par 0', width=0)
                    self.nombre2=''
                    self.symbole_operation=''
                else :
                    self.resultat=float(n1)/float(n2)
            self.calcul.config(text=self.nombre1 + self.symbole_operation + self.nombre2 + ' = ' + str(self.resultat), width=0)
            self.historique.append([self.nombre1, self.symbole_operation, self.nombre2,' = ', str(self.resultat)])

    def creation_button_autres(self):
        '''
        Cette méthode permet d'afficher tous les autres boutons :
            - pour fermer la page avec self.destroy,
            - pour supprimer le calcul encours en appelant la fonction self.supprimer,
            - pour commander l'historique en le montant de haut en bas (avec la fonction self.fleche('sens')) et en relançant le
              calcul sur lequel l'utilisateur est stoppé grâce à la méthode self.relancer.
        '''
        tk.Button(self, text='Vider', command=self.supprimer, bg='dimgray', fg='white', font=2, width=11, borderwidth=2, relief='groove').grid(row=13, column=1, columnspan=3)
        tk.Button(self, text='Quitter', command=self.destroy, bg='dimgray', fg='white', font=2, width=8, borderwidth=2, relief='groove').grid(row=13, column=4, columnspan=2)
        tk.Button(self, text='↑', command=lambda:self.fleche('up'), bg='dimgray', fg='white', font=2, width=2, borderwidth=2, relief='groove').grid(row=3, column=1)
        tk.Button(self, text='↓', command=lambda: self.fleche('down'), bg='dimgray', fg='white', font=2, width=2, borderwidth=2, relief='groove').grid(row=3, column=2)
        tk.Button(self, text='Répéter', command=self.relancer, bg='dimgray', fg='white', font=2, width=12, borderwidth=2, relief='groove').grid(row=3, column=3, columnspan=3)

    def supprimer(self):
        '''
        Cette méthode permet de réinitialiser le calcul en enregistrant le calcul encours (s'il a été lancer via la méthode
        self.calculer) et en remettant à vide ou à 0 ou à False les autres variables de manière à pouvoir lancer un nouveau calcul.
        De plus, il repositionne l'historique au dernier calcul effectué.
        '''
        self.position_historique = 0
        chaine=""
        for element in self.historique[len(self.historique) - 1 ]:
            chaine += element
        self.label_historique.config(text=chaine, width=0)
        self.nombre1=""
        self.nombre2=""
        self.symbole_operation=""
        self.resultat=""
        self.calcul.config(text="", width=22)
        self.sous_methode=False

    def fleche(self, sens):
        '''
        Cette méthode permet de parcourir l'historique de haut (calcul précédent) en bas (vers calcul le plus récent) et
        d'afficher l'historique correspondant à la position du curseur dans la liste contenant tous les calculs.
        Entrée : variable str pour renseigner le sens du mouvement dans l'historique.
        Sortie : modification du label historique.
        '''
        chaine=""
        if sens=='up' :
            self.position_historique += 1
            for element in self.historique[len(self.historique)-2-self.position_historique] :
                chaine+=element
            self.label_historique.config(text=chaine, width=0)
        else :
            self.position_historique -= 1
            for element in self.historique[len(self.historique)-2-self.position_historique] :
                chaine+=element
            self.label_historique.config(text=chaine, width=0)

    def relancer(self):
        '''
        Cette méthode permet à l'utilisateur de renouveller un ancien calcul de l'historique s'il le souhaite.
        '''
        self.nombre1=self.historique[len(self.historique)-2-self.position_historique][0]
        self.nombre2=self.historique[len(self.historique)-2-self.position_historique][2]
        self.symbole_operation=self.historique[len(self.historique)-2-self.position_historique][1]
        self.calculer()

def main():
    f=Calculatrice()
    f.mainloop()

main()