from controllers import user_controller, role_controller
from main_screen import MainScreen

# active_user = ""
# is_admin = False

def verifyUser(username,password):
    #username, password = "Admin", "P4ssw0rd"
    username,password = username.rstrip(),password.rstrip()
    result = user_controller.VerifyUser(username,password)
    if not result:
        return False
    elif result:
        if result[0][2] == 1:
            is_admin = True
        #MainScreen.IsAdmin({ "data": result[0], "admin" : is_admin})


def compileDataForNewUserEntry(data):
    data["role"] = role_controller.getRoleIdFromName(data["Role"])
    data["Username"] = data["Username"][:30]
    data["Password"] = data["Passwrod"][:20]
    user_controller.addNewUser(data)