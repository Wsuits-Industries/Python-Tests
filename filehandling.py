#reading all file
# with open("test.txt","r") as textfile:
#     content = textfile.read()
#     print(content)

#Reading Line by Line
# with open("test.txt","r") as f:
#     for line in f:
#         print("THIS IS A LINE  >>>" + line.strip())

#Reading Specific bytes
# with open("vuln_ctf.bin","rb") as f:
#     payload = f.read(10)
#     print(payload)

#Overwriting ffile contents
# with open("test.txt","w") as f:
#     f.write("THIS IS OVER WRITTEN! \n")
    
#Appending Contents Adding 
# with open("test.txt", "a") as f:
#     a = 2
#     while a == 2 in range(10):
#         f.write("Still in the loop...\n")
#         break

#FILE CHECKS (BEFORE TOUCHING IT)
# import os

# if os.path.exists("payload.txt"):
#     print("FILE EXIST")
# else:
#     print("404: NOT found")

