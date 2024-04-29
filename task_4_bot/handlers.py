def parse_input(user_input):
  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, *args

def add_contact(args, contacts):
  try:
    name, phone = args
    contacts[name] = phone
    return "Contact added."
  except ValueError:
    return "Please enter name and phone number!"

def change_contact(args, contacts):
  try:
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
  except ValueError:
    return "To change user phone please enter name and phone number!"

def show_phone(args, contacts):
  try:
    name = args
    for user_name in contacts:
      if name[0] == user_name:
        return f"{contacts[user_name]}"
  except:
    return "Please enter user name!"
    
def show_all(contacts):
  str_ = ''
  for name, phone in contacts.items():
    str_ += name + ' ' + phone + '\n'
  return str_ 