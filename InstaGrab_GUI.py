# Matthew Palmer 833497
# InstaGrab Program
# 21/06/2021 @ 23:45
 
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import PIL
from PIL import ImageTk, Image
import instaloader

USER = ""
PASSWORD = ""
displayUsername = ""
#############################################################################################################
class Login(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Background
        self.img = PIL.Image.open('InstaGrab_Background.png')
        self.img = self.img.resize((450, 200))
        self.photo = ImageTk.PhotoImage(self.img)
        self.imgLabel = tk.Label(image=self.photo)
        self.img.image = self.photo
        self.imgLabel.place(relx=.0,rely=.0, anchor="nw")

        # Text
        self.title = tk.Label(text="InstaGrab", fg="black", font=("Helvetica",16,"bold"), background = "white")
        self.title.place(relx=.5,rely=.18, anchor="center")

        self.text = tk.Label(text="Please Login to a Instagram Account or Continue as Guest", fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.5,rely=.3, anchor="center")

        self.text = tk.Label(text="Username:", fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.13,rely=.45, anchor="center")

        self.text = tk.Label(text="Password:", fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.13,rely=.6, anchor="center")

        # Username Entry
        self.USERvar = tk.StringVar()       
        self.entrybox = tk.Entry(textvariable=self.USERvar, bd=3, width=50)
        self.entrybox.place(relx=.55,rely=.45, anchor="center", height=24)

        self.PASSWORDvar = tk.StringVar()        
        self.entrybox = tk.Entry(textvariable=self.PASSWORDvar, bd=3, width=50, show="*")
        self.entrybox.place(relx=.55,rely=.6, anchor="center", height=24)

        self.continuebutton = tk.Button(text="Log In", fg="black", command=self.contlogin, font=("Helvetica", 9, "bold"), width=20, height=1, background="grey99", bd=1)
        self.continuebutton.place(relx=.3,rely=.8, anchor="center")

        self.continuebutton = tk.Button(text="Continue as Guest", command=self.contguest, fg="black", font=("Helvetica", 9, "bold"), width=20, height=1, background="grey99", bd=1)
        self.continuebutton.place(relx=.7,rely=.8, anchor="center")
    
    def contguest(self):
        global displayUsername
        displayUsername = "Guest"
        self.destroy()
        newframe = Frame(self.master)
    
    def contlogin(self):
        USER = self.USERvar.get()
        PASSWORD = self.PASSWORDvar.get()
        try:
            global displayUsername
            insta.login(USER, PASSWORD)
            displayUsername = USER
            self.destroy()
            newframe = Frame(self.master)
        except:
            tkinter.messagebox.showinfo("InstaGrab ERROR", "Account not Authorised")
#############################################################################################################
class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Background
        self.img = PIL.Image.open('InstaGrab_Background.png')
        self.img = self.img.resize((450, 200))
        self.photo = ImageTk.PhotoImage(self.img)
        self.imgLabel = tk.Label(image=self.photo)
        self.img.image = self.photo
        self.imgLabel.place(relx=.0,rely=.0, anchor="nw")

        # Text Boxes
        self.title = tk.Label(text="InstaGrab", fg="black", font=("Helvetica",16,"bold"), background = "white")
        self.title.place(relx=.5,rely=.18, anchor="center")

        self.text = tk.Label(text="Enter the Username of a Instagram Account", fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.5,rely=.3, anchor="center")

        self.text = tk.Label(text=("Logged in as " + str(displayUsername)), fg="grey", font=("Helvetica",6,"bold"), background = "white")
        self.text.place(relx=.965,rely=.89, anchor="e")
        
        self.text = tk.Label(text="Username:", fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.13,rely=.55, anchor="center")

        # Username Entry
        self.username = tk.StringVar()        
        self.entrybox = tk.Entry(textvariable=self.username, bd=3, width=50)
        self.entrybox.place(relx=.55,rely=.55, anchor="center", height=24)

        self.continuebutton = tk.Button(text="Continue", command=self.cont, fg="black", font=("Helvetica", 9, "bold"), width=20, height=1, background="grey99", bd=1)
        self.continuebutton.place(relx=.7,rely=.75, anchor="center")

        self.logoutbutton = tk.Button(text="Log Out", command=self.logout, fg="black", font=("Helvetica", 9, "bold"), width=20, height=1, background="grey99", bd=1)
        self.logoutbutton.place(relx=.3,rely=.75, anchor="center")

    # Functions
    def cont(self):
        try:
            global profile
            profile = instaloader.Profile.from_username(insta.context, self.username.get())
            self.destroy()
            newframe = Frame2(self.master)
        except:
            tkinter.messagebox.showinfo("InstaGrab ERROR", "User not found. Please try again")

    def logout(self):
        self.destroy()
        newframe = Login(self.master)
#############################################################################################################     
class Frame2(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Background
        self.img = PIL.Image.open('InstaGrab_Background.png')
        self.img = self.img.resize((450, 200))
        self.photo = ImageTk.PhotoImage(self.img)
        self.imgLabel = tk.Label(image=self.photo)
        self.img.image = self.photo
        self.imgLabel.place(relx=.0,rely=.0, anchor="nw")

        # Info
        self.text = tk.Label(text=("Username: " +  str(profile.username)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.15, anchor="w")

        self.text = tk.Label(text=("User ID: " +  str(profile.userid)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.25, anchor="w")

        self.text = tk.Label(text=("Post Count: " +  str(profile.mediacount)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.35, anchor="w")

        self.text = tk.Label(text=("IGTV Count: " +  str(profile.igtvcount)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.45, anchor="w")

        self.text = tk.Label(text=("Followers: " +  str(profile.followers)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.55, anchor="w")

        self.text = tk.Label(text=("Followees: " +  str(profile.followees)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.65, anchor="w")

        self.text = tk.Label(text=("Full Name: " +  str(profile.full_name)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.75, anchor="w")

        self.text = tk.Label(text=("Verified: " +  str(profile.is_verified)), fg="black", font=("Helvetica",9,"bold"), background = "white")
        self.text.place(relx=.04,rely=.85, anchor="w")

        self.text = tk.Label(text=("Logged in as " + str(displayUsername)), fg="grey", font=("Helvetica",6,"bold"), background = "white")
        self.text.place(relx=.965,rely=.89, anchor="e")

        self.pfpbutton = tk.Button(text="Download Profile Pic", command=self.download_pfp, fg="black", font=("Helvetica", 9, "bold"), width=18, height=1, background="grey99", bd=1)
        self.pfpbutton.place(relx=.8,rely=.3, anchor="center")

        self.postbutton = tk.Button(text="Download Posts", command=self.download_posts, fg="black", font=("Helvetica", 9, "bold"), width=18, height=1, background="grey99", bd=1)
        self.postbutton.place(relx=.8,rely=.45, anchor="center")    

        self.storybutton = tk.Button(text="Download Highlights", command=self.download_stories, fg="black", font=("Helvetica", 9, "bold"), width=18, height=1, background="grey99", bd=1)
        self.storybutton.place(relx=.8,rely=.6, anchor="center")    

        self.backbutton = tk.Button(text="Back", command=self.back, fg="black", font=("Helvetica", 9, "bold"), width=18, height=1, background="grey99", bd=1)
        self.backbutton.place(relx=.8,rely=.75, anchor="center")

    def download_posts(self):
        posts = profile.get_posts()
        for post in posts:
            insta.download_post(post,target=f"{profile.username}")
            
    def download_stories(self):
        highlights = insta.get_highlights(profile.userid)
        insta.download_highlights(user=profile.userid)
        
    def download_pfp(self):
        insta.download_profile(profile.username, profile_pic_only=True)

    def back(self):
        self.destroy()
        newframe = Frame(self.master)

#############################################################################################################    
insta = instaloader.Instaloader()
root = tk.Tk()
app = Login(root) 
root.wm_title("InstaGrab") 
root.iconbitmap('InstaGrab_Logo.ico')
root.geometry("450x200")
#root.protocol("WM_DELETE_WINDOW", lambda: print("lol"))
#root.wm_attributes("-topmost", 1)
#root.wm_attributes("-disabled", True)
#root.wm_attributes('-transparentcolor', root['bg'])
#root.wm_attributes('-toolwindow', 1)
root.resizable(False, False)
root.mainloop()
