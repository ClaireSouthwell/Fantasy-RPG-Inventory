stuff = {'Backpack': 1, 'Chain Mail': 0, 'Clothes, Common': 0, 'Crossbow Bolts': 20,
         'Crossbow, Light': 1, 'Crowbar': 1, 'Hammer': 1, 'Dagger': 0, 'Longsword': 1,
         'Piton': 10, 'Playing Card Set': 1, 'Rations (1 Day)': 10,
         'Rope, Hempen (50 feet)': 1, 'Tinderbox': 1, 'Torch': 10, 'Warhammer': 1,
         'Waterskin':1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v 
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
