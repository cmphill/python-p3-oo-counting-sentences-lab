#!/usr/bin/env python3
class MyString:
  def __init__(self,value = ""):
    self.value = value
  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False
  def is_question(self):
    if self._value.endswith("?"):
      return True
    else:
      return False
  def is_exclamation(self):
    if self._value.endswith("!"):
      return True
    else:
      return False
  def count_sentences(self):
    value = self.value
    for ends in ["?", "!"]:
      value = value.replace(ends, ".")
    sentences = [sentence for sentence in value.split(".") if sentence]
    return len(sentences)

  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):
      self._value= value
    else:
      print("The value must be a string.")
      
  value = property(get_value, set_value)
  