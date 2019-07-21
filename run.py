#! /usr/bin/env python3

import pyperclip
from password_locker import User,Credential

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
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
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
	print(' ')
	print('Hello! you are Welcomed to Password_Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n A-Create an Account \n B-Log In \n X-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'X':
			break

		elif short_code == 'A':
			print("-"*60)
			print(' ')
			print('To create new account?:')
			first_name = input('Enter first name - ').strip()
			last_name = input('Enter last name - ').strip()
			password = input('Enter password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'B':
			print("-"*60)
			print(' ')
			print('login, by entering your account information:')
			user_name = input('Enter first name - ').strip()
			password = str(input('Enter password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*20)
					print('Navigation codes: \n C-Create a Credential \n D-Display Credentials \n V-Copy Password \n X-Exit')
					short_code = input('Your choice ?: ').lower().strip()
					print("-"*60)
					if short_code == 'X':
						print(" ")
						print(f'Lovely day! {user_name}')
						break
					elif short_code == 'C':
						print(' ')
						print('Enter credentials information:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*20)
							print('Please choose an option for entering a password: \n exist-enter existing password \n gene-generate a password \n X-exit')
							psw_choice = input('Your choice?: ').lower().strip()
							print("-"*20)
							if psw_choice == 'exist':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gene':
								password = generate_password()
								break
							elif psw_choice == 'X':
								break
							else:
								print(f'Try again {user_name}')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created:Your site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'D':
						print(' ')
						if display_credentials(user_name):
							print(f'This are your credentials {user_name}')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't have saved credentials")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print(' Try again.')

			else: 
				print(' ')
				print('Try again or Create an Account.')		
		
		else:
			print("-"*20)
			print(' ')
			print('Try again.')
				






if __name__ == '__main__':
    main()