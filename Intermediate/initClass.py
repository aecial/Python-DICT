class Guest:
  # init method is used to assign values to the properties and operations of objects when it is created
  def  __init__(self, first, last, interest, phone):
    self.first = first
    self.last = last
    self.interest = interest
    self.phone = phone
    
p1 = Guest('Teddy', 'Pascual', 'Coding', '09982409945')

print(p1.phone)