from anvil import *

from Formatter import *
from NameFormat import Name
import time

class MainForm (MainFormTemplate):
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
    unit = generate_text_block(self.l_unit, self.tb_unit)
    type_of_training = generate_text_block(self.l_training_type, self.tb_training_type)
    date_conducted = generate_text_block(self.l_date, self.tb_date)
    time_conducted = generate_text_block(self.l_time, self.tb_time)
    
    def generate_location():
      location_text = self.tb_location.text
      if location_text:
        if (self.tb_map.text):
          location_text += "," + self.tb_map.text
      else:
        location_text = self.tb_map.text
        
      return generate_text_block(self.l_location, location_text)
    location = generate_location()
    
    try:
      required_attendees = generate_text_block(self.l_required_attendees,
                                              generate_sorted_member_list(self.ta_required_attendees.text.splitlines()))
      non_required_attendees = generate_text_block(self.l_non_required_attendees,
                                                  generate_sorted_member_list(self.ta_non_required_attendees.text.splitlines()))
      absent = generate_text_block(self.l_absent,
                                  generate_sorted_member_list(self.ta_absent.text.splitlines(), include_reason=True))
    except Exception, e:
      alert(e.args)
      return
    training_conducted = generate_text_block(self.l_training, self.ta_training)
    comments = generate_text_block(self.l_comments, self.ta_comments)
    sustains = generate_text_block(self.l_sustains, self.ta_sustains)
    signature = "Respectfully submitted,\n\n" + self.ta_signature.text
    
    training_report = (unit + type_of_training + date_conducted + time_conducted + location
                      + required_attendees + non_required_attendees + absent
                      + training_conducted + comments + sustains + signature)
    
    training_report_link = generate_text_block("Training Report Link", "(Link here)")
    fillins = generate_text_block("Fill-Ins", generate_sorted_member_list(self.ta_non_required_attendees.text.splitlines()))
    fillin_report = (unit + type_of_training + date_conducted + time_conducted 
                     + training_report_link + fillins)
    
    self.ta_training_report.text = training_report
    self.ta_fillin_report.text = fillin_report
    self.ta_training_report.visible = True
    self.ta_fillin_report.visible = True

  def tb_unit_lost_focus (self, **event_args):
    if self.tb_training_type.text or not self.tb_unit.text:
      return
    if not self.ta_signature.text:
      self.ta_signature.text = "\n\n" + self.tb_unit.text

    dashes = self.tb_unit.text.count("-")
    training_types = {0: "Platoon", 1: "Squad", 2: "Fireteam"}
    if "4" in self.tb_unit.text:
      training_types[1] = "Section"
      training_types[2] = "Squad"
      training_types[3] = "Fireteam"
    
    self.tb_training_type.text = "Scheduled {} Training".format(training_types.get(dashes, "?"))

  def tb_date_show (self, **event_args):
    self.tb_date.text = time.strftime("%d%b%y").upper()
