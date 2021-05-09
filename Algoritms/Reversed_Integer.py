x = input('Enter Number : ')
minLimit = -2**31
maxLimit = 2**31

numStr = str(x) #Conversion
numStr = numStr[::-1] #Reverse digits
print('The Reversed Number is '+numStr)
last_number = numStr[::1]
if last_number == '-':
    print('The Reversed number is '+'-'+numStr)
