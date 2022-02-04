# Fantasy Game Inventory
# Chapter 5 - Dictionaries and Data Structures
def display_inventory(inv, name=None):
    if name is None:
        print("Inventory:")
    else:
        print("Inventory of " + name + ":")
    item_total = 0
    for key, val in inv.items():
        print(val, end=' ')
        print(key)
        item_total += inv[key]  # inv[key] == val
    print("Total number of items: " + str(item_total))


def add_to_inventory(inv, added_items):
    for i in added_items:
        inv.setdefault(i, 0)  # if an item is not in the dict, add it
        inv[i] += 1  # add 1 to inv for each item in added_items


inv_mike = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv_jason = {'torch': 1, 'rope': 2, 'gold coin': 123, 'sword': 1, 'arrow': 45, 'longbow': 1}
display_inventory(inv_mike, "Mike")
print("\n")

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'diamond', 'sword']
add_to_inventory(inv_mike, dragon_loot)
display_inventory(inv_mike, "Mike")
add_to_inventory(inv_jason, dragon_loot)
display_inventory(inv_jason, "Jason")
