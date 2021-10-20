from tkinter import *
import webbrowser


def open_livremediatheque():
    webbrowser.open_new("https://fr.wikipedia.org/wiki/M%C3%A9diath%C3%A8que")
 # creer une premiere fenetre
window = Tk()
 # personnaliser la fenetre
window.title("Mediathèque")
window.geometry("1080x720")
window.iconbitmap("images.ico")
window.config(background='#41B77F')

#creer la frame
frame = Frame(window, bg='#41B77F', bd=1, relief=SUNKEN)

 # ajout texte
label_title = Label(frame, text="Bienvenue sur la médiathèque de La Chapelle-Curreaux", font=("Helvetica", 30), bg='#41B77F', fg='white')
label_title.pack()

 #ajout corps du texte
label_subtitle = Label(frame, text="La médiathèque vous propose de consulter et de réserver vos livres directement sur notre site !", font=("Helvetica", 15), bg='#41B77F', fg='white')
label_subtitle.pack()

 #ajouter un bouton
consulter_livre = Button(frame, text="Consulter les livres", font=("Helvetica", 15), bg='#41B77F', fg='white', command=open_livremediatheque)
consulter_livre.pack(pady=10, fill=X)

 # ajouter
frame.pack(expand=YES)
 #afficher

window.mainloop()