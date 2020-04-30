import random

password_length = 15

low = ['a','b','c','d','e','f','g','h,','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up = ['A','B','C','D','E','F','G','H,','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8,','9']
sym = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','<','>','.','?','/']
options = [low, up, num, sym]

password = ''
for i in range(0, password_length):
    option_index = (random.randint(0,3))
    category = options[option_index]
    category_index = random.randint(0,len(category)-1)
    password += category[category_index]
    
print(password)
    
