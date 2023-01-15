import pyinputplus as pyip

price = 0

breadType = pyip.inputMenu(['White', 'Brown', 'Sourdough'], prompt = 'What type of bread would you like?\n')
price += 100
proteinType = pyip.inputMenu(['Chicken','Turkey', 'Ham', 'Tofu'], prompt= 'What type of protein would you like?\n')
price += 150
wantCheese = pyip.inputYesNo('Would you like to have cheese?')
if wantCheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='What type of Cheese would you like?\n')
    price += 25
wantMayo = pyip.inputYesNo('Would you like to have Mayo?')
if wantMayo == 'yes':
    price += 10
wantMustard = pyip.inputYesNo('Would you like to have Mustard?')
if wantMustard == 'yes':
    price += 10
wantLettuce = pyip.inputYesNo('Would you like to have Lettuce?')
if wantLettuce == 'yes':
        price += 10
wantTomato = pyip.inputYesNo('Would you like to have Tomato?')
if wantTomato == 'yes':
        price += 10

print("The total cost for your order is", price, "Rupees")
