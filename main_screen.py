import tkinter as tk
from controllers import episode_controller, category_controller, series_controller, role_controller
from managers import user_manager, episode_manager, series_manager, category_manager
import util




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
        self.body.destroy()
        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)
        recents = episode_controller.listRecentEpisodes()
        if not recents:
            test = tk.Label(self.body, text="No Episodes Found")
            test.pack()
        else:
            for epi in recents:
                test = tk.Label(self.body, text=epi[0])
                test.pack()

    def ListAllCategories(self):
        for widget in self.toolbar.winfo_children():
            widget.destroy()
        home = tk.Button(self.toolbar,
                  text="Home",
                  command=lambda: self.MostRecentEpisodes()
                  )
        home.pack(side=tk.LEFT)
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
                          #state="disabled"
                          )
        admin.pack(side=tk.LEFT)

    def SendToGenreListing(self, id):
        self.body.destroy()
        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)

        genre = category_controller.getCategoryNameById(id)
        label = tk.Label(self.body, text=genre)
        label.pack(side=tk.TOP)

        listing = series_controller.listSeriesByCategory(id)
        for l in listing:
            inv_frame = tk.Frame(self.body)
            inv_frame.pack(side=tk.TOP)
            name = tk.Button(inv_frame,text=l[0], command= lambda i = l[0]: self.openSeriesPage(i))
            name.pack(side=tk.LEFT)
            desc = tk.Label(inv_frame, text=l[1])
            desc.pack(side=tk.LEFT)

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
                          command=lambda: user_manager.verifyUser("Admin", "P4ssw0rd")

                          )
        submit.pack()

    def IsAdmin(self, data):
        pass
        # if data:
        #     if data["admin"]:
        #         self.adminbar.children.values()["admin"]["state"] = 'normal'

    def adminControls(self):
        self.body.destroy()
        self.body = tk.Frame(self.root)
        self.body.pack(side=tk.TOP, fill=tk.X)

        series_frame = tk.Frame(self.body,name="series_frame", width=int(self.root.winfo_screenwidth()*.5),height=int(self.root.winfo_screenheight()*.5),borderwidth=2,relief=tk.GROOVE)
        series_frame.pack(side=tk.LEFT)
        episode_frame = tk.Frame(self.body,name="episode_frame", width=int(self.root.winfo_screenwidth()*.5),height=int(self.root.winfo_screenheight()*.5),borderwidth=2,relief=tk.GROOVE)
        episode_frame.pack(side=tk.LEFT)
        category_frame = tk.Frame(self.body,name="category_frame", width=int(self.root.winfo_screenwidth()*.5),height=int(self.root.winfo_screenheight()*.5),borderwidth=2,relief=tk.GROOVE)
        category_frame.pack(side=tk.LEFT)
        user_frame = tk.Frame(self.body,name="user_frame", width=int(self.root.winfo_screenwidth()*.5),height=int(self.root.winfo_screenheight()*.5),borderwidth=2,relief=tk.GROOVE)
        user_frame.pack(side=tk.LEFT)

        #region Series widgets
        s_title = tk.Label(series_frame, name="series_frame", text="Create New Series")
        s_title.pack()
        s_nameLabel = tk.Label(series_frame, text="Name")
        s_nameLabel.pack()
        s_nameBox = tk.Text(series_frame, name="s_nameBox", height=1, width=40)
        s_nameBox.pack()
        s_categoryLabel = tk.Label(series_frame, text="Category")
        s_categoryLabel.pack()
        s_var = tk.StringVar()
        category_options = category_controller.listAllCategories()
        category_options = util.returnDropDownList(category_options,1)
        s_categoryDD = tk.Listbox(series_frame, name="s_categoryDD", listvariable=s_var, selectmode=tk.MULTIPLE, width=20, height=10)
        for item in category_options:
            s_categoryDD.insert(tk.END, item)
        s_categoryDD.pack()
        s_descriptionLabel = tk.Label(series_frame, text="Description")
        s_descriptionLabel.pack()
        s_descriptionText = tk.Text(series_frame, name="s_descriptionText", height=1,width=40)
        s_descriptionText.pack()
        s_submit = tk.Button(series_frame,text="Submit",command= lambda : self.submitNewSeries())
        s_submit.pack()
        #endregion

        #region Episode Widgets
        e_title = tk.Label(episode_frame, text="Create New Episode")
        e_title.pack()
        e_nameLabel = tk.Label(episode_frame, text="Name")
        e_nameLabel.pack()
        e_nameBox = tk.Text(episode_frame, name="e_nameBox", height=1, width=40)
        e_nameBox.pack()
        e_seriesLabel = tk.Label(episode_frame, text="Series")
        e_seriesLabel.pack()
        e_var = tk.StringVar()
        e_var.set("Select")
        series_options = series_controller.listAllSeries()
        series_options = util.returnDropDownList(series_options,1)
        e_seriesDD = tk.OptionMenu(episode_frame, e_var, *series_options)
        e_seriesDD.pack()
        e_descriptionLabel = tk.Label(episode_frame, text="Description")
        e_descriptionLabel.pack()
        e_descriptionText = tk.Text(episode_frame,name="e_descriptionText", height=1, width=40)
        e_descriptionText.pack()
        e_episodeNumberLabel = tk.Label(episode_frame, text="Episode Number")
        e_episodeNumberLabel.pack()
        e_episodeNumberText = tk.Text(episode_frame, name="e_episodeNumberText", height=1, width=3)
        e_episodeNumberText.pack()
        e_seasonNumberLabel = tk.Label(episode_frame, text="season Number")
        e_seasonNumberLabel.pack()
        e_seasonNumberText = tk.Text(episode_frame, name="e_seasonNumberText", height=1, width=3)
        e_seasonNumberText.pack()
        e_locationLabel = tk.Label(episode_frame, text="File Name")
        e_locationLabel.pack()
        e_locationText = tk.Text(episode_frame, name="e_locationText", height=1, width=50)
        e_locationText.pack()
        e_submit = tk.Button(episode_frame, text="Submit", command=lambda: self.submitNewEpisode(e_var))
        e_submit.pack()
        #endregion

        #region Category Widgets
        c_title = tk.Label(category_frame, name="category_frame", text="Create New Category")
        c_title.pack()
        c_nameLabel = tk.Label(category_frame, text="Description")
        c_nameLabel.pack()
        c_nameBox = tk.Text(category_frame, name="c_nameBox", height=1, width=40)
        c_nameBox.pack()
        c_submit = tk.Button(category_frame,text="Submit",command= lambda : self.submitNewCategory())
        c_submit.pack()

        #endregion

        #region User Widgets
        u_title = tk.Label(user_frame, name="user_frame", text="Create New User")
        u_title.pack()
        u_usernameLabel = tk.Label(user_frame, text="Username")
        u_usernameLabel.pack()
        u_usernameBox = tk.Text(user_frame, name="u_usernameBox", height=1, width=40)
        u_usernameBox.pack()
        u_passwordLabel = tk.Label(user_frame, text="Password")
        u_passwordLabel.pack()
        u_passwordBox = tk.Text(user_frame, name="u_passwordBox", height=1, width=40)
        u_passwordBox.pack()
        u_roleLabel = tk.Label(user_frame, text="Role")
        u_roleLabel.pack()
        u_var = tk.StringVar()
        u_var.set("Select")
        role_options = role_controller.listAllRoles()
        role_options = util.returnDropDownList(role_options,0)
        u_roleDD = tk.OptionMenu(user_frame, u_var, *role_options)
        u_roleDD.pack()
        u_submit = tk.Button(user_frame, text="Submit", command=lambda: self.submitNewUser(u_var))
        u_submit.pack()

        #endregion

    def submitNewEpisode(self, e_var):
        frame = self.body.children["episode_frame"]
        e_seriesDD = e_var.get()
        dropdown = ""
        for widget in frame.winfo_children():
            if isinstance(widget, tk.OptionMenu):
                dropdown = widget

        data = {
            "Name" : frame.children["e_nameBox"].get("1.0",tk.END).rstrip(),
            "Series" : e_seriesDD,
            "Description" : frame.children["e_descriptionText"].get("1.0",tk.END).rstrip(),
            "EpisodeNumber" : int(frame.children["e_episodeNumberText"].get("1.0",tk.END).rstrip()),
            "SeasonNumber" : int(frame.children["e_seasonNumberText"].get("1.0",tk.END).rstrip()),
            "FileLocation" : frame.children["e_locationText"].get("1.0",tk.END).rstrip(),
            "DateAdded" : ""

        }

        episode_manager.compileDataForNewEpisodeEntry(data)

        frame.children["e_nameBox"].delete("1.0", tk.END)
        frame.children["e_descriptionText"].delete("1.0", tk.END)
        frame.children["e_episodeNumberText"].delete("1.0", tk.END)
        frame.children["e_seasonNumberText"].delete("1.0", tk.END)
        frame.children["e_locationText"].delete("1.0", tk.END)
        e_var.set("Select")

    def submitNewSeries(self):
        frame = self.body.children["series_frame"]
        e_categoryDD = []
        listbox = ""
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Listbox):
                t = widget.curselection()
                listbox = widget
                for item in t:
                    e_categoryDD.append(widget.get(item))
        data = {
            "Name": frame.children["s_nameBox"].get("1.0", tk.END).rstrip(),
            "Category": e_categoryDD,
            "Description": frame.children["s_descriptionText"].get("1.0", tk.END).rstrip(),
        }

        series_manager.compileNewSeriesData(data)

        #clear fields
        frame.children["s_nameBox"].delete('1.0', tk.END)
        frame.children["s_descriptionText"].delete("1.0", tk.END)
        listbox.selection_clear(0, tk.END)

    def submitNewCategory(self):
        frame = self.body.children["category_frame"]

        data = {
            "Description": frame.children["c_nameBox"].get("1.0", tk.END).rstrip(),
        }
        category_manager.compileDataForNewCategoryEntry(data)

        frame.children["c_nameBox"].delete("1.0", tk.END)
        self.ListAllCategories()

    def submitNewUser(self,u_var):
        frame = self.body.children["user_frame"]
        u_role_selected = u_var.get()
        dropdown = ""
        for widget in frame.winfo_children():
            if isinstance(widget, tk.OptionMenu):
                dropdown = widget

        data = {
            "Username": frame.children["u_usernameBox"].get("1.0", tk.END).rstrip(),
            "Password" : frame.children["u_passwordBox"].get("1.0", tk.END).rstrip(),
            "Role" : u_role_selected
        }
        user_manager.compileDataForNewUserEntry(data)

        frame.children["u_usernameBox"].delete("1.0", tk.END)
        frame.children["u_passwordBox"].delete("1.0", tk.END)

MainScreen()