import pyinputplus as pyip

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Bread type:\n")
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Protein type:\n")

cheese = pyip.inputYesNo(prompt="Would you like cheese?\n")
cheese.lower()
if cheese == "yes":
    cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'], prompt="Cheese type:\n")

mayo = pyip.inputYesNo(prompt="Would you like mayo?\n")
mustard = pyip.inputYesNo(prompt="Would you like mustard?\n")
lettuce = pyip.inputYesNo(prompt="Would you like lettuce?\n")
tomato = pyip.inputYesNo(prompt="Would you like tomato?\n")

how_many_sandwitches = pyip.inputInt(prompt="How many sandwitches?\n",min=1)
