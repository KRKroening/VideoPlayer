import tkinter as tk
from controllers import episode_controller, category_controller
from managers import user_manager




class MainScreen():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('{}x{}'.format(int(self.root.winfo_screenwidth()*0.9),int(self.root.winfo_screenheight()*0.8)))

        self.toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.adminbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        self.adminbar.pack(side=tk.BOTTOM, fill=tk.X)


        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)

        self.PopulateAdminBar()
        self.MostRecentEpisodes()
        self.ListAllCategories()


        self.root.mainloop()

    def MostRecentEpisodes(self):
        recents = episode_controller.listRecentEpisodes()
        for epi in recents:
            test = tk.Label(self.root, text=epi["Name"])
            test.pack()

    def ListAllCategories(self):
        recents = category_controller.listAllCategories()
        for cat in recents:
            test = tk.Button(self.toolbar,
                             text=cat[1],
                             command=lambda i=cat[0]:self.SendToGenreListing(i)
                             )
            test.neededVar = cat[0]
            test.pack(side=tk.LEFT)

    def PopulateAdminBar(self):
        login = tk.Button(self.adminbar,
                         text="Sign In",
                         command=lambda: self.LoginWindow()
                         )
        login.pack(side=tk.LEFT)
        admin = tk.Button(self.adminbar,
                          text="System Controls",
                          command=lambda: self.adminControls(),
                          state="disabled"
                          )
        admin.pack(side=tk.LEFT)

    def SendToGenreListing(self, id):
        self.body.destroy()
        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)

        test = tk.Label(self.body,text=id)
        test.pack()

    def LoginWindow(self):
        popup = tk.Toplevel(self.root)
        usernameLabel = tk.Label(popup, text="Username")
        usernameLabel.pack()
        usernameBox = tk.Text(popup,height=1,width=40)
        usernameBox.pack()
        passwordLabel = tk.Label(popup, text="Password")
        passwordLabel.pack()
        passwordBox = tk.Text(popup, height=1, width=40)
        passwordBox.pack()

        submit= tk.Button(popup,text="Log In",
                          # command= lambda : user_manager.verifyUser(str(usernameBox.get("1.0",tk.END)),str(passwordBox.get("1.0",tk.END)))
                          command=lambda: user_manager.verifyUser("Admin","P4ssw0rd")

                          )
        submit.pack()

    def IsAdmin(self, data):
        if data:
            if data["admin"]:
                self.adminbar.children.values()["admin"]["state"] = 'normal'

    def adminControls(self):
        self.body.destroy()
        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)

        series_frame = tk.Frame(self.body,width=int(self.root.winfo_screenwidth()*.25),height=int(self.root.winfo_screenheight()))
        episode_frame = tk.Frame(self.body,width=int(self.root.winfo_screenwidth()*.25),height=int(self.root.winfo_screenheight()))
        category_frame = tk.Frame(self.body,width=int(self.root.winfo_screenwidth()*.25),height=int(self.root.winfo_screenheight()))
        user_frame = tk.Frame(self.body,width=int(self.root.winfo_screenwidth()*.25),height=int(self.root.winfo_screenheight()))

        s_nameLabel = tk.Label(series_frame, text="Name")
        s_nameLabel.pack()
        s_nameBox = tk.Text(series_frame, height=1, width=40)
        s_nameBox.pack()
        s_categoryLabel = tk.Label(series_frame, text="Name")
        s_categoryLabel.pack()
        s_var = tk.StringVar()
        category_options = category_controller.listAllCategories()
        s_categoryDD = tk.OptionMenu(series_frame, s_var, category_options )
        s_categoryDD.pack()



MainScreen()