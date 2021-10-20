import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)



# creer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x890")
window.iconbitmap("images.ico")
window.config(background='green')

#creer la frame principale
frame = Frame(window, bg='green')

# creation d'image
width = 500
height = 500
image = PhotoImage(file="images.png").zoom(35).subsample(32)
canvas = Canvas(window, width=width, height=height, bg='green')
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

#creer une sous boite
right_frame = Frame(frame, bg='green')


#creer un titre
label_title = Label(frame,text="Mot de passe", font=("Helvetica", 20), bg='green', fg='white')
label_title.pack()

#creer un input
password_entry = Entry(frame, font=("Helvetica", 20), bg='green', fg='white')
password_entry.pack()

#creer un bouton
generate_password_button = Button(frame,text="Générer", font=("Helvetica", 20), bg='green', fg='white', command=generate_password)
generate_password_button.pack()

#afficher la frame
frame.pack(expand=YES)

#creation barre de menu
menu_bar = Menu(window)
#creer 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer la fenetre pour ajouter la menu bar
window.config(menu=menu_bar)





# afficher la fenetre

window.mainloop()