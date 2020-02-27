# Date: 2/27/2020
# Topic: Dictonaries

# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s 
# inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should 
# return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item.
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
