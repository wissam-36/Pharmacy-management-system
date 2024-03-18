from customtkinter import *
from tkinter import messagebox
from customtkinter import CTkToplevel
from tkinter import Text,Toplevel
from PIL import Image,ImageTk
import os
import mysql.connector
import tkinter as tk
from tkinter import Text
from tkinter import ttk




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



def add_medicine():
    def save_medicine():
        if (medicine_name.get()=='' or medicine_name.get()=='Medicine Name') or \
        (medicine_quantity.get()=='' or medicine_quantity.get()=='Quantity') or \
        (validity_date.get()=='' or validity_date.get()=='Validity Date') or \
        (purchase_price.get()=='' or purchase_price.get()=='purchase Price') or \
        (selling_price.get()=='' or selling_price.get()=='Selling Price'):
            messagebox.showerror('Entry error', 'There are entries that you did not write !!')
        else:
            try:
                # Connect to the database
                mydb = mysql.connector.connect(host='localhost', user='root', password='2003', database='PharmacyDB')
                mycursor = mydb.cursor()
                print("connected to database")
            
                # Insert new medicine into database
                command = "INSERT INTO Medicines (medicine_name, expiry_date, purchase_price, selling_price, quantity) VALUES (%s, %s, %s, %s, %s)"
                data = (medicine_name.get(), validity_date.get(), purchase_price.get(), selling_price.get(), medicine_quantity.get())
                mycursor.execute(command, data)
            
                mydb.commit()
                mydb.close()
            
                messagebox.showinfo("Success", "New Medicine added successfully")

            except mysql.connector.Error as err:
                messagebox.showerror('Database Error', f'Database error: {err}')


    medicine_name = CTkEntry(root, placeholder_text='Medicine Name', bg_color='#E7ECF2', fg_color='white',
                             text_color='black', height=40, width=260, corner_radius=5)
    medicine_name.place(x=240, y=40)

    medicine_quantity = CTkEntry(root, placeholder_text='Quantity', bg_color='#E7ECF2', fg_color='white',
                                 text_color='black', height=40, width=260, corner_radius=5)
    medicine_quantity.place(x=600, y=40)

    validity_date = CTkEntry(root, placeholder_text='Example 2025-7-18', bg_color='#E7ECF2', fg_color='white',
                              text_color='black', height=40, width=260, corner_radius=5)
    validity_date.place(x=240, y=160)

    purchase_price = CTkEntry(root, placeholder_text='purchase Price', bg_color='#E7ECF2', fg_color='white',
                             text_color='black', height=40, width=260, corner_radius=5)
    purchase_price.place(x=600, y=160)

    selling_price = CTkEntry(root, placeholder_text='Selling Price', bg_color='#E7ECF2', fg_color='white',
                             text_color='black', height=40, width=260, corner_radius=5)
    selling_price.place(x=600, y=200)

    done_btn = CTkButton(root, text='Done', bg_color='#E7ECF2', fg_color='#3F70D4', text_color='white',
                         corner_radius=5, hover_color='#618EE0', font=fnt_not_bold, command=save_medicine)
    done_btn.place(x=900, y=600)

    reset_btn = CTkButton(root, text='Reset', bg_color='#E7ECF2', fg_color='#3F70D4', text_color='white',
                          corner_radius=5, hover_color='#618EE0', font=fnt_not_bold)
    reset_btn.place(x=900, y=640)





def view_medicines():
    
    try:
        # Connect to the database
        mydb = mysql.connector.connect(host='localhost', user='root', password='2003', database='PharmacyDB')
        mycursor = mydb.cursor()

        # Execute the query to fetch data
        mycursor.execute("SELECT medicine_name, expiry_date, purchase_price, selling_price, quantity FROM Medicines")
        medicines = mycursor.fetchall()

        # Create a frame to contain the treeview
        tree_frame = CTkFrame(root)
        tree_frame.place(x=330, y=40)

        # Define treeview
        tree = ttk.Treeview(tree_frame, columns=("Medicine Name", "Expiry Date", "Purchase Price", "Selling Price", "Quantity"))
        tree.pack(expand=True, fill="both")

        # Define column headings and adjust column width
        tree.heading("#0", text="ID", anchor=tk.CENTER)
        tree.column("#0", width=50)
        tree.heading("#1", text="Medicine Name", anchor=tk.CENTER)
        tree.column("#1", width=150)
        tree.heading("#2", text="Expiry Date", anchor=tk.CENTER)
        tree.column("#2", width=100)
        tree.heading("#3", text="Purchase Price", anchor=tk.CENTER)
        tree.column("#3", width=100)
        tree.heading("#4", text="Selling Price", anchor=tk.CENTER)
        tree.column("#4", width=100)
        tree.heading("#5", text="Quantity", anchor=tk.CENTER)
        tree.column("#5", width=100)

        # Insert data into the treeview
        for idx, medicine in enumerate(medicines, start=1):
            tree.insert("", "end", text=idx, values=medicine)

        mydb.close()
    except mysql.connector.Error as err:
        messagebox.showerror('Database Error', f'Database error: {err}')


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
    add_button = CTkButton(root, text='Add Medicine',bg_color='#2157C2', fg_color='#3F70D4', text_color='white',height=47,width=195,corner_radius=10,hover_color='#618EE0',image=plus_image,font=fnt_not_bold,command=add_medicine)
    add_button.place(x=10, y=300)

    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "drug.png")), size=(24, 24))
    view_button = CTkButton(root, text='View Medicine',bg_color='#2157C2', fg_color='#3F70D4', text_color='white',height=47,width=195,corner_radius=10,hover_color='#618EE0',image=drug_image,font=fnt_not_bold,command=view_medicines)
    view_button.place(x=10,y=360)




    drug_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "pills.png")), size=(24, 24))
    modify_button = CTkButton(root, text='Modify Medicine',bg_color='#2157C2', fg_color='#3F70D4', text_color='white',height=47,width=195,corner_radius=10,hover_color='#618EE0',image=drug_image,font=fnt_not_bold,command=add_medicine)
    modify_button.place(x=10,y=420)


    validity_image= CTkImage(Image.open(os.path.join("Pharmacy assets", "buttons", "validity.png")), size=(24, 24))
    validity_button = CTkButton(root, text='Validity Check', bg_color='#2157C2', fg_color='#3F70D4', text_color='white',height=47,width=195,corner_radius=10,hover_color='#618EE0',image=validity_image ,font=fnt_not_bold,command=add_medicine)
    validity_button.place(x=10,y=480)




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