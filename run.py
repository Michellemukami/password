#! /usr/bin/env python3

import sys
from password_locker import User,Credential

def create_user(firstname,lastname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(firstname,lastname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def del_credential(contact):
    '''
    Function to delete a credential
    '''
    credential.delete_credentails()

def verify_user(first_name,password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password
	'''
	gen_pass = generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def main():
	print(' ')
	print('Welcome to Password_Locker.')
	while True:
		print(' ')
		print("-"*50)
		print('Use these codes to navigate: \n ca-Create Account today! \n li-Log In \n ex-Exit')
		short_code = input('Your choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*50)
			print(' ')
			print('Make a new account?:')
			first_name = input('Enter first name - ').strip()
			last_name = input('Enter last name - ').strip()
			password = input('Enter password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account for: {first_name} {last_name} with the password: {password}')
		elif short_code == 'li':
			print("-"*50)
			print(' ')
			print('In order to login, enter your account information kindly:')
			user_name = input('Enter first name - ').strip()
			password = str(input('Enter password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose to continue with us.')
				print(' ')
				while True:
					print("-"*50)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n del-delete credentials \n ex-Exit')
					short_code = input('Your choice?: ').lower().strip()
					print("-"*50)
					if short_code == 'ex':
						print(" ")
						print(f'lovely day! {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential information:')
						site_name = input('Enter site\'s name- ').strip()
						account_name = input('Enter account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*50)
							print('Kindly note that this are the options for your password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Your choice?: ').lower().strip()
							print("-"*50)
							if psw_choice == 'ep':
								print(" ")
								password = input('Your password kindly?: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Sorry!.Kindly Try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print(' A display of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You seem not to have saved credentials")
							print(' ')
			
                    elif short_code == 'del':
                        print("Enter name of account to be deleted")
                        deli_user = input()
                        if check_existing_user(deli_user):
                            search_account = find_user(deli_user)
                            del_user(search_account)
                            print(f"{search_account.account} account credentials have been successfully deleted")	
		
		else:
			print("-"*50)
			print(' ')
			print('Sorry!.Kindly Try again..')
				






if __name__ == '__main__':
    main()