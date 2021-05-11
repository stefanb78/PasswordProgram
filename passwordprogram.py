def Get_Password():
    return input("Enter your desired password: ")

def Count_Digits(password):
    return sum(character.isdigit() for character in password)

def Valid_password_length(password):
    if len(password) >= 8:
        return True
    else:
        print("Invalid password: too short")
        return False

def Valid_password_characters(password):
    if password.isalnum():
        return True
    else:
        print("Invalid password: illegal character detected")
        return False

def Valid_password_numdigit(password):
    if Count_Digits(password) >= 2:
        return True
    
    print("Invalid password: Must have at least 2 digits")
    return False
        
        
def Valid_password_lowercase(password):
    for i in password:
        if i.islower():
            return True
        else:
            continue
        
    print("Invalid password: No lowercase characters detected")
    return False
    
def Valid_password_uppercase(password):
    for i in (password):
        if i.isupper():
            return True
        else:
            continue
            
    print("Invalid password: No uppercase characters detected")
    return False
        
def password_checker():
    password = Get_Password()
    step1 = Valid_password_length(password)
    step2 = Valid_password_characters(password)
    step3 = Valid_password_numdigit(password)
    step4 = Valid_password_lowercase(password)
    step5 = Valid_password_uppercase(password)

    if step1 and step2 and step3 and step4 and step5:
        print("Congratulations! This password is valid")
        return password

#'r' represents read only files
with open ('hwcompsci.txt', 'r') as usrlist:
    lines = usrlist.readlines()

    store_username=[]
    store_password=[]
 
    
    #Splits lines into seperate variables and uses indexes to assign them variables
    #line.split is the variable for the list of username and passwords

    for line in lines:
        line_split = line.strip('\n').split()
        print(line_split)
        username = line_split[0]
        password = line_split[1]    
        store_username.append(username)
        store_password.append(password)

# 'len' prints length of the list
print(len(store_username))
print(len(store_password))

while True:
        
    username = input("Please create a username: \n")
        
    if username in store_username:
        print("[!] That user already exists \n")
        login=input("Would you like to log in? Y/N \n")
        
        if login.upper() == "N":
            continue
        elif login.upper() == "Y":
            print("Logging in... \n")
    
    password = password_checker()
    
    # The username and password are assigned to the store_username and store_password lists
    store_username.append(username)
    store_password.append(password)
    
    # variables are stored to hwcompsci.txt file
    with open ('hwcompsci.txt', 'a') as usrlist:
        usrlist.write(f"\n{username:s} {password:s}")
    
    condition=input("Would you like to create another user?: Y/N \n")
    if condition.upper() == "Y":
        continue
    elif condition.upper() == "N":
        break
