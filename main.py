from customtkinter import *
from PIL import Image
import os





root = CTk()
root.geometry('1080x720')
root.title('Pharmacy management system')
root.resizable(False, False)


def clicked():
    print('Done')

def login_to_main_win ():
    background_login_label.pack_forget()
    ent_username.place_forget()
    ent_password.place_forget()
    login_button.place_forget()
    signup_label.place_forget()
    signup_button.place_forget()


    main_screen_background = CTkImage(Image.open(os.path.join("Pharmacy assets", "backgrounds", "mainscreen-01.jpg")), size=(1080, 720))
    background_screen_label = CTkLabel(root, image=main_screen_background, text='')
    background_screen_label.pack()

    plus_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "plus.png")), size=(24, 24))
    add_button = CTkButton(root, text='Add Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=plus_image,font=fnt_not_bold,command=clicked)
    add_button.place(x=15,y=300)


    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "drug.png")), size=(24, 24))
    view_button = CTkButton(root, text='View Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    view_button.place(x=15,y=360)




    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "pills.png")), size=(24, 24))
    modify_button = CTkButton(root, text='Modify Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    modify_button.place(x=15,y=420)


    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "validity.png")), size=(24, 24))
    modify_button = CTkButton(root, text='Modify Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    modify_button.place(x=15,y=480)










def sign_up():
    pass









def back_to_login():
    # Destroy signup window widgets
    background_signup_label.destroy()
    ent_new_username.destroy()
    ent_new_password.destroy()
    signup_btn.destroy()
    back_btn.destroy()

    # Recreate login window widgets
    background_login_label.pack()
    ent_username.place(x=40,y=300)
    ent_password.place(x=40,y=380)
    login_button.place(x=40,y=490)
    signup_label.place(x=115,y=600)
    signup_button.place(x=247,y=603)



def signup_win():
    global background_signup_label, ent_new_username, ent_new_password, signup_btn, back_btn
    # Destroy widgets from login window
    background_login_label.pack_forget()
    ent_username.place_forget()
    ent_password.place_forget()
    login_button.place_forget()
    signup_label.place_forget()
    signup_button.place_forget()


    signup_background = CTkImage(Image.open(os.path.join("Pharmacy assets", "backgrounds", "signup-bacground.jpg")), size=(1080, 720))
    background_signup_label = CTkLabel(root, image=signup_background, text='')
    background_signup_label.pack()

    ent_new_username = CTkEntry(root, placeholder_text='New Username', bg_color='#F7F9F8', fg_color='white', border_color='#1E61D8', corner_radius=25, height=47, width=316, text_color='black')
    ent_new_username.place(x=40,y=300)

    ent_new_password = CTkEntry(root, placeholder_text='New Password', bg_color='#F7F9F8', fg_color='white', border_color='#1E61D8', corner_radius=25, height=47, width=316, text_color='black')
    ent_new_password.place(x=40,y=380)

    signup_btn = CTkButton(root, text='Sign up', text_color='white', bg_color='#F7F9F8', fg_color='#2658B6', width=315, height=53, corner_radius=25, font=fnt,command=sign_up,hover_color='#3F70D4')
    signup_btn.place(x=40,y=490)

    back_btn = CTkButton(root, text='<', text_color='#2658B6', bg_color='#F7F9F8', fg_color='#F7F9F8',hover_color='#F7F9F8',height=25,width=25,font=CTkFont(family='Bahnschrift', size=30), command=back_to_login)
    back_btn.place(x=1,y=0)




login_background = CTkImage(Image.open(os.path.join("Pharmacy assets", "backgrounds", "login-background.jpg")), size=(1080, 720))
background_login_label = CTkLabel(root, image=login_background, text='')
background_login_label.pack()

fnt = CTkFont(family='Bahnschrift', weight='bold', size=20)
fnt_not_bold = CTkFont(family='Bahnschrift', size=17)
ent_username = CTkEntry(root, placeholder_text='Username', bg_color='#F7F9F8', fg_color='white', border_color='#1E61D8', corner_radius=25, height=47, width=316, text_color='black')
ent_username.place(x=40,y=300)

ent_password = CTkEntry(root, placeholder_text='Password', bg_color='#F7F9F8', fg_color='white', border_color='#1E61D8', corner_radius=25, height=47, width=316, text_color='black')
ent_password.place(x=40,y=380)

login_button = CTkButton(root, text='Login', text_color='white', bg_color='#F7F9F8', fg_color='#2658B6', width=315, height=53, corner_radius=25, font=fnt,command=login_to_main_win,hover_color='#3F70D4')
login_button.place(x=40,y=490)

signup_label = CTkLabel(root, text='Dont have an account ?', bg_color='#F7F9F8', text_color='black')
signup_label.place(x=115,y=600)


signup_button = CTkButton(root, text='Sign up', bg_color='#F7F9F8', fg_color='#F7F9F8', text_color='#2658B6', width=35, height=10, hover_color='#FfF9F8', command=signup_win)
signup_button.place(x=247,y=603)

root.mainloop()