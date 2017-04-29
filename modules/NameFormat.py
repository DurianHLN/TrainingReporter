# A module defining a member's name represented by his/her rank, last name, and first & middle initials (if needed).
#

class Name(object):
  ranks = {"Col": 1, "Lt. Col": 2, "Maj": 3, "Capt": 4, "1stLt": 5, "2ndLt": 6, 
      "MGySgt": 7, "SgtMaj": 8, "HMCM": 9, "1stSgt": 10, "MSgt": 11, "HMCS": 12, "GySgt": 13, "HMC": 14, "SSgt": 15, "HM1": 16, 
      "Sgt": 17, "HM2": 18, "Cpl": 19, "HM3": 20, 
      "LCpl": 21,"HN": 22, "PFC": 23,"HA": 24, "Pvt": 25, "HR": 26, 
      "SNA": 27}
  
  @staticmethod
  def checkRank(rank):
      if (Name.ranks.get(rank) == None):
        raise KeyError(rank + " is not a valid rank!")
      return rank
  
  def __init__(self, rank, last_name, first_inital="", middle_initial=""):
    self.rank = rank
    self.last_name = last_name
    self.first_initial = first_inital
    self.middle_initial = middle_initial
    self.reason = None
    
  def __str__(self):
    name = "{} {}".format(self.rank, self.last_name)
    if self.first_initial:
      name += ", {}.".format(self.first_initial)
      if self.middle_initial:
        name += " {}.".format(self.middle_initial)
    
    if self.reason:
        name += " " + self.reason
        
    return name
    
  def __lt__(self, other):
    return self.compare(other) < 0
  
  def __eql(self, other):
    return self.compare(other) == 0
  
  def __gt__(self, other):
    return self.compare(other) > 0
  
  def compare(self, otherName):
    
    Name.checkRank(self.rank)
    Name.checkRank(otherName.rank)
    
    def compareStrings(string1, string2):
      if string1 < string2:
        return -1
      elif string1 == string2:
        return 0
      elif string1 > string2:
        return 1
    return (Name.ranks[self.rank] - Name.ranks[otherName.rank] or
            compareStrings(self.last_name, otherName.last_name) or
            compareStrings(self.first_initial, otherName.first_initial) or
            compareStrings(self.middle_initial, otherName.middle_initial))

  