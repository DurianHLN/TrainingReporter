# Module that holds functions to format text or sort name lists
#
from anvil import *
from NameFormat import Name

def title(string):
  return "[b]" + string.upper() + "[/b]"

def color_excuse(reason):
  reason = reason.upper()
  if "UN" in reason:
    return "[color=red]" + reason + "[/color]"
  elif "EXCUSED" in reason or "LOA" in reason:
    return "[color=green]" + reason + "[/color]"
  else:
    return "[color=yellow]" + reason + "[/color]"
      
def generate_text_block(header, body):
  if isinstance(header, Label):
    header = header.text
  if isinstance(body, TextArea) or isinstance(body, TextBox):
    body = body.text
  text_block = "{}\n{}\n\n\n"
  return text_block.format(title(header), body)

def generate_sorted_member_list(members, include_reason=False):
  def trim_name(name, delimiter):
    return name if delimiter not in name else name[:-1]
  member_names = []
  
  for member_string in members:
    member_string = member_string.split()
    if include_reason:
      reason = color_excuse(member_string[len(member_string)-1])
      member_string = member_string[:-1]
    rank = member_string[0]
    member_length = len(member_string)
    #UGLINESS!!!!!!!!!!!
    if member_length == 2:
      last_name = member_string[1]
      name = Name(rank, last_name)
    elif member_length == 3:
      if "." not in member_string[1]:
        last_name = trim_name(member_string[1], ",")
        first_initial = trim_name(member_string[2], ".")
      else:
        first_initial = trim_name(member_string[1], ".")
        last_name = member_string[2]
      name = Name(rank, last_name, first_initial)
    elif member_length == 4:
      if "." not in member_string[1]:
        last_name = trim_name(member_string[1], ",")
        first_initial = trim_name(member_string[2], ".")
        middle_initial = trim_name(member_string[3], ".")
      else:
        first_initial = trim_name(member_string[1], ".")
        middle_initial = trim_name(member_string[2], ".")
        last_name = member_string[3]
      name = Name(rank, last_name, first_initial, middle_initial)
    else:
      raise Exception(" ".join(member_string) + " in invalid format!")
      
    if include_reason:
      name.reason = reason
    member_names.append(name)
    
  member_names.sort()
      
  return "\n".join(member_names)