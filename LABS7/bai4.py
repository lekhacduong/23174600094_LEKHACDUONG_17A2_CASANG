inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# yc1:
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory,'\n')

# yc2:
sap_xep = sorted(inventory['backpack'])
print(sap_xep, '\n')

# yc3:
del inventory['backpack'][1]
print(inventory, '\n')

#yc4:
inventory['gold'] += 50
print(inventory)
