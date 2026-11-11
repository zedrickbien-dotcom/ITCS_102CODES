isExpensive = True 

while isExpensive == True:
    x = bool(input("is the gas price still expensive? (True/False)"))

    if x == True:
        print("continuing loop")
        continue
    else:
        break