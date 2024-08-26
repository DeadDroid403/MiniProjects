# program for bakery shop management
cname = []
citem = []
cprice = []
index = 0
cid = []

while True:
    print("""
            1) To add a sold item
            2) To show sales details
            3) To exit
            """)
    u = input("enter your choice number:- ")
    if u == "1":
        name = input("enter costumer name here:- ")
        cname.append(name)
        item = input("enter item name here:- ")
        citem.append(item)
        price = int(input("enter the price here:- "))
        cprice.append(price)
        index += 1
        cid.append(index)
        print()
        print("*** Item Saved Successfully ***")


    elif u == "2":

        print(f"{'costumer id':<15}{'costumer name':<15}{'item name':<15}{'price':<10}")
        for a,b,c,d in zip(cid,cname,citem,cprice):
            print(f"{a:<15}{b:<15}{c:<15}{d:<10}")

    elif u == "3":
        break

    else:
        print("your input is invalid... enter again:")
        continue
