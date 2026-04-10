import time
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
    'Total': round(25.50 * 2,2)
},{
    'Item': 'Mechanical Keyboard',
    'Price': 89.99,
    'Quantity': 1,
    'Total': round(89.99 * 1,2)
}, {
    'Item': 'USB-C Hub',
    'Price': 45.00,
    'Quantity': 3,
    'Total': round(45.00 * 3,2)
}]

#action information
print('-'*10,'Enter 0 to stop simulation','-'*20)
print('-'*10,'Enter 1 to add to shopping list','-'*20)
print('-'*10,'Enter 2  to edit the shopping list-> This action only allows editing not deletion','-'*10)
print('-'*10,'Enter 3 to delete from shopping list','-'*20)
print('-'*10,'Enter p to proceed to checkout','-'*10)
#Enter customer Budget then subtract it from total to be balanace
def p_to_check_out():
    print("\n Proceeding to checkout")
    totals=[]
    if shopping_list:
        for i in shopping_list:
            tot=i.get('Total','Key Not Found')
            totals.append(tot)
        final=round(sum(totals),2)
        print(*shopping_list,sep='\n')
        time.sleep(2)
        print(f'\n Your shopping total is:${final}')
    else:
        print('🚨 Can not Proceed to Checking->Empty Shopping Cart')
#input actions

def unknown_action():
    print("Error-> Unknown Command")


def change_budget():
    print('\n Proceeding to change the Budget')
    while True:
        new_budget_input=gate_keeper('Enter the new Budget:',input_actions)
        try:
            new_budget=float(new_budget_input)
            return new_budget
        except ValueError:
            print('Error Invalid Input-> User ONly Numbers to Enter Budget')

def quit():
    print('-'*15,"Proceeding to Quit the Online shopping system",'-'*15)
    time.sleep(3)
    print('Bye!👋')


def get_customer_budget():
    while True:
        customer_budget_input=gate_keeper('Enter Your budget for safer tracking',input_actions)
        try:
            customer_budget=float(customer_budget_input)
            time.sleep(2)
            print('Your Current Budget is:$',customer_budget)
            return customer_budget
        except ValueError:
            print('\n 🚨Unsupported Input->Please use Numbers Only')



def add_items():
    print('\n Proceeding to Adding Items to shopping List')
    time.sleep(2)
    input_actions={
            'p':p_to_check_out,
            'q':quit
        }
    customer_budget=get_customer_budget()
    while True:
        item_index_input=gate_keeper('Enter the NUmber of item to be added to your shopping list->use Numbers please',input_actions)
        if item_index_input:
            if item_index_input in input_actions:
                action=input_actions.get(item_index_input,unknown_action)
                action()
                break
            else:
                try:
                    item_index=int(item_index_input)-1
                    true_item=tuple(grocery_prices)[item_index]
                except ValueError:
                    print("\n 🚨 Unsupported Input Format->Please Use Numbers Only")
                except IndexError:
                    print('\n 🚨Index Out Of Bounds->NUmber Entered Does Not exist')
        else:
            print("Empty->Fill The Input Please")
        item_price=grocery_prices.get(true_item,"Item does not Exist")
        quantity_input=gate_keeper(f"How many {true_item}/s would you like? ",input_actions)
        if quantity_input:
            if quantity_input in input_actions:
                action=input_actions.get(quantity_input,unknown_action)
                action()
                break
            else:
                try:
                    quantity=int(quantity_input)
                    print(true_item,item_price,quantity,round((item_price*quantity),2))
                except ValueError:
                    print("\n 🚨 Unsupported Input Format->Please Use Numbers Only")
        else:
            print("Empty Field->Fill The Input Please")
        grocery_item={
            'Item':true_item,
            "Price":item_price,
            "Quantity":quantity,
            "Total":round((quantity*item_price),2)
        }
        print("\n Your Current shopping list")
        shopping_list.append(grocery_item)
        print(*shopping_list,sep='\n')
        customer_budget=check_budget(customer_budget,shopping_list)


def check_budget(customer_budget,list):
    print("\n Proceeding to check customer's budget")
    time.sleep(2)
    tots=[]
    if not list:
        print('🚨Error->Shopping List is Empty can not proceed to Checkout')
    else:
        for i in list:
            tots.append(i['Total'])
        total_bill = sum(tots) 
        if total_bill > customer_budget:
            over = total_bill - customer_budget
            print(f"⚠️ Warning: You are ${over:.2f} OVER BUDGET")
            next_step=gate_keeper('What would you like to do to chage this\n1: Change_budget\n2: Change_quantity \n:q Quit',input_actions)
            if next_step =='1':
                print(f'\n You need {customer_budget+over} to catch up to your current shopping Total')
                customer_budget=change_budget()
                print(f'Your New Budget is:{customer_budget}')
                return check_budget(customer_budget,list)
            elif next_step=='2':
                item_pos=get_item_from_list()
                if item_pos is not None:
                    quantity_change(item_pos)
            elif next_step=='q':
                quit()
        elif total_bill < customer_budget:
            leftover = customer_budget - total_bill
            print(f"✅ You have ${leftover:.2f} remaining.")
        else:
            print("🎯 You are exactly on budget!")


def delete_items():
    input_actions={
            'p':p_to_check_out,
            'q':quit
        }
    print("\n Proceeding to Delete Items from the shopping List")
    time.sleep(2)
    while True:
        print('\n')
        for num ,i in enumerate(shopping_list,1):
            print(f"{num}:{i}")
        position_to_delete=gate_keeper('Enter the Position For the item You would like to Delete?',input_actions)
        if position_to_delete:
            if position_to_delete in input_actions:
                action=input_actions.get(position_to_delete,unknown_action)
                action()
                break
            else:
                try:
                    pos=int(position_to_delete)-1
                    item_removed=shopping_list.pop(pos)
                    print(f"\n Item Removed:{item_removed}")
                except IndexError:
                    print('\n 🚨Index Out Of Bounds->NUmber Entered Does Not exist')
                except ValueError:
                    print("\n 🚨 Unsupported Input Format->Please Use Numbers Only")
        else:
            print("🚨Empty Field-> Fill the Input Field")


def get_item_from_list():
    for num, i in enumerate(shopping_list,1):
        print(num,i)
    while True:
        item_position_input=gate_keeper('Enter the position of the Item Quantity you would like to change?',input_actions)
        if item_position_input:
            if item_position_input in input_actions:
                action=input_actions.get(item_position_input,unknown_action)
                action()
                break
            else:
                try:
                    item_pos=int(item_position_input)-1
                    true_item=shopping_list[item_pos]
                    print(true_item)
                    print(f"proceeding to change:\"{true_item.get('Item','Key Not Found')}\"from \"{true_item.get('Quantity','Key Not Found')}\"")
                    break
                except ValueError:
                    print('\n 🚨Unsupported Input->Please use Numbers Only')
                except IndexError:
                    print('\n 🚨Index Out Of Bounds->NUmber Entered Does Not exist')
        else:
            print("🚨Empty Field-> Fill the Input Field")
    return item_pos


def item_change(item_pos):
    print('\n Proceeding to change the Item')
    input_actions={
            'p':p_to_check_out,
            'q':quit
        }
    for num, i in enumerate(shopping_list,1):
        print(num,i)
    print(f"Changing Name for: {shopping_list[item_pos]['Item']}")
    while True:
        new_item_position=gate_keeper('Enter the Position of the new item you would like ?',input_actions)
        if new_item_position:
            if new_item_position in input_actions:
                action=input_actions.get(new_item_position,unknown_action)
                action()
                break
            else:
                try:
                    new_item=int(new_item_position)-1
                    item_name=tuple(grocery_prices)[new_item]
                    item_price=grocery_prices.get(item_name,'Key Not Found')
                    choosen_item=shopping_list[item_pos]
                    choosen_item["Item"]=item_name
                    choosen_item["Price"]=item_price
                    choosen_item["Total"]=round((item_price*choosen_item["Quantity"]),2)
                    print('Item change successful')
                    print(*shopping_list,sep='\n')
                    break
                except ValueError:
                    print('\n 🚨Unsupported Input->Please use Numbers Only')
                except IndexError:
                    print('\n 🚨Index Out Of Bounds->NUmber Entered Does Not exist')
        else:
            print("🚨Empty Field-> Fill the Input Field")


def quantity_change(item_pos):
    print("\n Proceeding to change the item's Quantity")
    while True:
        new_item_position_quantity=gate_keeper('Enter the New Quantity?',input_actions)
        if new_item_position_quantity:
            if new_item_position_quantity in input_actions:
                action=input_actions.get(new_item_position_quantity,unknown_action)
                action()
                break
            else:
                try:
                    new_quantity=int(new_item_position_quantity)
                    choosen_item=shopping_list[item_pos]
                    choosen_item["Quantity"]=new_quantity
                    choosen_item["Total"]=round((choosen_item["Price"]*new_quantity),2)
                    print('Item change successful')
                    print(*shopping_list,sep='\n')
                    break
                except ValueError:
                    print('\n 🚨Unsupported Input->Please use Numbers Only')
                except IndexError:
                    print('\n 🚨Index Out Of Bounds->NUmber Entered Does Not exist')
        else:
            print("🚨Empty Field-> Fill the Input Field")
#return value and use it as argument for Edit funcion

def edit_list():
    while True:
        print("\n--- Edit Menu ---")
        print("1: Change Item Name\n2: Change Quantity\n3: Change Both\nq: Back\n:p: Checkout")
        
        choice = input("Choice: ").strip().lower()
        if choice == 'q':
            break
        elif choice == '1':
            item_pos= get_item_from_list() 
            if item_pos is not None:    
                item_change(item_pos) 
        elif choice == '2':
            item_pos= get_item_from_list()
            if item_pos is not None:
                quantity_change(item_pos)
        elif choice == '3':
            item_pos= get_item_from_list()
            if item_pos is not None:
                item_quantity_change(item_pos)
        elif choice=='p':
            p_to_check_out()
            break
        else:
            print("🚨 Invalid Option. Please try again.")


def item_quantity_change(item_pos):
    print("\n--- Step 1: Change the Item Name ---")
    item_change(item_pos) 
    
    print("\n--- Step 2: Change the Quantity ---")
    quantity_change(item_pos)
    
    print("\n✅ Both Item and Quantity updated successfully.")


input_actions={
    'p':p_to_check_out,
    'q':quit,
}
user_actions={
    '0':quit,
    '1':add_items,
    '2':edit_list,
    '3':delete_items,
}
def gate_keeper(prompts,actions):
    while True:
        user_input=input(prompts).lower().strip()
        if not user_input:
            print('Error-> Empty Input:Please fill the field')
            continue
        if user_input in actions:
            return user_input
        try:
            float(user_input)
            return user_input
        except ValueError:
            print('Error-> Use Number Only')
        else:
            print('Error -> Invalid option Entered by the User')
def main(user_actions):
    while True:
        choice=gate_keeper('What would you like to do',input_actions)
        action=user_actions.get(choice,unknown_action)
        action()

main(user_actions)
