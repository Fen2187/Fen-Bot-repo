import random
import time 
#ip generator system

ip1g = random.randint(10, 40)
ip2g = random.randint(1, 9)
ip3g = random.randint(0, 10)
ip4g = random.randint(0, 11)

ip = str(ip1g) + '.' + str(ip2g) + '.' + str(ip3g) + '.' + str(ip4g)

# start up
user1 = 'amycool45'
user2 = 'puzzleguyFR'
user3 = 'random_guy69'
user4 = 'idk1234cv53idk34'

us = random.randint(1, 4)

if us == 1:
  user = user1

if us == 2:
  user = user2

if us == 3:
  user = user3

if us == 4:
  user = user4

#password gerenratior
pas1 = random.randint(10, 100)
pas2 = random.randint(10, 100)
pas3 = random.randint(10, 100)

passwor = random.randint(1, 4)
print(passwor)

if passwor == 1:
  password = str(pas1) + user1 + str(pas3) + str(pas1) + user1

if passwor == 2:
  password = str(pas1) + user2 + str(pas3) + str(pas3) + user2

if passwor == 3:
  password = str(pas1) + user3 + str(pas3) + str(pas1) + user3

if passwor == 4:
  password = str(pas1) + user4 + str(pas3) + str(pas1) + user4

print(ip)

#password hash
hash = user + str(ip3g) + password + user + str(ip4g) + str(
  ip2g) + password + str(ip1g)

print(hash)

#files

main_drive = '''Os    logs
User_data

'''

print(main_drive)

Os = 'System  pplications  privacy  runtime'
logs = 'server_time  server_update  server_leaks  server_attackes'
User_data = 'password_hashes  user_hashes  email_hashes  decription_keys'
