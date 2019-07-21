import unittest
import sys.setrecursionlimit (1500)
from password_locker import User, Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviors.
    Args:
        unittest.TestCase: helps in creating test cases
    '''

    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Gitau', 'Mukami', 'kamikaze99')

    def test__init__(self):
        '''
        Test to if check creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name, 'Gitau')
        self.assertEqual(self.new_user.last_name, 'Mukami')
        self.assertEqual(self.new_user.password, 'kamikaze99')

    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviors.
    Args:
        unittest.TestCase: helps in creating test cases
    '''

    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User('Gitau', 'Mukami', 'kamikaze99')
        self.new_user.save_user()
        user2 = User('Gitau', 'Mukami', 'kamikaze99')
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
            return current_user

        self.assertEqual(current_user, Credential.check_user(
            user2.password, user2.first_name))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential(
            'Gitau', 'Linkin', 'test', 'kamikaze99')

    def test__init__(self):
        '''
        Test to if check the initialization/creation of credential instances is properly done
        '''
        self.assertEqual(self.new_credential.user_name, 'Gitau')
        self.assertEqual(self.new_credential.site_name, 'Linkin')
        self.assertEqual(self.new_credential.account_name, 'test')
        self.assertEqual(self.new_credential.password, 'kamikaze99')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Gitau', 'Twitter', 'works', 'kamikaze99')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credential.credentials_list = []
        User.users_list = []

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Gitau', 'Twitter', 'works', 'kamikaze99')
        twitter.save_credentials()
        gmail = Credential('Gitau', 'Gmail', 'send', 'pswd200')
        gmail.save_credentials()
        self.assertEqual(
            len(Credential.display_credentials(twitter.user_name)), 3)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Gitau', 'Twitter', 'works', 'kamikaze99')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists, twitter)


if __name__ == '__main__':
    unittest.main()