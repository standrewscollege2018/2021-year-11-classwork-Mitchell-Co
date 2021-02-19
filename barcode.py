
ask = True
while ask == True:
    code= input("What is your barcode? ")
    if len(code)!=13:
        print("ERROR")
    else:
        ask = False

country = (code[0:2])
manufacturer = (code[2:7])
product = (code[7:12])
check = (code[12:])

print("Country numbers", country, "Manufacturer numbers", manufacturer,"Product numbers", product,"Final check number", check)


