from anvil import *
from BBFormatter import *

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)
    
    self.ta_required_attendees.placeholder = "Cpl Wason\n1stLt C. Russell\nPFC Young, A. A."
    self.ta_non_required_attendees.placeholder = "LCpl Nguyen, D. L.\nPvt Akif"
    self.ta_absent.placeholder = "Cpl Page (LOA)\nPvt Evans, C. (Unexcused)\nLCpl Horta(Excused)"
    
    self.ta_training.placeholder = "We went to Athira and waited around for 30 min. ENDEX"
    self.ta_comments.placeholder = "LCpl Nguyen got the Marlboros instead of the Camels"
    self.ta_sustains.placeholder = "Good reaction to contact\nGot loadouts and lined up quickly"
    self.ta_improves.placeholder = "Shooting civilians"
    self.ta_signature.placeholder = "Sgt Allan\nSquad Leader\nGambler 2-2"
    
  def b_generate_click (self, **event_args):
    training_report = ""
    fillin_report = ""
    
    text_block = "{}\n{}\n\n"
    unit = text_block.format(title(self.l_unit.text), self.tb_unit.text)
    type_of_training = text_block.format(title(self.l_training_type.text), self.tb_training_type.text)
    date_conducted = text_block.format(title(self.l_date.text), self.tb_date.text)
    time_conducted = text_block.format(title(self.l_time.text), self.tb_time.text)
    
    def generate_location():
      location_text = self.tb_location.text
      if (self.tb_map.text):
        location_text += "," + self.tb_map.text
      return text_block.format(title(self.l_date.text), location_text)
    location = generate_location()
    
    def generate_required_attendees():
      attendee_names = self.ta_required_attendees.text.splitlines()
      for attendee_name in attendees_names:
         
    training_report = unit + type_of_training + date_conducted + time_conducted
    self.ta_training_report.text = training_report
    self.ta_training_report.visible = True
    self.ta_fillin_report.visible = True
      
  

  

