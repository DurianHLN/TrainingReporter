# This is a module.
# You can define variables and functions here, and use them from any form. For example:
#
#    import Module1
#
#    Module1.say_hello()
#

ranks = ["Col", "Lt. Col", "Maj", "Capt", "1stLt", "2ndLt", 
         "MGySgt", "SgtMaj", "HMCM", "1stSgt", "MSgt", "HMCS", "GySgt", "HMC", "SSgt", "HM1", 
         "Sgt", "HM2", "Cpl","HM3", "LCpl","HN", "PFC","HA", "Pvt", "HR", "SNA"]


def title(string):
  return "[b]" + string.upper() + "[/b]"