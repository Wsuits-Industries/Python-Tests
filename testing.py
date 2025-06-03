password = ""
attemps = 0
correct_password = "root"
#Cheking if password is Correct Using A while loop
while password != correct_password:
    password = input("[+] Input the Pasword TO loogin:     ")
    attemps += 1

print(f"[!] Access Granted after {attemps} Attemps")



