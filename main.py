from customtkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import mysql.connector




root = CTk()
# Set window position and size
screen_width=root.winfo_screenwidth()
x=round(screen_width/2-540)
screen_hight=root.winfo_screenheight()
y=round(screen_hight/2-360)
root.geometry(f'1080x720+{x}+{y}')
root.title('Pharmacy management system')
root.resizable(False, False)
iconpath = ImageTk.PhotoImage(file=os.path.join("Pharmacy assets","backgrounds", "icon.png"))
root.wm_iconbitmap()
root.iconphoto(False, iconpath)




def clicked():
    print('Done')




# Function to handle the login process
def login_to_main_win():
    if (ent_username.get()=='' or ent_username.get()=='Username') or (ent_password.get()=='' or ent_password.get()=='Password'):
        messagebox.showerror('Entry error','Type user name or password !!')
    else:
        try:
            # Connect to the database
            with mysql.connector.connect(host='localhost', user='root', password='2003', database='loginDB') as mydb:
                mycursor = mydb.cursor()
                print("connected to database")
                command = "SELECT * FROM login WHERE Username=%s AND Password=%s"
                mycursor.execute(command, (ent_username.get(), ent_password.get()))
                myresult = mycursor.fetchone()
                print(myresult)
                if myresult is None:
                    messagebox.showinfo("invalid", "Invalid username and password")

                else:
                    messagebox.showinfo("Login", "Successfully logged in")
                    main_window()  
        except mysql.connector.Error as err:
            messagebox.showerror('Connection error', f'Database connection error: {err}')
            return



# Function to display the main window after successful login.
def main_window():
    # Hide login elements
    background_login_label.pack_forget()
    ent_username.place_forget()
    ent_password.place_forget()
    login_button.place_forget()
    signup_label.place_forget()
    signup_button.place_forget()

    # Place your main window widgets here
    main_screen_background = CTkImage(Image.open(os.path.join("Pharmacy assets", "backgrounds", "mainscreen-01.jpg")), size=(1080, 720))
    background_screen_label = CTkLabel(root, image=main_screen_background, text='')
    background_screen_label.pack()

    # Place other buttons as per your design
    plus_image = CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "plus.png")), size=(24, 24))
    add_button = CTkButton(root, text='Add Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=plus_image,font=fnt_not_bold,command=clicked)
    add_button.place(x=15, y=300)

    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "drug.png")), size=(24, 24))
    view_button = CTkButton(root, text='View Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    view_button.place(x=15,y=360)




    dvalidity_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "pills.png")), size=(24, 24))
    validity_button = CTkButton(root, text='Validity Check', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    validity_button.place(x=15,y=420)


    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "validity.png")), size=(24, 24))
    modify_button = CTkButton(root, text='Modify Medicine', bg_color='#F7F9F8', fg_color='#2157C2', text_color='white',height=47,width=195,corner_radius=10,hover_color='#3F70D4',image=drug_image,font=fnt_not_bold,command=clicked)
    modify_button.place(x=15,y=480)




def sign_up_function():
        print(ent_new_username.get(),ent_new_password.get())
        if (ent_new_username.get()=='' or ent_new_username.get()=='Add Username') or (ent_new_password.get()=='' or ent_new_password.get()=='Add Password'):
                messagebox.showerror('Entry error','Type user name or password !!')
        else:
                try:
                        # Connect to the database
                        mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='loginDB')
                        mycursor=mydb.cursor()
                        print("connected to database")
                        # Insert new user into database
                        command="use loginDB"
                        mycursor.execute(command)
                        command="insert into login(Username,Password) values(%s,%s)"
                        mycursor.execute(command, (ent_new_username.get(), ent_new_password.get()))
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("register","new user added sucessfully")


                except:
                        messagebox.showerror('connection','Database connection not stablish')






def back_to_login():
    # Destroy sign-up elements
    background_signup_label.destroy()
    ent_new_username.destroy()
    ent_new_password.destroy()
    signup_btn.destroy()
    back_btn.destroy()

    # Show login elements
    background_login_label.pack()
    ent_username.place(x=40,y=300)
    ent_password.place(x=40,y=380)
    login_button.place(x=40,y=490)
    signup_label.place(x=115,y=600)
    signup_button.place(x=247,y=603)






def signup_win():
    global background_signup_label, ent_new_username, ent_new_password, signup_btn, back_btn
    # Hide login elements
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

    signup_btn = CTkButton(root, text='Sign up', text_color='white', bg_color='#F7F9F8', fg_color='#2658B6', width=315, height=53, corner_radius=25, font=fnt,command=sign_up_function,hover_color='#3F70D4')
    signup_btn.place(x=40,y=490)

    back_btn = CTkButton(root, text='<', text_color='#2658B6', bg_color='#F7F9F8', fg_color='#F7F9F8',hover_color='#F7F9F8',height=25,width=25,font=CTkFont(family='Bahnschrift', size=30), command=back_to_login)
    back_btn.place(x=1,y=0)



# Create login screen elements
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