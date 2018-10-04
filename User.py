# User class 
class User(object):
    # empty List to hold all users
    users_list = []
    # constructor
    def __init__(self, name, email, password, confirm_password):
        # instance variables
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    # class method to save user details
    def save_user(self, user):
        User.users_list.append(user)
        return dict(
            name=User.users_list[0].name,
            email=User.users_list[0].email
        )
    
    # class method to update users details
    def update_user(self, user):
        # get the user data from database
        # make the necessary edits
        # save the data back to db
        pass