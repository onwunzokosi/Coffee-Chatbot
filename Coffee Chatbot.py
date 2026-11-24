# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  drinks = []

# this loop takes the user back to get_size when yes is selected in additional_drink function
  while True:
    size = get_size()
    drink_type = get_drink_type()
    drinks.append("{} {}".format(size, drink_type))
    print("Alright, that's a {} {}!".format(size, drink_type))

    if not additional_drink():
      break

  name = input("Can I get your name please?")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

  print("Your drinks:")

  for drink in drinks:
    print("- " + drink)

# this function ask the user the size of their drink
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

# this function prints a message when an incorrect option is selected
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# this function ask the user for their drink type
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == "a":
    return order_coffee()
  elif res == "b":
    return "mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

# this function ask the user what kind of milk to use when latte is selected
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

  if res == "a":
    return "latte"
  elif res == "b":
    return "non-fat latte"
  elif res == "c":
    return "soy latte"
  else:
    print_message()
    return order_latte()

# this function ask the user the prefered temp when coffe is selected
def order_coffee():
  res = input('How would you like your coffee? \n[a] Hot \n[b] Iced \n> ')

  if res == "a":
    return "hot coffee"
  elif res == "b":
    return "iced coffee"
  else:
    print_message()
    return order_coffee()

# this function ask the user for an additional drink 
def additional_drink():
  while True:
    res = input('Would you like to order an additional drink? \n[a] Yes  \n[b] No  \n> ')

    if res == "a":
      return True
    elif res == "b":
      return False
    else:
      print_message()
      return additional_drink()

# Call coffee_bot()!
coffee_bot()
