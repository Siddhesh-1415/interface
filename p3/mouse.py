import re

code = input ("enter loc:")

tokens = re.findall(r'[a-zA-Z_]\w*|\d+|[+\-*/=()]', code)



for token in tokens:
    if re.fullmatch(r'[a-zA-Z_]\w*',token):
        print(f"{token}-> identifier")
    elif re.fullmatch(r'\d+', token):
        print(f"{token} -> number")
    elif token in "+-*/=":
         print(f"{token}-> operator")
    else :
         print(f"{token}-> unknown")
