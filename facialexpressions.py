
# Let's have fun

print("Welcome to the Fun Program!")
print("This program will display a smiley or frown face based on your input.")

# Creating a smile function
def happy():
    print("     +\"\"\"\"\"+     ")
    print("   [  o   o  ]   ")
    print("   |    ^    |   ")
    print("   |  \\___/  |   ")
    print("    +_______+    ")

# Creating a frown function
def sad():
    print("       +\"\"\"\"\"+       ")
    print("     [  o   o  ]     ")
    print("     |    ^    |     ")
    print("     |   ___   |     ")
    print("     |  /   \\  |     ")
    print("      +_______+      ")
    print("     /         \\    ")
    print("    /           \\   ")
    print("   +-------------+  ")

def angry():
    print("     +\"\"\"\"\"+     ")
    print("   [  >   <  ]   ")
    print("   |    ~    |   ")
    print("   |  _____  |   ")
    print("    +_______+    ")

def surprised():
    print("     +\"\"\"\"\"+     ")
    print("   [  O   O  ]   ")
    print("   |    o    |   ")
    print("   |   ___   |   ")
    print("    +_______+    ")

def neutral():
    print("     +\"\"\"\"\"+     ")
    print("   [  o   o  ]   ")
    print("   |    -    |   ")
    print("   |  _____  |   ")
    print("    +_______+    ")

def cool():
    print("     +\"\"\"\"\"+     ")
    print("   [  B   B  ]   ")
    print("   |    ^    |   ")
    print("   |  \\___/  |   ")
    print("    +_______+    ")

def crying():
    print("     +\"\"\"\"\"+     ")
    print("   [  o   o  ]   ")
    print("   |    ~    |   ")
    print("   |  \\___/  |   ")
    print("   |  /   \\  |   ")
    print("  /         \\  ")
    print(" /    '''    \\ ")
    print("+-------------+")

def silly():
    print("     +\"\"\"\"\"+     ")
    print("   [  o   o  ]   ")
    print("   |    ~    |   ")
    print("   |  \\___/  |   ")
    print("   |   ---   |   ")
    print("    +_______+    ")

#===============================
#===============================
    


while True:

    faceToCHoice = input("""
============================|
[+] What face should I make |
[+] Silly Face          (si)|
[+] crying face         (cr)|
[+] cool face           (co)|
[+] Nuetral Face        (nu)|
[+] Surprosed Face      (su)|
[+] Angry Face          (an)|
[+] Sad Face            (sa)|
============================|
                         [+] :::::
""")
    #Conditional Statement for Input
    #===============================
    #===============================
    
    if faceToCHoice   == "si":
        silly()
    elif faceToCHoice == "cr":
        crying()
    elif faceToCHoice == "o":
        cool()
    elif faceToCHoice == "nu":
        neutral()
    elif faceToCHoice == "su":
        surprised()
    elif faceToCHoice == "an":
        angry()
    elif faceToCHoice == "sa":
        sad()
    else:
        print("[-] I dont understan follow the Input Format")