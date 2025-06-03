#let shave fun

print("lets play with the Print staement")
#creating a frown and smile fuction
def smile():
    print("       +          +       ")
    print("     + + +      + + +     ")
    print("       +          +       ")
    print("                          ")
    print("        +++     +++       ")
    print("         +       +        ")
    print("          + + + +         ")
    print("            +++           ")

#frown Fuction

def frown():
    print("       +          +       ")
    print("     + + +      + + +     ")
    print("       +          +       ")
    print("                          ")
    print("            +++           ")
    print("         +       +        ")
    print("        +         +       ")
    print("       +++       +++      ")

#Asking if the user is happy or not 
#TO utilize the fronw fuction
state = input(" [+] Are you Happy: Yes(y) No(n) :::  ")
if state == "y":
    smile()
elif state == "n":
    frown()
else:
    print("SORRY I DONT GET YOU: ")
    