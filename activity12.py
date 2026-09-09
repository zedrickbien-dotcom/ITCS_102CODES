import getpass

username = 'dazz0914'
password = 'dazz198204156378'

u = input("enter username ----> ")
p = getpass.getpass("enter password ----> ")

if username == u and password == p :
              print("ACCESS GRANTED)
else:
              print("ACCESS DENIED)