import datetime
# User class 
class User(object):
    # Empty List to hold all users
    users_list = []
    # Constructor
    def __init__(self, name, email, password, confirm_password, roles):
        # Instance variables
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.roles = roles
        self.created_at = datetime.datetime.now()

    # Class method to save user details
    def save_user(self, user):
        User.users_list.append(user)
        return dict(
            name=User.users_list[0].name,
            email=User.users_list[0].email
        )
    
    # Class method to update users details
    def update_user(self, user):
        # get the user data from database
        # make the necessary edits
        # save the data back to db
        pass

# Admin class that inherits from User class
class Admin(User):
    def __init__(self, name, email, password, confirm_password, roles):
        super(Admin, self).__init__(name=name, email=email, password=password, confirm_password=confirm_password, roles=roles)
        self.roles = 'Admin Roles'

# Contributor class that inherits from User class
class Contributor(User):
    def __init__(self, name, email, password, confirm_password, roles):
        super(Contributor, self).__init__(name=name, email=email, password=password, confirm_password=confirm_password, roles=roles)
        self.roles = 'Contributor Roles'