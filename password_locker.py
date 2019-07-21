
import random
import string 



class User:
    '''
    class to create user accounts and save their information
    '''
   
 
    users_list = []

    def __init__(self , first_name, last_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)


class Credential:
    '''
    Class to create  account credentials, generate passwords and save their information
    '''
    
    credentials_list = []
    user_credentials_list = []
    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and password entered match inputs in the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
    
        Credential.credentials_list.append(self)
    
    
    @classmethod
    def generate_Password():
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ1234567890'
        gen_pass = ''.join(random.sample(chars, 5))
        return gen_pass
        
    @classmethod
    def display_credentials(cls, user_name):
        '''
        Class method to display the list of credential saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method that takes in a site_name and returns a credentials.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

   