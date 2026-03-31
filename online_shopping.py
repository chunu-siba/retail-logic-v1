grocery_prices = {
    "Milk (1 gal)": 3.99,
    "Eggs (1 doz)": 2.49,
    "Bread (Loaf)": 2.99,
    "Apples (1 lb)": 1.89,
    "Bananas (1 lb)": 0.59,
    "Chicken Breast (1 lb)": 4.50,
    "Rice (2 lb bag)": 2.25,
    "Butter (1 lb)": 4.99,
    "Pasta (16 oz)": 1.50,
    "Cheddar Cheese (8 oz)": 3.75,
    "Coffee (12 oz)": 8.99,
    "Potatoes (5 lb bag)": 4.25,
    "Greek Yogurt (32 oz)": 5.49,
    "Spinach (Fresh bag)": 3.29,
    "Olive Oil (500ml)": 7.95
}
text='GROCERY ITEMS'
print(f"{text:-^38}") 
for post,( item , price )in enumerate(grocery_prices.items(),1):
    print(f"{post}:{item:<37} | ${price:<7.2f}")
print('-'*38)
shopping_list=[ {
    'Item': 'Wireless Mouse',
    'Price': 25.50,
    'Quantity': 2,
    'Total': f'{25.50 * 2:.2f}'
},{
    'Item': 'Mechanical Keyboard',
    'Price': 89.99,
    'Quantity': 1,
    'Total': f'{89.99 * 1:.2f}'
}, {
    'Item': 'USB-C Hub',
    'Price': 45.00,
    'Quantity': 3,
    'Total': f'{45.00 * 3:.2f}'
}]
#action information
print('-'*10,'Enter 0 to stop simulation','-'*20)
print('-'*10,'Enter 1 to add to shopping list','-'*20)
print('-'*10,'Enter 2  to edit the shopping list-> This action only allows editing not deletion','-'*10)
print('-'*10,'Enter 3 to delete from shopping list','-'*20)
print('-'*10,'Enter p to proceed to checkout','-'*10)
action_input=input('What would you like to do:')
#functions for each action
#function for adding items to shopping list
def add_items():
    print('-'*15,'Enter q to quit','-'*15)
    print('-'*15,'Enter P to move to check out','-'*15)
    while True:
        item_number_input=input('Please enter the NUMBER POSITION of the item you would like to add')
        if item_number_input.lower().strip() =='q':
            print('\n Quiting the shopping process')
            break
        elif item_number_input.lower().strip() =='p':
            print('-'*15,"Proceeding to Checkout",'-'*15)
            p_to_check_out()
            break
        else:
            try:
                item_number=int(item_number_input)-1
                true_item_key=tuple(grocery_prices.keys())[item_number]
                true_item_value=tuple(grocery_prices.values())[item_number]
                print(true_item_key,'at',true_item_value)
                item_quantity_input=input(f'how many {true_item_key} would you like?')
                if item_quantity_input.lower() =='q':
                    print('\n Quiting the shopping process')
                    break
                elif item_quantity_input.lower().strip()=='p':
                    print('-'*5,f"Proceeding to checkout now item:\"{true_item_key}\" won't be added to your shopping list->Quantity Unknown",'-'*5)
                    confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                    if confirmation =='y':
                        print('-'*15,"Proceeding to Checkout",'-'*15)
                        p_to_check_out()
                        break
                    elif confirmation =='n':
                        item_quantity_input=input(f'how many {true_item_key} would you like?')
                        try:
                            item_quantity=int(item_quantity_input)
                            add_to_cart={
                                'Item':true_item_key,
                                "Price":true_item_value,
                                "Quantity":item_quantity,
                                "Total":f'{true_item_value*item_quantity:.2f}'
                            }
                            shopping_list.append(add_to_cart)
                            print("Your current Shopping list")
                            print(*shopping_list,sep='\n')
                            #check bugdet after each item added to the shopping cart
                            check_budget()
                        except ValueError:
                            print('Unsupported Input->Please use numbers Only',item_quantity_input)
                    else:
                        try:
                            item_quantity=int(item_quantity_input)
                            add_to_cart={
                                'Item':true_item_key,
                                "Price":true_item_value,
                                "Quantity":item_quantity,
                                "Total":f'{true_item_value*item_quantity:.2f}'
                            }
                            shopping_list.append(add_to_cart)
                            print("Your current Shopping list")
                            print(*shopping_list,sep='\n')
                            #check bugdet after each item added to the shopping cart
                            check_budget()
                        except ValueError:
                            print('Unsupported Input->Please use numbers Only',item_quantity_input)
            except ValueError:
                print('Unsupported Input->Please use numbers Only',item_number_input)
            except IndexError:
                print('Index Out Of Bounds->Number not in Grocery List',item_number_input)

def check_budget():
    tots=[]
    for t in shopping_list:
        tots.append(float(t['Total']))
    total=sum(tots)
    if total > customer_budget:
        print(f'You have exceeded the budget by:{total- customer_budget:.2f}')
        query=input('would you like to: A->Increase your budget| B Reduce your grocery|C add it to your credit card').lower().strip()
        if query=='a':
            new_budget=input(f'Please Enter the new Budget the old is:${total- customer_budget:.2f}short')
            try:
                new_customer_budget=float(new_budget)
                print(f"\n Your new Budget has been changed from ${customer_budget:.2f} to:${new_customer_budget:.2f}")
            except ValueError:
                print('Please Enter Numbers only')
        elif  query=='b':
            print('Proceeding to edit your shopping list')
            edit_list()
        elif  query=='c':
            print(f'\n While proceeding to check out you will have a credit balance of: ${total- customer_budget:.2f}')
        else:
            print('Please put input from given options')
    else:
        print(f'You have {customer_budget-total:.2f} left in your budget')

def edit_list():
    print('-'*15,"Proceeding to edit your shopping list",'-'*15)
    print('-'*15,'Enter q to quit','-'*15)
    print('-'*15,'Enter P to move to check out','-'*15)
    #check if there are items in the shopping list
    while True:
        if not shopping_list:
            print("Sorry you can not edit your shppping list-> shopping list empty")
        else:
            part_edit_input=input("Enter-> 1=To edit Item| 2= To edit quantity| 3= To edit Both").lower().strip()
            if part_edit_input =='p':
                print('-'*15,"Proceeding to Checkout",'-'*15)
                p_to_check_out()
                break
            elif part_edit_input== 'q':
                print('-'*15,"Leaving the Editing Option",'-'*15)
                break
            elif part_edit_input=='1':
                print(f"\n Proceeding to change Item")
                founds=[]
                for num,i in enumerate(shopping_list,1):
                    founds.append(i['Item'])
                    print(num,i)
                item_change_input=input("which Item would you like to change->Enter Number of item to be changed").lower().strip()
                if item_change_input=='p':
                    print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                    confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                    if confirmation =='y':
                        print('-'*15,"Proceeding to Checkout",'-'*15)
                        p_to_check_out()
                        break
                    elif confirmation =='n':
                        item_change_input=input("which Item would you like to change->Enter Number of item to be changed").lower().strip()
                        try:
                            true_item_change_index=int(item_change_input)-1
                            old_item=founds[true_item_change_index]
                            new_item_pos=input(f"please Enter the number in which you want to change \"{old_item}\" to")
                            if new_item_pos=='p':
                                print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                if confirmation =='y':
                                    print('-'*15,"Proceeding to Checkout",'-'*15)
                                    p_to_check_out()
                                    break
                                elif confirmation =='n':
                                    new_item_pos=input(f"\n please Enter the number in which you want to change \"{old_item}\" to")
                                    try:
                                        #fixed the bug and update code on the no confirmation
                                        new_item_index=int(new_item_pos)-1
                                        new_item_true_index=tuple(grocery_prices)[new_item_index]
                                        new_item_price = grocery_prices.get(new_item_true_index, 0)
                                        print(new_item_true_index,new_item_price)
                                        print()
                                        choosen_item=shopping_list[true_item_change_index]
                                        choosen_item['Item']=new_item_true_index
                                        choosen_item['Price']=new_item_price
                                        choosen_item['Total']=f"{new_item_price*i['Quantity']:.2f}"
                                        print('Your shoping list has been updated-> Both the item and the price')
                                        print(*shopping_list,sep='\n')
                                    except ValueError:
                                        print("Please use Numbers Only")
                                    except IndexError:
                                        print('Index Out Of Bounds->Number entered does not exist')
                            elif new_item_pos=='q':
                                print("quiting the Editing process-> All items shall remain unchanged")
                            else:
                                try:
                                    #fixed the bug and update code on the no confirmation
                                    new_item_index=int(new_item_pos)-1
                                    new_item_true_index=tuple(grocery_prices)[new_item_index]
                                    new_item_price = grocery_prices.get(new_item_true_index, 0)
                                    print(new_item_true_index,new_item_price)
                                    print()
                                    choosen_item=shopping_list[true_item_change_index]
                                    choosen_item['Item']=new_item_true_index
                                    choosen_item['Price']=new_item_price
                                    choosen_item['Total']=f"{new_item_price*i['Quantity']:.2f}"
                                    print('Your shoping list has been updated-> Both the item and the price')
                                    print(*shopping_list,sep='\n')
                                except ValueError:
                                    print("Please use Numbers Only")
                                except IndexError:
                                    print('Index Out Of Bounds->Number entered does not exist')
                        except ValueError:
                            print('Unsupported INput->Use numbers only')
                        except IndexError:
                            print('Index Out Of Bounds->Number entered does not exist')
                elif item_change_input =='q':
                    print("quiting the Editing process-> All items shall remain unchange")
                    break
                else:
                    try:
                        true_item_change_index=int(item_change_input)-1
                        old_item=founds[true_item_change_index]
                        new_item_pos=input(f"please Enter the number in which you want to change \"{old_item}\" to")
                        if new_item_pos=='p':
                            print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                            confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                            if confirmation =='y':
                                print('-'*15,"Proceeding to Checkout",'-'*15)
                                p_to_check_out()
                            elif confirmation =='n':
                                new_item_pos=input(f"\n please Enter the number in which you want to change \"{old_item}\" to")
                                try:
                                    #fixed the bug and update code on the no confirmation
                                    new_item_index=int(new_item_pos)-1
                                    new_item_true_index=tuple(grocery_prices)[new_item_index]
                                    new_item_price = grocery_prices.get(new_item_true_index, 0)
                                    print(new_item_true_index,new_item_price)
                                    print()
                                    choosen_item=shopping_list[true_item_change_index]
                                    choosen_item['Item']=new_item_true_index
                                    choosen_item['Price']=new_item_price
                                    choosen_item['Total']=f"{new_item_price*i['Quantity']:.2f}"
                                    print('Your shoping list has been updated-> Both the item and the price')
                                    print(*shopping_list,sep='\n')
                                except ValueError:
                                    print("Please use Numbers Only")
                                except IndexError:
                                    print('Index Out Of Bounds->Number entered does not exist')
                        elif new_item_pos=='q':
                            print("quiting the Editing process-> All items shall remain unchanged")
                        else:
                            try:
                                #fixed the bug and update code on the no confirmation
                                new_item_index=int(new_item_pos)-1
                                new_item_true_index=tuple(grocery_prices)[new_item_index]
                                new_item_price = grocery_prices.get(new_item_true_index, 0)
                                print(new_item_true_index,new_item_price)
                                print()
                                choosen_item=shopping_list[true_item_change_index]
                                choosen_item['Item']=new_item_true_index
                                choosen_item['Price']=new_item_price
                                choosen_item['Total']=f"{new_item_price*i['Quantity']:.2f}"
                                print('Your shoping list has been updated-> Both the item and the price')
                                print(*shopping_list,sep='\n')
                            except ValueError:
                                print("Please use Numbers Only")
                            except IndexError:
                                print('Index Out Of Bounds->Number entered does not exist')
                    except ValueError:
                        print('Unsupported INput->Use numbers only')
                    except IndexError:
                        print('Index Out Of Bounds->Number entered does not exist')
            elif part_edit_input=='2':
                print('-'*15,"Proceeding to Quantity Editing",'-'*15)
                founds_q=[]
                for num,i in enumerate(shopping_list,1):
                    founds_q.append(i['Quantity'])
                    print(num,i)
                product_for_quanity_change_input=input("Which product would you like to change it's Quantity-> Enter product Position")
                if product_for_quanity_change_input.lower() =='p':
                    print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                    confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                    if confirmation =='y':
                        print('-'*15,"Proceeding to Checkout",'-'*15)
                        p_to_check_out()
                        break
                    elif confirmation =='n':
                        product_for_quanity_change_input=input("Which product would you like to change it's Quantity-> Enter product Position")
                        try:
                            product_for_quanity_change=int(product_for_quanity_change_input)-1
                            old_item_quantity=founds_q[product_for_quanity_change]
                            choosen_item_q=shopping_list[product_for_quanity_change]
                            new_quantity_change_to_input=input(f"you would like to change the amount of \"{choosen_item_q['Item']}\" from:\"{old_item_quantity}\" to?")
                            if new_quantity_change_to_input.lower()=='p':
                                print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                #include confirmation statements
                            elif new_quantity_change_to_input.lower()=='q':
                                print('-'*17,"Quiting the Quantity Change Process",'-'*17)
                            else:
                                try:
                                    new_quantity_change_to=int(new_quantity_change_to_input)
                                    choosen_item_q['Quantity']=new_quantity_change_to
                                    choosen_item_q['Total']=round((choosen_item_q['Price']*new_quantity_change_to),2)
                                    print('\n Updated Shopping List->Quantity Updated')
                                    print(*shopping_list,sep='\n')
                                except  ValueError:
                                    print("Unsupported INput-> Use Numbers Positon Only")
                        except  ValueError:
                            print("Unsupported INput-> Use Numbers Positon Only")
                elif product_for_quanity_change_input.lower()=='q':
                    print('-'*17,'\n Quiting the Editing Process','-'*17)
                    break
                else:
                    try:
                        product_for_quanity_change=int(product_for_quanity_change_input)-1
                        old_item_quantity=founds_q[product_for_quanity_change]
                        choosen_item_q=shopping_list[product_for_quanity_change]
                        new_quantity_change_to_input=input(f"you would like to change the amount of \"{choosen_item_q['Item']}\" from:\"{old_item_quantity}\" to?")
                        if new_quantity_change_to_input.lower()=='p':
                            print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                            confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                            if confirmation =='y':
                                print('-'*15,"Proceeding to Checkout",'-'*15)
                                p_to_check_out()
                            elif confirmation =='n':
                                new_quantity_change_to_input=input(f"you would like to change the amount of \"{choosen_item_q['Item']}\" from:\"{old_item_quantity}\" to?")
                                try:
                                    new_quantity_change_to=int(new_quantity_change_to_input)
                                    choosen_item_q['Quantity']=new_quantity_change_to
                                    choosen_item_q['Total']=round((choosen_item_q['Price']*new_quantity_change_to),2)
                                    print('\n Updated Shopping List->Quantity Updated')
                                    print(*shopping_list,sep='\n')
                                except  ValueError:
                                    print("Unsupported INput-> Use Numbers Positon Only")
                        elif new_quantity_change_to_input.lower()=='q':
                            print('-'*17,"Quiting the Quantity Change Process",'-'*17)
                        else:
                            try:
                                new_quantity_change_to=int(new_quantity_change_to_input)
                                choosen_item_q['Quantity']=new_quantity_change_to
                                choosen_item_q['Total']=round((choosen_item_q['Price']*new_quantity_change_to),2)
                                print('\n Updated Shopping List->Quantity Updated')
                                print(*shopping_list,sep='\n')
                            except  ValueError:
                                print("Unsupported INput-> Use Numbers Positon Only")
                    except ValueError:
                        print("Unsupported INput-> Use Numbers Positon Only")
                    except IndexError:
                        print("Index Out of Bounds-> The Number Entered does Not Exist")
            elif part_edit_input=='3':
                print('Proceeding to Edit Both Item and Quantity')
                founds=[]
                for num,i in enumerate(shopping_list,1):
                    founds.append(i['Item'])
                    print(num,i)
                postion_item__to_change_input=input("Enter Position of item You would like to change")
                if postion_item__to_change_input.lower()=='p':
                    print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                    confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                    if confirmation =='y':
                        print('-'*15,"Proceeding to Checkout",'-'*15)
                        p_to_check_out()
                        break
                    elif confirmation =='n':
                        postion_item__to_change_input=input("Enter Position of item You would like to change")
                        try:
                            postion_item__to_change=int(postion_item__to_change_input)-1
                            choosen_item_c=shopping_list[postion_item__to_change]
                            print(choosen_item_c)
                            new_item_change_pos_input=input('Enter Position of new_item')
                            if new_item_change_pos_input.lower()=='p':
                                print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                if confirmation =='y':
                                    print('-'*15,"Proceeding to Checkout",'-'*15)
                                    p_to_check_out()
                                    break
                                elif confirmation =='n':
                                    new_item_change_pos_input=input('Enter Position of new_item')
                                    try:
                                        new_item_change_pos=int(new_item_change_pos_input)-1
                                        grocery_item=tuple(grocery_prices)[new_item_change_pos]
                                        grocery_price=grocery_prices.get(grocery_item,'Not Found')
                                        print(grocery_item,grocery_price)
                                        new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                        if new_quantity_change_inp.lower()=='p':
                                            print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                            confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                            if confirmation =='y':
                                                print('-'*15,"Proceeding to Checkout",'-'*15)
                                                p_to_check_out()
                                                break
                                            elif confirmation =='n':
                                                new_quantity_change_inp=input(f"How many {grocery_item} would you like?")
                                                try:
                                                    new_quantity=int(new_quantity_change_inp)
                                                    choosen_item_c['Item']=grocery_item
                                                    choosen_item_c['Price']=grocery_price
                                                    choosen_item_c['Quantity']=new_quantity
                                                    choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                                    print(*shopping_list,sep='\n')
                                                except ValueError:
                                                    print("Unsupported INput-> Use Numbers Positon Only")
                                        elif new_quantity_change_inp.lower()=='q':
                                            print('-'*18,'Quiting the Item Change','-'*18)
                                        else:
                                            try:
                                                new_quantity=int(new_quantity_change_inp)
                                                choosen_item_c['Item']=grocery_item
                                                choosen_item_c['Price']=grocery_price
                                                choosen_item_c['Quantity']=new_quantity
                                                choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                                print(*shopping_list,sep='\n')
                                            except ValueError:
                                                print("Unsupported INput-> Use Numbers Positon Only")
                                    except ValueError:
                                        print("Unsupported INput-> Use Numbers Positon Only")
                                    except IndexError:
                                        print("Index Out of Bounds-> The Number Entered does Not Exist")
                            elif new_item_change_pos_input.lower()=='q':
                                print('-'*18,'Quiting the Item Change','-'*18)
                                break
                            else:
                                try:
                                    new_item_change_pos=int(new_item_change_pos_input)-1
                                    grocery_item=tuple(grocery_prices)[new_item_change_pos]
                                    grocery_price=grocery_prices.get(grocery_item,'Not Found')
                                    print(grocery_item,grocery_price)
                                    new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                    if new_quantity_change_inp.lower()=='p':
                                        print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                        confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                        if confirmation =='y':
                                            print('-'*15,"Proceeding to Checkout",'-'*15)
                                            p_to_check_out()
                                        elif confirmation =='n':
                                            new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                            try:
                                                new_quantity=int(new_quantity_change_inp)
                                                choosen_item_c['Item']=grocery_item
                                                choosen_item_c['Price']=grocery_price
                                                choosen_item_c['Quantity']=new_quantity
                                                choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                                print(*shopping_list,sep='\n')
                                            except ValueError:
                                                print("Unsupported INput-> Use Numbers Positon Only")
                                    elif new_quantity_change_inp.lower()=='q':
                                        print('-'*18,'Quiting the Item Change','-'*18)
                                    else:
                                        try:
                                            new_quantity=int(new_quantity_change_inp)
                                            choosen_item_c['Item']=grocery_item
                                            choosen_item_c['Price']=grocery_price
                                            choosen_item_c['Quantity']=new_quantity
                                            choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                            print(*shopping_list,sep='\n')
                                        except ValueError:
                                            print("Unsupported INput-> Use Numbers Positon Only")
                                except ValueError:
                                    print("Unsupported INput-> Use Numbers Positon Only")
                                except IndexError:
                                    print("Index Out of Bounds-> The Number Entered does Not Exist")
                        except ValueError:
                            print("Unsupported INput-> Use Numbers Positon Only")
                        except IndexError:
                            print("Index Out of Bounds-> The Number Entered does Not Exist")
                elif postion_item__to_change_input.lower()=='q':
                    print('-'*18,'Quiting the Item Change','-'*18)
                    break
                else:
                    try:
                        postion_item__to_change=int(postion_item__to_change_input)-1
                        choosen_item_c=shopping_list[postion_item__to_change]
                        print(choosen_item_c)
                        new_item_change_pos_input=input('Enter Position of new_item')
                        if new_item_change_pos_input.lower()=='p':
                            print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                            confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                            if confirmation =='y':
                                print('-'*15,"Proceeding to Checkout",'-'*15)
                                p_to_check_out()
                                break
                            elif confirmation =='n':
                                new_item_change_pos_input=input('Enter Position of new_item')
                                try:
                                    new_item_change_pos=int(new_item_change_pos_input)-1
                                    grocery_item=tuple(grocery_prices)[new_item_change_pos]
                                    grocery_price=grocery_prices.get(grocery_item,'Not Found')
                                    print(grocery_item,grocery_price)
                                    new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                    if new_quantity_change_inp.lower()=='p':
                                        print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                        confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                        if confirmation =='y':
                                            print('-'*15,"Proceeding to Checkout",'-'*15)
                                            p_to_check_out()
                                            break
                                        elif confirmation =='n':
                                            new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                            try:
                                                new_quantity=int(new_quantity_change_inp)
                                                choosen_item_c['Item']=grocery_item
                                                choosen_item_c['Price']=grocery_price
                                                choosen_item_c['Quantity']=new_quantity
                                                choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                                print(*shopping_list,sep='\n')
                                            except ValueError:
                                                print("Unsupported INput-> Use Numbers Positon Only")
                                    elif new_quantity_change_inp.lower()=='q':
                                        print('-'*18,'Quiting the Item Change','-'*18)
                                        break
                                    else:
                                        try:
                                            new_quantity=int(new_quantity_change_inp)
                                            choosen_item_c['Item']=grocery_item
                                            choosen_item_c['Price']=grocery_price
                                            choosen_item_c['Quantity']=new_quantity
                                            choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                            print(*shopping_list,sep='\n')
                                        except ValueError:
                                            print("Unsupported INput-> Use Numbers Positon Only")
                                except ValueError:
                                    print("Unsupported INput-> Use Numbers Positon Only")
                                except IndexError:
                                    print("Index Out of Bounds-> The Number Entered does Not Exist")
                        elif new_item_change_pos_input.lower()=='q':
                            print('-'*18,'Quiting the Item Change','-'*18)
                            break
                        else:
                            try:
                                new_item_change_pos=int(new_item_change_pos_input)-1
                                grocery_item=tuple(grocery_prices)[new_item_change_pos]
                                grocery_price=grocery_prices.get(grocery_item,'Not Found')
                                print(grocery_item,grocery_price)
                                new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                if new_quantity_change_inp.lower()=='p':
                                    print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
                                    confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
                                    if confirmation =='y':
                                        print('-'*15,"Proceeding to Checkout",'-'*15)
                                        p_to_check_out()
                                        break
                                    elif confirmation =='n':
                                        new_quantity_change_inp=input(f"How many{grocery_item} would you like?")
                                        try:
                                            new_quantity=int(new_quantity_change_inp)
                                            choosen_item_c['Item']=grocery_item
                                            choosen_item_c['Price']=grocery_price
                                            choosen_item_c['Quantity']=new_quantity
                                            choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                            print(*shopping_list,sep='\n')
                                        except ValueError:
                                            print("Unsupported INput-> Use Numbers Positon Only")
                                elif new_quantity_change_inp.lower()=='q':
                                    print('-'*18,'Quiting the Item Change','-'*18)
                                    break
                                else:
                                    try:
                                        new_quantity=int(new_quantity_change_inp)
                                        choosen_item_c['Item']=grocery_item
                                        choosen_item_c['Price']=grocery_price
                                        choosen_item_c['Quantity']=new_quantity
                                        choosen_item_c['Total']=round((grocery_price*new_quantity),2)
                                        print(*shopping_list,sep='\n')
                                    except ValueError:
                                        print("Unsupported INput-> Use Numbers Positon Only")
                            except ValueError:
                                print("Unsupported INput-> Use Numbers Positon Only")
                            except IndexError:
                                print("Index Out of Bounds-> The Number Entered does Not Exist")
                    except ValueError:
                        print("Unsupported INput-> Use Numbers Positon Only")
                    except IndexError:
                        print("Index Out of Bounds-> The Number Entered does Not Exist")
            else:
                print("Unsupported INput-> Use Numbers Provided Only")

def delete_item():
    print('-'*20,"Proceeding to Item Deletion",'-'*20)
    founds=[]
    deleted_items=[]
    while True:
        for num,i in enumerate(shopping_list,1):
            founds.append(i)
            print(num,i)
        choosen_item_input_pos=input('Enter postion for item you want to delete')
        if choosen_item_input_pos.lower()=='p':
            print("Can not proceed to check out while editing shopping menu-> if you wish to shopping menu shall be kept as was")
            confirmation=input("would you like to proceed to check out knowing this?(y=Yes|n=No)").lower().strip()
            if confirmation =='y':
                print('-'*15,"Proceeding to Checkout",'-'*15)
                p_to_check_out()
                break
            elif confirmation =='n':
                choosen_item_input_pos=input('Enter postion for item you want to delete')
                try:
                    choosen_item_pos=int(choosen_item_input_pos)-1
                    removed_item = shopping_list.pop(choosen_item_pos)
                    deleted_items.append(removed_item)
                    print('-'*15,'Updated your shopping List','-'*15)
                    print(*shopping_list,sep='\n')
                    print('-----  Deleted Items List->Items shall be stored for 2days before permanent Deletion  -----')
                    print(*deleted_items,sep='\n')
                except ValueError:
                    print("Unsupported INput-> Use Numbers Provided Only")
                except IndexError:
                    print("Index Out of Bounds-> The Number Entered does Not Exist")
        elif choosen_item_input_pos.lower()=='q':
            print('-'*15,"Quiting the Deletion Process",'-'*15)
            break
        else:
            try:
                choosen_item_pos=int(choosen_item_input_pos)-1
                removed_item = shopping_list.pop(choosen_item_pos)
                deleted_items.append(removed_item)
                print('-'*15,'Updated your shopping List','-'*15)
                print(*shopping_list,sep='\n')
                print('-----  Deleted Items List->Items shall be stored for 2days before permanent Deletion  -----')
                print(*deleted_items,sep='\n')
            except ValueError:
                print("Unsupported INput-> Use Numbers Provided Only")
            except IndexError:
                print("Index Out of Bounds-> The Number Entered does Not Exist")

def p_to_check_out():
    if not shopping_list:
        print('\n Shopping List is Empty ')
        ques=input("->Would you like to shop?Enter: y=yes | n=No").lower().strip()
        if ques=='y':
            add_items()
        elif ques=='n':
            totals=[]
            for num, i in enumerate(shopping_list,1):
                totals.append(float(i["Total"]))
                print(num,i)
            tots=sum(totals)
            print(f"Shopping Total:${tots:.2f}")
    else:
        totals=[]
        for num, i in enumerate(shopping_list,1):
            totals.append(float(i["Total"]))
            print(num,i)
        tots=sum(totals)
        print(f"Shopping Total:${tots:.2f}")
        
# function for checking users desired action

if action_input =='0':
    print('-'*15,'Quiting Online shopping','-'*15)
elif action_input=='1':
    while True:
        customer_budget_input=input("Please Enter your Budget to Total Trackig purposes")
        try:
            customer_budget=float(customer_budget_input)
            print(f"Your budget is: ${customer_budget:.2f}")
            break
        except ValueError:
            print('Invalid amount',customer_budget_input,'please try again')
        print('Proceeding to Add items to the shopping list')
    add_items()
elif action_input=='2':
    edit_list()
elif action_input=='3':
    delete_item()
elif action_input.lower()=='p':
    p_to_check_out()
else:
    print('Invalid action command',action_input)
    print('Please try again')
    #function for trying again
