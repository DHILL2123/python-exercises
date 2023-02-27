with open('checkbook.rtf')as f:
    data = f.read()
currentbal = data

def balance():
    bal = float(currentbal)
print(float(currentbal))   