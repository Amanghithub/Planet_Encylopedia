from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk


root = Tk()
root.title("Planet Encylopidea")
root.geometry("1000x1000")
root.configure(background="lightblue")

mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
earth = ImageTk.PhotoImage(Image.open("earth.jpg"))
venus = ImageTk.PhotoImage(Image.open("venus.jpg"))

planets = ["Mercury","Venus","Earth"]

selected_planet = StringVar()

dropdown = ttk.Combobox(root,values=planets,textvariable=selected_planet)
dropdown.place(relx=0.5,rely=0.1)

lbl_planet = Label(root,text="Planet: ",bg="lightblue")
lbl_planet.place(relx=0.2,rely=0.1,anchor=CENTER)

lbl_planetname = Label(root,font=("courier",20,"bold"),bg="lightblue")
lbl_planetname.place(relx=0.5,rely=0.25,anchor=CENTER)

lbl_planetimg = Label(root,bg="yellow",highlightthickness=5,borderwidth=2,relief=SOLID)
lbl_planetimg.place(relx=0.5,rely=0.5,anchor=CENTER)

lbl_gravity = Label(root,font=("courier",20,"bold"),bg="lightblue")
lbl_gravity.place(relx=0.5,rely=0.7,anchor=CENTER)

lbl_radius = Label(root,font=("courier",20,"bold"),bg="lightblue")
lbl_radius.place(relx=0.5,rely=0.8,anchor=CENTER)

lbl_info = Label(root,font=("courier",8),bg="lightblue")
lbl_info.place(relx=0.5,rely=0.9,anchor=CENTER)

def planetInfo():
    planet = selected_planet.get()
    
    if(planet == "Mercury"):
        lbl_planetname["text"]="Mercury"
        lbl_planetimg["image"]=mercury
        lbl_gravity["text"]="Gravity: 3.7m/second2"
        lbl_radius["text"]="Radius: 2439.7km"
        lbl_info["text"]="Mercury is the smallest planet in our Solar System it is just a little bigger than Earth's Moon."
        
    elif(planet == "Venus"):
        lbl_planetname["text"]="Venus"
        lbl_planetimg["image"]=venus
        lbl_gravity["text"]="Gravity: 8.87m/second2"
        lbl_radius["text"]="Radius: 6051.8km"
        lbl_info["text"]="Venus is the brighest object in the sky after the Sun and the Moon and sometimes looks like a bright star in the morning or evening sky."
        
    elif(planet == "Earth"):
        lbl_planetname["text"]="Earth"
        lbl_planetimg["image"]=earth
        lbl_gravity["text"]="Gravity: 9.8m/second2"
        lbl_radius["text"]="Radius: 6371km"
        lbl_info["text"]="Earth is the only place in the known universe confirmed to host life and its the only one known to have liquid water on its surface"
    
button = Button(root,text="Show Planet Info",command=planetInfo)
button.place(relx=0.5,rely=0.18,anchor=CENTER)

root.mainloop()