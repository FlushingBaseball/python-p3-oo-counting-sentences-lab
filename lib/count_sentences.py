#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) ==str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
      if self.value.endswith("."):
        return True
      else: 
        return False
      
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else: 
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    without_spaces = self.value.replace(" ", "")
    print(without_spaces)
    sentance_array = re.split("[!?\.]+", without_spaces) 
    print(sentance_array)
    for sentance in sentance_array:
      if sentance ==(""):
        sentance_array.remove(sentance)
    print(sentance_array)
    return(len(sentance_array))

  value = property(get_value, set_value)
