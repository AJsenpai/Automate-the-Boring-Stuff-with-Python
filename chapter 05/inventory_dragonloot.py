# Date: 2/27/2020
# Topic: Dictonaries

# #########################################################################################################################################



def displayInventory(inventory):
    item_total = 0
    print("Inventory:")
    for k, v in inventory.items():
        # print(str(v)+' '+k)
        print(v,k)
        item_total+= v
    print("Total number of items: " + str(item_total))
    
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item),0)
        inventory[item] += 1
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby' , 'eggs']
addToInventory(inv, dragonLoot)
displayInventory(inv)
