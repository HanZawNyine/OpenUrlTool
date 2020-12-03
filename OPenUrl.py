import webbrowser

print("your txt file of link to open WEB Broswer")
===============================================
a = input("Enter Your File (*.txt) :")
with open(a) as f:
    lines = f.readlines()
    for b in lines:
        print(b) 
        webbrowser.open(b, new=2)
