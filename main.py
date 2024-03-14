from customtkinter import *
from PIL import Image
import os



root = CTk()
root.geometry('1080x720')
root.title('Pharmacy management system')
root.resizable(False,False)

login_background = CTkImage(Image.open(os.path.join("Pharmacy assets", "backgrounds", "login-background.jpg")),size=(1080,720))
background_login_label = CTkLabel(root, image=login_background,text='')
background_login_label.pack()

fnt = CTkFont(family='Bahnschrift', weight='bold', size=20)

ent_username=CTkEntry(root,placeholder_text='Username',bg_color='#F7F9F8',fg_color='white',border_color='#1E61D8',corner_radius=25,height=47,width=316,text_color='black')
ent_username.place(x=40,y=300)


ent_password=CTkEntry(root,placeholder_text='Password',bg_color='#F7F9F8',fg_color='white',border_color='#1E61D8',corner_radius=25,height=47,width=316,text_color='black')
ent_password.place(x=40,y=380)




login_button=CTkButton(root,text='Login',text_color='white',bg_color='#F7F9F8',fg_color='#2658B6',width=315,height=53,corner_radius=25,font=fnt)
login_button.place(x=40,y=490)




signup_label=CTkLabel(root,text='Dont have an account ?',bg_color='#F7F9F8',text_color='black')
signup_label.place(x=115,y=600)

signup_button=CTkButton(root,text='Sign up',bg_color='#F7F9F8',fg_color='#F7F9F8',text_color='#2658B6',width=35,height=10,hover_color='#FfF9F8')
signup_button.place(x=247,y=603)








root.mainloop()
