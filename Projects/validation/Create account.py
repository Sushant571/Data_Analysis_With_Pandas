import time
import random
myfile_2 =open('names.txt')
myfile = open('Names.txt','a')
user_input = input('Enter a Name :')
time.sleep(2)
user_input_2 = input('Enter a Mail : ')
Userask = input('Do you want to make you Mail PUBLIC or PRIVATE : ')
if Userask =='Private'or'PRIVATE':
       print('Okay we will make sure that your mail is between Hoofle and you only..')
OTP = random.randrange(5000,7000)
print(OTP)
user_input_3 = int(input('Enter OTP(OneTimePassword):'))
if user_input_3 == OTP:
       myfile.writelines(user_input + ',' + user_input_2 + '\n ')
       print('Your account was created ',user_input)

