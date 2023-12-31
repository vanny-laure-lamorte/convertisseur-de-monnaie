# Importer le module 
from forex_python.converter import CurrencyRates
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

# Couleur
orange = "#ff6702"
green = "#a2af77"
light_grey = "#3e3e47"
dark_grey = "#21212b"
white = "#ffffff"

# Fenetre principale
fenetre = Tk()
fenetre.geometry("400x450")
fenetre.title ("Convertisseur de monnaie")

# Bandeau gris
top = Frame(fenetre, width=450, height=80, bg=light_grey)
top.grid(row=0, column=0)

# Image logo
logo = Image.open("images/logo.png")
logo = logo.resize((60, 60))
logo = ImageTk.PhotoImage(logo)
app_name = Label(top, image = logo, compound = LEFT, text = "Convertisseur de monnaie", fg = white, height = 5, padx = 1, pady = 30, width= 390, font=('Arial 16 bold'), bg = light_grey)
app_name.place(x=0, y=0)

# Espace principal
main = Frame(fenetre, width=450, height =550, bg=dark_grey)
main.grid(row=1, column=0)

# Rectangle pour afficher le montant
label_montant = Label(main, text = "MONTANT", width = 9, height=1, padx = 5, pady = 1, relief = "flat", anchor = NW, font=('Ivy 16 bold'), fg = white, bg=dark_grey)
label_montant.place (x= 140, y=23)

value = Entry(main, width=27, justify=CENTER, font = ("Ivy 12 bold"), relief = SOLID)
value.place(x =70, y=52)

# Rectangle pour afficher "From" et "To"
label_from = Label(main, text = "FROM", width = 9, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, font=('Ivy 16 bold'), fg = white, bg=dark_grey)
label_from.place (x=64, y=92)

label_to = Label(main, text = "TO", width = 9, height=1, padx = 5, pady = 1, relief = "flat", anchor = NW, font=('Ivy 16 bold'), fg = white, bg=dark_grey)
label_to.place (x= 218, y=92)

# Rectangle pour choisir les devises sous forme de menu deroulant
c = CurrencyRates()
currency = list(c.get_rates('USD').keys())

combo_from = ttk.Combobox (main, width= 8, justify=CENTER, font=("Ivy 12 bold"),)
combo_from["values"] = (currency)
combo_from.place (x=70, y=122)

combo_to = ttk.Combobox (main, width= 8, justify=CENTER, font=("Ivy 12 bold"))
combo_to["values"] = (currency)
combo_to.place (x=218, y=122)

# Fonction pour la conversion 
historique = []

def convertir():
    # Récupérer la devise de départ
    # Récupérer la devise de d'arrivée
    # Récupérer le montant à convertir
    devise_depart = combo_from.get()  
    devise_arrivee = combo_to.get()    
    montant = float(value.get())   
    
    # Récupérer le taux de change
    c = CurrencyRates()
    taux = c.get_rate(devise_depart, devise_arrivee)
    
    # Calculer la conversion
    montant_converti = montant * taux    

    # Ajouter la conersion historique
    historique.append({
        "Montant choisi": montant,
        "Devise de depart": devise_depart,
        "Devise d'arrivee": devise_arrivee,
        "Resultat": montant_converti
    })

    sauvegarder()

    # Mettre à jour l'affichage du résultat
    resultat.config(text=f"{montant} {devise_depart} = {montant_converti:.2f} {devise_arrivee}")

def sauvegarder():
    with open("historique_monnaie.txt", "a") as fichier:
        fichier.write(str(historique) + "\n\n")        

# Rectangle pour déclencher la conversion    
bouton_convertir = Button(main, text="Convertir", width=23, padx=5, height=1, bg=orange, font=("Ivy 12 bold"), relief=SOLID, command=convertir)
bouton_convertir.place(x=70, y=175)

# Rectangle pour afficher le resultat de la conversion
resultat = Label(main, text = " ", width = 17, height=2, padx = 13, pady = 7, relief = "solid", anchor = CENTER, font=('Ivy 16 bold'), bg = white, fg = dark_grey)
resultat.place(x=70, y=220)   

# Sauvegarder les données dans le document txt
def ouvrir_historique():
    fen_historique= Tk()
    fen_historique.title("Historique des conversions")
    fen_historique.geometry("400x450")
    fen_historique.config(bg = dark_grey)
  
# Sauvegarder l'historique des conversions
    historique_listbox = Listbox(fen_historique,  width = 35, height=20, justify= CENTER, font=('Ivy 10 bold'), bg = white, fg = dark_grey)
    historique_listbox.place(x=70, y=55)

# Afficher les éléments de l'historique dans la Listbox    
    for conversion in historique:
        historique_listbox.insert(END, f"{conversion['Montant choisi']} {conversion['Devise de depart']} = {conversion['Resultat']:.2f} {conversion["Devise d'arrivee"]}")

    # Fermer la page historique
    bouton_fermer = Button(fen_historique, text="Fermer", font=("Ivy 10 bold"), width=5, height=1,                   command=fen_historique.destroy, bg=orange, fg=dark_grey, relief="flat")
    bouton_fermer.place (x =70, y=410)

    fen_historique.mainloop()   

# Rectangle pour accéder à l'historique
bouton_historique = Button(main, text="Historique des conversions", width=23, padx=5, height=1, bg=orange, font=("Ivy 12 bold"), relief=SOLID, command=ouvrir_historique)
bouton_historique.place(x=70, y=320) 

fenetre.mainloop ()

