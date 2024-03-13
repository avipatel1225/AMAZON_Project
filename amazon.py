#Amazon Project

regs_buy=[]
regs_sell=[]
products=[]
prod_id=0
cart=[]

while True:
    print("-----------------------")
    print("| Enter 1: For Buyer  |")
    print("| Enter 2: For Seller |")
    print("| Enter 0: To Exit    |")
    print("-----------------------")
    ch=int(input("Enter the choice:"))
    
    if ch!=0:
        if ch==1:
            print()
            print("||Welcome Buyers||")           
            while True:
                print("\t------------------------")
                print("\t| Enter 1: To Register |")
                print("\t| Enter 2: To Login    |")
                print("\t| Enter 0: To Go Back  |")
                print("\t------------------------")
                ch1=int(input("Enter the choice:"))
                
                if ch1!=0:
                    if ch1==1:
                        print()
                        print("||Registration||")                
                        reg={}
                        name=input("Enter your name:")
                        reg["name"]=name
                        last_name=input("Enter your last name:")
                        reg["last_name"]=last_name
                        mobile=int(input("Enter your phone number:"))
                        for i in regs_buy:
                            if i["mobile"]==mobile:
                                reg["mobile"]=0
                                print("Phone number already exist")
                                break
                        else:
                            reg["mobile"]=mobile
                        email=input("Enter your email:")
                        for j in regs_buy:
                            if j["email"]==email:
                                reg["email"]="NULL"
                                print("Email already exist")
                                break
                        else:
                            reg["email"]=email                     
                        password=input("Enter your password:")
                        reg["password"]=password
                        confirm_password=input("Confirm your password:")  
                        if password==confirm_password:
                            reg["confirm_password"]=confirm_password
                            regs_buy.append(reg)                        
                        else:
                            print("Confirm Password does not match with Password")                        
                    elif ch1==2:
                        print()
                        print("||Login||")                 
                        if len(regs_buy)!=0:
                            print("\t\t--------------------------------")
                            print("\t\t| Enter 1:Login through Mobile |")
                            print("\t\t| Enter 2:Login through Email  |")
                            print("\t\t--------------------------------")
                            ch2=int(input("Enter the choice:"))
                            
                            func=0
                            if ch2==1:
                                func=0
                                print()
                                print("||Login through Mobile||")                  
                                login_mobile=int(input("Enter your phone number:"))
                                flag=1
                                for i in regs_buy:
                                    if i["mobile"]==login_mobile:
                                        flag=2
                                        login_password=input("Enter your password:")
                                        if i["password"]==login_password:
                                            print("Login successfull")
                                            func=1
                                        else:
                                            print("Password not matched")
                                if flag==1:
                                    print("Phone number not found")
                            elif ch2==2:
                                func=0
                                print()
                                print("||Login through Email||")                  
                                login_email=input("Enter your Email:")
                                flag=1
                                for i in regs_buy:
                                    if i["email"]==login_email:
                                        flag=2
                                        login_password=input("Enter your password:")
                                        if i["password"]==login_password:
                                            print("Login successfull")
                                            func=1
                                        else:
                                            print("Password not matched")
                                if flag==1:
                                    print("Email not found")
                            else:
                                print("Invalid choice")
                                
                            if func==1:
                                print()
                                while True:
                                    print("\t\t\t---------------------------------")
                                    print("\t\t\t| Enter 1: Display All Products |")
                                    print("\t\t\t| Enter 2: Low To High          |")
                                    print("\t\t\t| Enter 3: High To Low          |")
                                    print("\t\t\t| Enter 4: Category             |")
                                    print("\t\t\t| Enter 5: Go To Cart           |")
                                    print("\t\t\t| Enter 6: Help                 |")
                                    print("\t\t\t| Enter 0: To Go Back           |")
                                    print("\t\t\t---------------------------------")
                                    ch3=int(input("Enter the choice:"))
                                    
                                    if ch3!=0:
                                        if ch3==1:
                                            print("||All Products||")
                                            print()
                                            print("Product:")
                                            if len(products)!=0:
                                                for i in products:
                                                    print("Name:",i["prod_name"])
                                                    print("Category:",i["prod_category"])
                                                    print("Price:",i["prod_price"])
                                                    print("Desc:",i["prod_desc"])
                                                    print("ID:",i["ID"])
                                                    print()
                                            else:
                                                print("No Products")
                                        elif ch3==2:
                                            print("||Low To High||")
                                            print()
                                            price1=[]
                                            for i in products:
                                                price1.append(i["prod_price"])                                     
                                            price1.sort()
                                            print("Products:")
                                            if len(products)!=0:
                                                for j in price1:
                                                    for i in products:
                                                        if j==i["prod_price"]:
                                                            print("Name:",i["prod_name"])
                                                            print("Category:",i["prod_category"])
                                                            print("Price:",i["prod_price"])
                                                            print("Desc:",i["prod_desc"])
                                                            print("ID:",i["ID"])
                                                            print()
                                            else:
                                                print("No Products")
                                        elif ch3==3:
                                            print("||High To Low||")
                                            print()
                                            price2=[]
                                            for i in products:
                                                price2.append(i["prod_price"])                                     
                                            price2.sort(reverse = True)
                                            print("Products:")
                                            if len(products)!=0:
                                                for j in price2:
                                                    for i in products:
                                                        if j==i["prod_price"]:
                                                            print("Name:",i["prod_name"])
                                                            print("Category:",i["prod_category"])
                                                            print("Price:",i["prod_price"])
                                                            print("Desc:",i["prod_desc"])
                                                            print("ID:",i["ID"])
                                                            print()
                                            else:
                                                print("No Products")
                                        elif ch3==4:
                                            print("||Category||")
                                            print()
                                            '''while True:
                                                print("\t\t\t\t---------------------------")
                                                print("\t\t\t\t| Enter 1: Dairy Products |")
                                                print("\t\t\t\t| Enter 2: Electronics    |")
                                                print("\t\t\t\t| Enter 3: Clothes        |")
                                                print("\t\t\t\t| Enter 4: Beauty         |")
                                                print("\t\t\t\t| Enter 5: Furniture      |")
                                                print("\t\t\t\t| Enter 6: Pharmacy       |")
                                                print("\t\t\t\t| Enter 7: Books/Toys     |")
                                                print("\t\t\t\t| Enter 0: Go To Back     |")
                                                print("\t\t\t\t---------------------------")
                                                ch4=int(input("Enter the choice:"))
                                                
                                                if ch4!=0:
                                                    if ch4==1:
                                                        print("||Dairy Products||")
                                                    elif ch4==2:
                                                        print("||Electronic||")
                                                    elif ch4==3:
                                                        print("||Clothes||")
                                                    elif ch4==4:
                                                        print("||Beauty||")
                                                    elif ch4==5:
                                                        print("||Furniture||")
                                                    elif ch4==6:
                                                        print("||Pharmacy||")
                                                    elif ch4==7:
                                                        print("||Books/Toys||")
                                                    else:
                                                        print("Invalid choice")
                                                else:
                                                    break'''
                                            category={}    
                                            k=0
                                            duplicate=0
                                            for i in products:
                                                for j in category.values():
                                                    if i["prod_category"]==j:                                                                                                           
                                                        duplicate=1
                                                        break
                                                    if duplicate==0:
                                                        k=k+1
                                                        category[k]=i["prod_category"]
                                                        break
                                                else:
                                                    k=k+1
                                                    category[k]=i["prod_category"]  
                                            
                                            while True:
                                                if len(category)!=0: 
                                                    print("\t---------------------------")
                                                    for i in category.items():                                                        
                                                        print("\t| Enter",end=" ")
                                                        print(i[0],":",sep="",end=" ")
                                                        print(i[1])
                                                    print("\t| Enter 0: Go To Back")
                                                    print("\t---------------------------")
                                                    ch4=int(input("Enter the choice:"))
                                                    
                                                    the_category="No"
                                                    useless=0
                                                    if ch4!=0:                                                        
                                                        for i in category.items():
                                                            if i[0]==ch4:
                                                                the_category=i[1]
                                                                break
                                                        else:
                                                            print("Invalid choice\n")
                                                            useless=-1
                                                            
                                                        if useless==0:
                                                            print("||",the_category,"Products ||")
                                                            no=0
                                                            name=[]
                                                            print("\t---------------------------")
                                                            for i in products:
                                                                if i["prod_category"]==the_category:                                                    
                                                                    no=no+1
                                                                    print("\tProduct ",no," Name: ",i["prod_name"],sep="")  
                                                                    name.append(i["prod_name"])                                                   
                                                            print("\t---------------------------")                                                        
                                                            while True:
                                                                ch_name=input("Enter Product name for Purchase:")                                                        
                                                                if ch_name in name:
                                                                    for i in products:
                                                                        if i["prod_name"]==ch_name:
                                                                            print()
                                                                            print("Name:",i["prod_name"])
                                                                            print("Category:",i["prod_category"])
                                                                            print("Price:",i["prod_price"])
                                                                            ch_price=i["prod_price"]
                                                                            print("Desc:",i["prod_desc"])
                                                                            print("ID:",i["ID"])
                                                                            print()
                                                                    while True:
                                                                        ch_quantity=int(input("Enter the Quantity of Product:"))
                                                                        if ch_quantity>0:
                                                                            Total=ch_price*ch_quantity
                                                                            print("Total Amount:",Total)
                                                                                       
                                                                            yes_no=input("Do you want to Add to Cart(yes/no):")
                                                                            if yes_no=="yes":
                                                                                for i in products:
                                                                                    if i["prod_name"]==ch_name:
                                                                                        i["prod_quantity"]=ch_quantity
                                                                                        i["prod_Total"]=Total
                                                                                        cart.append(i)
                                                                                        print("Product Added To CART")
                                                                            break
                                                                        else:
                                                                            print("Invalid Quantity")
                                                                    break
                                                                else:
                                                                    print("Invalid Name")
                                                                    print()
                                                    else:
                                                        break
                                                else:
                                                    print("No Products")
                                                    break
                                        elif ch3==5:
                                            print("||Welcome To CART||")
                                            print()
                                            while True:
                                                print("\t\t\t\t-------------------------")
                                                print("\t\t\t\t|Enter 1: Display CART  |")
                                                print("\t\t\t\t|Enter 2: Purchase Items|")
                                                print("\t\t\t\t|Enter 3: Remove Item   |")
                                                print("\t\t\t\t|Enter 0: Go To Back    |")
                                                print("\t\t\t\t-------------------------")
                                                ch4=int(input("Enter the choice:"))
                                                if ch4!=0:
                                                    if ch4==1:
                                                        print("||All Products||")
                                                        print()
                                                        print("Product:")
                                                        if len(cart)!=0:
                                                            for i in cart:
                                                                print("Name:",i["prod_name"])
                                                                print("Category:",i["prod_category"])
                                                                print("Price:",i["prod_price"])
                                                                print("Desc:",i["prod_desc"])
                                                                print("ID:",i["ID"])
                                                                print()
                                                        else:
                                                            print("CART is Empty") 
                                                    elif ch4==2:
                                                        print("||BILL||")
                                                        if len(cart)!=0:
                                                            Total_amt=0
                                                            for i in cart:
                                                                Total_amt=Total_amt+i["prod_Total"]
                                                            
                                                            print("-----------------------------------------------------")
                                                            print("Products    Price    Quantity    Amount")
                                                            for i in cart:
                                                                print(i["prod_name"],"         ",i["prod_price"],"        ",i["prod_quantity"],"     ",i["prod_Total"])
                                                            print()
                                                            print()
                                                            print()
                                                            print()
                                                            print()
                                                            print("YOUR TOTAL PURSCHASE:",Total_amt)                                                                
                                                            print("-----------------------------------------------------")
                                                            break
                                                        else:
                                                            print("CART is Empty") 
                                                    elif ch4==3:
                                                        print("||Remove Item||")
                                                        print()
                                                        if len(cart)!=0:
                                                            remove_id=int(input("Enter the ID of Product to Remove:"))
                                                            for i in cart:
                                                                if i["ID"]==remove_id:
                                                                    cart.remove(i)
                                                                    print("Item Removed")
                                                                    break
                                                            else:
                                                                print("ID does not match")
                                                        else:
                                                            print("CART is Empty")
                                                    else:
                                                        print("Invalid choice")
                                                else:
                                                    break
                                        elif ch3==6:
                                            print("||HELP||")
                                            print()
                                            print("Name: AVI PATEL")
                                            print("Co-Founder of the Company Amazon")
                                            print("Mobile:1234567899")
                                            print("Email:avi@gmail.com")
                                            print()
                                            print("Please contact the following person for HELP")
                                            print("Name: ABHI PATEL")
                                            print("Manager of the Company Amazon")
                                            print("Mobile:9023601796")
                                            print("Email:abhi@gmail.com")
                                        else:
                                            print("Invalid choice")
                                    else:
                                        break
                        else:
                            print("Not Registered Yet")
                    else:
                        print("Invalid choice")
                else:
                    break
        elif ch==2:
            print()
            print("||Welcome Sellers||")     
            while True:
                print("\t------------------------")
                print("\t| Enter 1: To Register |")
                print("\t| Enter 2: To Login    |")
                print("\t| Enter 0: To Go Back  |")
                print("\t------------------------")
                ch1=int(input("Enter the choice:"))
                
                if ch1!=0:
                    if ch1==1:
                        print()
                        print("||Registration||")                     
                        reg={}
                        name=input("Enter your name:")
                        reg["name"]=name
                        last_name=input("Enter your last name:")
                        reg["last_name"]=last_name
                        mobile=int(input("Enter your phone number:"))
                        for i in regs_sell:
                            if i["mobile"]==mobile:
                                reg["mobile"]=0
                                print("Phone number already exist")
                                break
                        else:
                            reg["mobile"]=mobile
                        email=input("Enter your email:")
                        for j in regs_sell:
                            if j["email"]==email:
                                reg["email"]="NULL"
                                print("Email already exist")
                                break
                        else:
                            reg["email"]=email
                        password=input("Enter your password:")
                        reg["password"]=password
                        confirm_password=input("Confirm your password:")                
                        if password==confirm_password:
                            reg["confirm_password"]=confirm_password
                            regs_sell.append(reg)                       
                        else:
                            print("Confirm Password does not match with Password")                        
                    elif ch1==2:
                        print()
                        print("||Login||")                     
                        if len(regs_sell)!=0:
                            print("\t\t--------------------------------")
                            print("\t\t| Enter 1:Login through Mobile |")
                            print("\t\t| Enter 2:Login through Email  |")
                            print("\t\t--------------------------------")
                            ch2=int(input("Enter the choice:"))
                            
                            func=0
                            if ch2==1:          
                                func=0
                                print()
                                print("||Login through Mobile||")                           
                                login_mobile=int(input("Enter your phone number:"))
                                flag=1
                                for i in regs_sell:
                                    if i["mobile"]==login_mobile:
                                        flag=2
                                        login_password=input("Enter your password:")
                                        if i["password"]==login_password:
                                            print("Login successfull")
                                            func=1
                                        else:
                                            print("Password not matched")
                                if flag==1:
                                    print("Phone number not found")                            
                            elif ch2==2:
                                func=0
                                print()
                                print("||Login through Email||")                          
                                login_email=input("Enter your Email:")
                                flag=1
                                for i in regs_sell:
                                    if i["email"]==login_email:
                                        flag=2
                                        login_password=input("Enter your password:")
                                        if i["password"]==login_password:
                                            print("Login successfull")
                                            func=1
                                        else:
                                            print("Password not matched")
                                if flag==1:
                                    print("Email not found")
                            else:
                                print("Invalid choice")
                            
                            if func==1:
                                print()
                                while True:
                                    print("\t\t\t----------------------------")
                                    print("\t\t\t| Enter 1: Add Product     |")
                                    print("\t\t\t| Enter 2: Remove Product  |")
                                    print("\t\t\t| Enter 3: Update Product  |")
                                    print("\t\t\t| Enter 4: Display Product |")
                                    print("\t\t\t| Enter 0: To Go Back      |")
                                    print("\t\t\t----------------------------")
                                    ch3=int(input("Enter the choice:"))                                    
                                    
                                    if ch3!=0:
                                        if ch3==1:
                                            print("||Adding Products||")
                                            print()                                            
                                            product={}
                                            flag1=1
                                            while flag1==1:
                                                prod_name=input("Enter the product Name:")
                                                for i in products:
                                                    if i["prod_name"]==prod_name:
                                                        print("Product with this name already exist")
                                                        break
                                                else:                                                
                                                    product["prod_name"]=prod_name
                                                    flag1=2
                                            prod_category=input("Enter the product Category:")
                                            product["prod_category"]=prod_category
                                            prod_price=int(input("Enter the product Price:"))
                                            product["prod_price"]=prod_price
                                            prod_desc=input("Enter the product Description:")
                                            product["prod_desc"]=prod_desc  
                                            prod_id=prod_id+1
                                            product["ID"]=prod_id
                                            products.append(product)
                                            print("Product Added")
                                        elif ch3==2:
                                            print("||Removing Products||")
                                            print()
                                            if len(products)!=0:
                                                remove_id=int(input("Enter the ID of Product to Remove:"))
                                                for i in products:
                                                    if i["ID"]==remove_id:
                                                        products.remove(i)
                                                        print("Product Removed")
                                                        break
                                                else:
                                                    print("ID does not match")
                                            else:
                                                print("No Products")
                                        elif ch3==3:
                                            print("||Updating Products||")
                                            print()
                                            if len(products)!=0:                                            
                                                old_name=input("Enter the Name of Product to Update:")
                                                for i in products:
                                                    if i["prod_name"]==old_name:
                                                        old_id=int(input("Enter the ID of Product to Update:"))
                                                        if i["ID"]==old_id:
                                                            update_name=input("Enter the NEW product Name:")
                                                            i["prod_name"]=update_name
                                                            update_category=input("Enter the Category of Product:")
                                                            i["prod_category"]=update_category
                                                            update_price=input("Enter the Price of Product:")
                                                            i["prod_price"]=update_price
                                                            update_desc=input("Enter the Description of Product:")
                                                            i["prod_desc"]=update_desc
                                                            update_id=int(input("Enter the ID of Product:"))                                                                
                                                            i["ID"]=update_id
                                                            print("Product Updated")
                                                        else:
                                                            print("Wrong ID of the product")
                                                        break
                                                else:
                                                    print("Product of this name not found")
                                            else:
                                                print("No Products")
                                        elif ch3==4:
                                            print("||Displaying Products||")
                                            print()
                                            print("Product:")
                                            if len(products)!=0:
                                                for i in products:
                                                    print("Name:",i["prod_name"])
                                                    print("Category:",i["prod_category"])
                                                    print("Price:",i["prod_price"])
                                                    print("Desc:",i["prod_desc"])
                                                    print("ID:",i["ID"])
                                                    print()
                                            else:
                                                print("No Products")
                                        else:
                                            print("Invalid choice")
                                    else:
                                        break
                        else:
                            print("Not Registered Yet")
                    else:
                        print("Invalid choice")
                else:
                    break
        else:
            print("Invalid choice")
    else:
        print("Thank you")
        print("Visit Again")
        break
#The END