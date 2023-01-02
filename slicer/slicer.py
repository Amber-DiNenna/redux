# collect email from user
# split email using the @, the first part as the user name, the second part as domain
# split domain using the .


def main():
  print('''
  Welcome to the Email Slicer
  ''')

  email_input = input('Enter your email address: ')

  (username, domain) = email_input.split('@')
  (domain, extension) = domain.split('.')

  print(f'''
  Username: {username}
  Domain: {domain}
  Extension: {extension}
  ''')

main()
