import webbrowser

print("your txt file of link to open WEB Broswer")
print("===============================================")
a = input("Enter Your File (*.txt) :")
with open(a) as f:
    lines = f.readlines()
    for b in lines:
        print(b) 
        webbrowser.open(b, new=2)
print("Developed by h4n24wny!n3")
