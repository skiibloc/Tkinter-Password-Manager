import tkinter as tk
import tkinter.messagebox
import time
import shutil
import random
import string
import re
window = tk.Tk()
window.geometry("600x400")

def main():
    for widgets in window.winfo_children():
        widgets.destroy()

    def delete():
        global string
        global file
        name = string.get()
        fileName = 'passwords.txt'
        

        string = open(fileName).read()
        new_str = re.sub(name, '', string)
        open(fileName, 'w').write(new_str)
        deleteConfirm = tk.Label(window, text='Successfully deleted Password')
        again = tk.Button(window, text='Run Again', command=main)
        deleteConfirm.pack()
        again.pack()
    
    def findLine():
        global line
        global file
        global string
        again.pack_forget()
        file = open('passwords.txt', 'r')
        string = tk.Entry(window, width=80)
        stringConfirm = tk.Button(window, text='Confirm', command=delete)
        string.pack()
        stringConfirm.pack()
    
    def searchComplete():
        global searchItem
        global line
        global search
        global again
        search = searchItem.get()
        searchItem.pack_forget()
        searchButton.pack_forget()
        
        with open("passwords.txt") as openfile:
            for line in openfile:
                if search in line:
                    window.clipboard_clear()
                    window.clipboard_append(line)
                    searchLabel = tk.Label(window, text=line)
                    
                    searchLabel.pack()
                    
        deleteButton = tk.Button(window, text='Delete Passwords', command=findLine)           
        again = tk.Button(window, text='Restart', command=main)
        deleteButton.pack()
        again.pack()
        
        

    def search():
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        global searchItem
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        searchItem = tk.Entry(window)
        searchButton = tk.Button(window, text='Search', command=searchComplete)
        searchItem.pack()
        searchButton.pack()

    def copy():
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        number_ = random.randint(1,1000000)
        number = str(number_)
        shutil.copyfile('passwords.txt', 'copy' + number + '.txt')
        copyConfirm = tk.Label(window, text='Successfully copied Passwords')
        again = tk.Button(window, text='Restart', command=main)
        copyConfirm.pack()
        again.pack()

    def leave():
        window.destroy()
        
    
    def addComplete():
        websites.pack_forget()
        names.pack_forget()
        pwds.pack_forget()
        infoLabel.pack_forget()
        addConfirm.pack_forget()
        website = websites.get()
        name = names.get()
        pwd = pwds.get()
        with open ('passwords.txt', 'a') as f:
            f.write(website + " // " + name + " // " + pwd + "\n")
        completeLabel1 = tk.Label(window, text="Successfully added Password to database")
        again = tk.Button(window, text='Restart', command=main)
        completeLabel1.pack()
        again.pack()
        


    def view():
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        with open ('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                viewLabel = tk.Label(window, text=data)
                viewLabel.pack()
        
        again = tk.Button(window, text='Run Again', command=main)
        again.pack()


    def copyAdd(): #required because reular add ran into some issues
        global infoLabel
        global websites
        global names
        global pwds
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        global passwlength
        global password
        global passwLabel
        global passwCopy
        global passwButton
        global again
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        passwLabel.pack_forget()
        passwCopy.pack_forget()
        again.pack_forget()
        passwlength.pack_forget()
        passwButton.pack_forget()
        copyConfirm.pack_forget()
        createLogin.pack_forget()
        infoLabel = tk.Label(window, text="First box is the website. Second is username. Third is Password")
        websites = tk.Entry(window)
        names = tk.Entry(window)
        pwds = tk.Entry(window)
        addConfirm = tk.Button(window, text = "Submit Login: ", command=addComplete)
        again = tk.Button(window, text='Restart', command=main)
        infoLabel.pack()
        websites.pack()
        names.pack()
        pwds.pack()
        addConfirm.pack()
        again.pack()

    def add():
        global infoLabel
        global websites
        global names
        global pwds
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        global passwlength
        global password
        global passwLabel
        global passwCopy
        global passwButton
        global again
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        infoLabel = tk.Label(window, text="First box is the website. Second is username. Third is Password")
        websites = tk.Entry(window)
        names = tk.Entry(window)
        pwds = tk.Entry(window)
        addConfirm = tk.Button(window, text = "Submit Login: ", command=addComplete)
        again = tk.Button(window, text='Restart', command=main)
        infoLabel.pack()
        websites.pack()
        names.pack()
        pwds.pack()
        addConfirm.pack()
        again.pack()

    def copyPassw():
        global copyConfirm
        global createLogin
        global passwLabel
        window.clipboard_clear()
        window.clipboard_append(password)
        copyConfirm = tk.Label(window, text='Successfully copied Password to clipboard')
        createLogin = tk.Button(window, text='Create a login with this password', command=copyAdd)
        copyConfirm.pack()
        createLogin.pack()

    def newPassw():
        global passwlength
        global password
        global passwLabel
        global passwCopy
        global again
        length_ = passwlength.get()
        length = int(length_)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        temp = random.sample(all, length)

        password = ''.join(temp)

        passwLabel = tk.Label(window, text=password)
        passwCopy = tk.Button(window, text='Copy Password?', command=copyPassw)
        again = tk.Button(window, text='Run Again', command=main)
        passwLabel.pack()
        passwCopy.pack()
        again.pack()
    

    def generate():
        global passwlength
        global addConfirm
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global leaveButton
        global passwButton
        optionLabel.pack_forget()
        addButton.pack_forget()
        viewButton.pack_forget()
        copyButton.pack_forget()
        searchButton.pack_forget()
        generateButton.pack_forget()
        leaveButton.pack_forget()
        passwlength = tk.Entry(window)
        passwButton = tk.Button(window, text='Generate', command=newPassw)

        passwlength.pack()
        passwButton.pack()
    
        
        

    def choice():
        global optionLabel
        global addButton
        global viewButton
        global copyButton
        global searchButton
        global generateButton
        global leaveButton
        master_pwd = pwdEntry.get()
        if master_pwd == "qwertyuiop":
            pwdEntry.pack_forget()
            pwdButton.pack_forget()
            firstLeave.pack_forget()
            optionLabel = tk.Label(window, text='Choose between one of these options')
            addButton = tk.Button(window, text='Add Login', command=add)
            viewButton = tk.Button(window, text='View Logins', command=view)
            copyButton = tk.Button(window, text='Copy Passwords', command=copy)
            searchButton = tk.Button(window, text='Search for a Login', command=search)
            generateButton = tk.Button(window, text='Generate a password', command=generate)
            leaveButton = tk.Button(window, text='Quit', command=leave)
            optionLabel.pack()
            addButton.pack()
            viewButton.pack()
            copyButton.pack()
            searchButton.pack()
            generateButton.pack()
            leaveButton.pack()
        if master_pwd != "qwertyuiop":
            denyLabel = tk.Label(window, text='Access Denied')
            denyLabel.pack()
            time.sleep(2) 
            window.destroy()

    


    global pwdEntry
    global pwdButton
    pwdEntry = tk.Entry(window, show="*")
    pwdButton = tk.Button(window, text="Enter Password: ", command=choice)
    firstLeave = tk.Button(window, text='Quit', command=leave)


    pwdEntry.pack()
    pwdButton.pack()
    firstLeave.pack()
    window.mainloop()

main()

