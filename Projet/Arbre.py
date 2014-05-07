from Sommet import *
import projet
import random

buttons = 0
td=time.time()

#Classe héritant, de Frame affichant le mobile.

class Arbre(Frame):
    def __init__(self,tk):
        Frame.__init__(self,tk)



        self.scale = DoubleVar()                                                                                                                                                                                                                                                                                            #Variable permettant de définir l'échelle du mobile pour le Zoom.
        self.scale.set(1)
        self.top=Frame(tk)                                                                                                                                                                                                                                                                                                  #Frame servant à l'affichage des information liée au mobile, FPS, score temps écoulé.
        self.boutons=Frame(tk)                                                                                                                                                                                                                                                                                    #Frame permetant l'affichage des boutons si il est impossible de cliquer sur les boules.
        self.window=Frame(tk)                                                                                                                                                                                                                                                                                               #Frame contenant le mobile.

        xscrollbar = Scrollbar(self.window, orient=HORIZONTAL)                                                                                                                                                                                                                                                              #ScrollBar Horrizontal
        yscrollbar = Scrollbar(self.window)                                                                                                                                                                                                                                                                                 #ScrollBar Vertical
        zoomscrollbar = Scale(self.window, orient=HORIZONTAL, from_=.1, to=5,  label="échelle",                                                                                                                                                                                                                             #ScrollBar Zoom
            resolution=.1, tickinterval=2, bigincrement=1, fg="white", bg="#303030",
            highlightbackground='#303030', variable=self.scale)
        zoomscrollbar.pack(side=TOP,fill="both")



        self.projet = projet.Projet(tk)                                                                                                                                                                                                                                                                                     #Conservation de la Frame Menu Projet pour la navigation.
        self.projet.bouton_arbre.config(height=2,width=20)
        self.projet.bouton_liste.config(height=2,width=20)
        self.projet.bouton_retour.config(height=2,width=20)

        self.projet.pack(side=LEFT,fill="both")
        self.top.pack(side=TOP,fill="both")
        self.boutons.pack(side=BOTTOM,fill="both")
        self.window.pack(fill="y")

        self.labTemps=Label(self.top,text="Temps écoulé : "+str(int(time.time()-td)))
        self.labScore=Label(self.top,text="Score : "+str(int(score/math.pi*180)))
        self.labFPS=Label(self.top,text="FPS : "+str((1//tempsUnitaire)))
        self.labTemps.pack(side=RIGHT)
        self.labScore.pack(side=LEFT)
        self.labFPS.pack()

        self.canvas = Canvas(self.window,width=l*4,height=l*4,background="white",xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, xscrollincrement = 10, yscrollincrement = 10, scrollregion=(0, 0, l*4, l*4))                                                                                                 #Création du canvas du mobile avec les fonction de scroll.
        xscrollbar.config(command=self.canvas.xview)                                                                                                                                                                                                                                                                        #Configuration des scrollbar.
        yscrollbar.config(command=self.canvas.yview)
        xscrollbar.pack(side=BOTTOM,fill="both")
        yscrollbar.pack(side=RIGHT,fill="both")

        #initialisation des données.

        self.canvas.pack(fill="both")
        self.tableau = None
        self.sommet = None
        self.profondeur = 0
        self.maximum = 0
        self.longueurMin = 2*l
        self.rayon = 0

        #Premier parcours de l'arbre permetant le setup de certaine variable tel que la taille des boules.
    def initialisation(self,tableau):
        setScore(0)
        print(getScore())
        self.sommet = self.construction(tableau)
        self.initAffichage(self.sommet)
        self.calculRayon()
        self.affichage(self.sommet)

        #Calcul du rayon des boules pour évité le chevauchement.
    def calculRayon(self):
        self.rayon = self.longueurMin/(2*(self.maximum)**(1/3))

        #Fonction récursive en parcours sufixe permettant la construction de l'arbre a partir du tableau de description
    def construction(self,tableau,i=0):
        sommet = Sommet()
        if type(tableau[0])!=int :
            sommet.gauche = self.construction(tableau[0],i+1)
        else :
            sommet.gauche = Sommet()
            (sommet.gauche).poids = tableau[0]
            (sommet.gauche).poidsVar = tableau[0]
            self.maximum = max(self.maximum,(sommet.gauche).poids)
        if type(tableau[1])!=int :
            sommet.droit = self.construction(tableau[1],i+1)
        else :
            sommet.droit = Sommet()
            (sommet.droit).poids= tableau[1]
            (sommet.droit).poidsVar= tableau[1]
            self.maximum = max(self.maximum,(sommet.droit).poids)

        sommet.poids = (sommet.gauche).poids + (sommet.droit).poids
        sommet.poidsVar = (sommet.gauche).poids + (sommet.droit).poids
        sommet.barycentre = (sommet.droit).poids / sommet.poids
        self.profondeur = max(self.profondeur,i)

        return sommet

        #Fonction gérant l'affichage du mobile grace au donnée de l'arbre de même elle est "recursive" par rapport a ces fils.
    def affichage(self,sommet,i=1,x=l,lo=2*l):
        if i == 1 :
            #Cas particulier du premier barycentre. différament au autres le premier barycentre est dessiner aprés la barre.
            i=15
            self.canvas.create_line(l+l*2*sommet.barycentre,h*(i-1),l+l*2*sommet.barycentre,h*(i-1))
            self.canvas.create_line(l*2-l,h*i,l*2+l,h*i)
            self.canvas.create_line(l*2-l,h*i,l*2-l,h*(i+1))
            self.canvas.create_line(l*2+l,h*i,l*2+l,h*(i+1))
            #recursivité
            self.affichage(sommet.gauche,i+1,l*2-l,2*l)
            self.affichage(sommet.droit,i+1,l*2+l,2*l)
        elif sommet.barycentre != None :
            #Le barycentre est fixe, et la barre est placé pour que le rapport corresponde.
            self.canvas.create_line(x-(sommet.longueur*sommet.barycentre),h*i,x+(sommet.longueur*(1-sommet.barycentre)),h*i)
            self.canvas.create_line(x-(sommet.longueur*sommet.barycentre),h*(i+1),x-(sommet.longueur*sommet.barycentre),h*i)
            self.canvas.create_line(x+(sommet.longueur*(1-sommet.barycentre)),h*(i+1),x+(sommet.longueur*(1-sommet.barycentre)),h*i)
            #recursivité
            self.affichage(sommet.gauche,i+1,x-(sommet.longueur*sommet.barycentre),sommet.longueur)
            self.affichage(sommet.droit,i+1,x+(sommet.longueur*(1-sommet.barycentre)),sommet.longueur)
        else :
            #On arrive au feuille ou creer donc les boule.
            sommet.color=self.randomColor()
            global buttons
            sommet.tagListen = "listen"+str(buttons)
            if degrade :
                self.sphereDegrade(self.canvas,sommet.color,x-(sommet.poids)**(1/3)*self.rayon,h*i,x+(sommet.poids)**(1/3)*self.rayon,h*i+(sommet.poids)**(1/3)*self.rayon*2,sommet)
            else :
                self.canvas.create_oval(x-(sommet.poids)**(1/3)*self.rayon,h*i,x+(sommet.poids)**(1/3)*self.rayon,h*i+(sommet.poids)**(1/3)*self.rayon*2,fill=sommet.color)
            #Les boules sont des boutons permetant d'initier leur errosion ou de l'arreter
            sommet.button = Button(self.boutons, text=str(sommet.poids), command=sommet.erroClick,bg=sommet.color)
            sommet.button.grid(row=0, column=buttons, sticky=W+N+E+S)
            buttons = buttons+1

            #Fonction completant les donner indispensable des arbres tel que leur positions avant l'affichage.
    def initAffichage(self,sommet,i=1,x=l,lo=2*l):
        if i == 1 :
            i=15
            #recursivité
            sommet.y = h*(i-1)
            sommet.x = l+l*2*sommet.barycentre
            sommet.longueur = 2*l
            sommet.droit.y = h*(i)
            sommet.droit.x = 3*l
            sommet.gauche.y = h*(i)
            sommet.gauche.x = l
            self.initAffichage(sommet.gauche,i+1,l*2-l,2*l)
            self.initAffichage(sommet.droit,i+1,l*2+l,2*l)
        elif sommet.barycentre != None :
            sommet.calculLongueur(lo)
            self.longueurMin = min(sommet.longueur,self.longueurMin)
            sommet.droit.y = h*(i)
            sommet.droit.x = x+(sommet.longueur*(1-sommet.barycentre))
            sommet.gauche.y = h*(i)
            sommet.gauche.x = x-(sommet.longueur*sommet.barycentre)
            #recursivité
            self.initAffichage(sommet.gauche,i+1,x-(sommet.longueur*sommet.barycentre),sommet.longueur)
            self.initAffichage(sommet.droit,i+1,x+(sommet.longueur*(1-sommet.barycentre)),sommet.longueur)

            #Fonction permetant l'affichage dynamique de facon récursive en parcours sufixe.
    def afficheDyna(self,sommet):
        self.canvas.create_line(l+l*2*self.sommet.barycentre,15*h,l+l*2*self.sommet.barycentre,0,width=2)
        if sommet.gauche.barycentre != None:
            self.afficheDyna(sommet.gauche)
        else:
            if degrade :
                self.sphereDegrade(self.canvas,sommet.gauche.color,sommet.gauche.x-(sommet.gauche.poidsVar)**(1/3)*self.rayon,sommet.gauche.y+h,sommet.gauche.x+(sommet.gauche.poidsVar)**(1/3)*self.rayon,sommet.gauche.y+h+(sommet.gauche.poidsVar)**(1/3)*self.rayon*2,sommet.gauche)
            else :
                 self.canvas.create_oval(sommet.gauche.x-(sommet.gauche.poidsVar)**(1/3)*self.rayon,sommet.gauche.y+h,sommet.gauche.x+(sommet.gauche.poidsVar)**(1/3)*self.rayon,sommet.gauche.y+h+(sommet.gauche.poidsVar)**(1/3)*self.rayon*2,fill=sommet.gauche.color,tags=sommet.gauche.tagListen,width=2)
                 self.canvas.tag_bind(sommet.gauche.tagListen,"<Button-1>",sommet.gauche.erroClick)
        if sommet.droit.barycentre != None:
            self.afficheDyna(sommet.droit)
        else :
            if degrade :
                self.sphereDegrade(self.canvas,sommet.droit.color,sommet.droit.x-(sommet.droit.poidsVar)**(1/3)*self.rayon,sommet.droit.y+h,sommet.droit.x+(sommet.droit.poidsVar)**(1/3)*self.rayon,sommet.droit.y+h+(sommet.droit.poidsVar)**(1/3)*self.rayon*2,sommet.droit)
            else :
                self.canvas.create_oval(sommet.droit.x-(sommet.droit.poidsVar)**(1/3)*self.rayon,sommet.droit.y+h,sommet.droit.x+(sommet.droit.poidsVar)**(1/3)*self.rayon,sommet.droit.y+h+(sommet.droit.poidsVar)**(1/3)*self.rayon*2,fill=sommet.droit.color,tags=sommet.droit.tagListen,width=2)
                self.canvas.tag_bind(sommet.droit.tagListen,'<Button-1>',sommet.droit.erroClick)


        self.canvas.create_line(sommet.gauche.x,sommet.gauche.y,sommet.droit.x,sommet.droit.y,width=2)
        self.canvas.create_line(sommet.gauche.x,sommet.gauche.y,sommet.gauche.x,sommet.gauche.y+h,width=2)
        self.canvas.create_line(sommet.droit.x,sommet.droit.y,sommet.droit.x,sommet.droit.y+h,width=2)

        #Fonction mettant a jours l'ensemble des données de la frame : le mobile et les label.
    def update(self):
        t0=time.time()
        self.sommet.majAll()
        self.canvas.delete("all")
        self.afficheDyna(self.sommet)
        self.canvas.scale(ALL, 0, 0, self.scale.get(), self.scale.get())
        self.canvas.config(scrollregion=(0, 0, l*4*self.scale.get(), l*4*self.scale.get()))
        self.canvas.update()
        setTempsUnitaire(time.time()-t0)
        self.labScore["text"]="Score : "+str(int(getScore()/math.pi*180))
        self.labTemps["text"]="Temps écoulé : "+str(int(time.time()-td))
        self.labFPS["text"]="FPS : "+str(1//getTempsUnitaire())


#Ensemble de fonction indispensable a l'affichage des couleur et du dégrader.
    def randomColor(self):
        return COLORS[random.randint(0,751)]

    def RGBToHTMLColor(self,rgb_tuple):
        """ convert an (R, G, B) tuple to #RRGGBB """
        hexcolor = '#%02x%02x%02x' % rgb_tuple
        # that's it! '%02x' means zero-padded, 2-digit hex values
        return hexcolor

    def HTMLColorToRGB(self,colorstring):
        """ convert #RRGGBB to an (R, G, B) tuple """
        colorstring = colorstring.strip()
        if colorstring[0] == '#': colorstring = colorstring[1:]
        if len(colorstring) != 6:
            raise(ValueError, "input #%s is not in #RRGGBB format" % colorstring)
        r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        return (r, g, b)

    def eclaireci(self,color):
        t=self.HTMLColorToRGB(color)
        red,green,blue=self.HTMLColorToRGB(color)
        if t[0]<253 :
            red=t[0]+3
        if t[1]<253 :
            green=t[1]+3
        if t[2]<253 :
            blue=t[2]+3
        return self.RGBToHTMLColor((red,green,blue))


    def eclaireci2(self,color):
        t=self.HTMLColorToRGB(color)
        red,green,blue=self.HTMLColorToRGB(color)
        if t[0]<243 :
            red=t[0]+12
        if t[1]<252 :
            green=t[1]+3
        if t[2]<240 :
            blue=t[2]+8
        return self.RGBToHTMLColor((red,green,blue))

    def sphereDegrade(self,canvas,color,x0,y0,x1,y1,sommet):
        h=color
        for i in range(0,int((y1-y0)/2)):
            if sommet.erro :
                if i < 2 :
                    if i == 0 :
                        if sommet.clignotant % 5 == 0 :
                            sommet.redOn =  not sommet.redOn
                    if sommet.redOn :
                        canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill="red",width=0,tags=sommet.tagListen)
                        canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                    else :
                        if i == 0 :
                            canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill=h,width=1,tags=sommet.tagListen)
                            canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                        else :
                            canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill=h,width=0,tags=sommet.tagListen)
                            canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                else :
                    canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill=h,width=0,tags=sommet.tagListen)
                    canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                h=self.eclaireci(h)
            else :
                if i == 0 :
                    canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill=h,tags=sommet.tagListen)
                    canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                else :
                    canvas.create_oval((x0+i),(y0+i),x1-i,y1-i,fill=h,width=0,tags=sommet.tagListen)
                    canvas.tag_bind(sommet.tagListen,"<Button-1>",sommet.erroClick)
                h=self.eclaireci(h)
            t=self.HTMLColorToRGB(h)
            if i>= 1 :
                if t[0]+t[1]+t[2]>=759 :
                    break
        sommet.clignotant += 1
