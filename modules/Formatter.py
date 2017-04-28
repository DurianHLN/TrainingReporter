# Module that holds functions to format text or sort name lists
#
from anvil import *
from NameFormat import Name

def title(string):
  return "[b]" + string.upper() + "[/b]"
      
def sort_text_area(text_area):
  try:
    text_area.text = generate_sorted_member_list(text_area.text.splitlines())
    text_area.foreground = "BLACK"
  except FormatError as e:
    text_area.foreground = "RED"
    alert(e.args)
    raise e
    
def generate_text_block(header, body):
  if isinstance(header, Label):
    header = header.text
  if isinstance(body, TextArea) or isinstance(body, TextBox):
    body = body.text
  text_block = "{}\n{}\n\n\n"
  return text_block.format(title(header), body)

def generate_sorted_member_list(members):
  if not members:
    return "N/A"
  def trim_name(name, *delimiters):
    for delimiter in delimiters:
      name = name.replace(delimiter, "")
    return name
  def is_initial(string):
    return len(string) == 1
  member_names = []
  
  for member_string in members:
    member_string = member_string.split()
    if len(member_string) > 4:
      raise FormatError(" ".join(member_string) + " in invalid format!")
      
    name_params = {"rank": member_string[0], "last_name": None,
                   "first_initial": None, "middle_initial": None}
    
    for token in member_string:
      token = trim_name(token, ",", ".")
      if is_initial(token):
        initial = "first_initial" if not name_params.get("first_initial") else "middle_initial"
        name_params[initial] = token
      else:
        name_params["last_name"] = token

    member_names.append(Name(name_params.get("rank"), name_params.get("last_name"), name_params.get("first_initial"), name_params.get("middle_initial")))
    
  member_names.sort()
      
  return "\n".join(str(member_name) for member_name in member_names)

class FormatError(Exception):
  """Exception raised for inputs that cannot be formatted"""
  def __init__(self, msg):
    self.msg = msg