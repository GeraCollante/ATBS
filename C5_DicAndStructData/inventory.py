# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,
                             0)  # this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1  # and this increases that value by one, each time that item appears in the loot list
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
