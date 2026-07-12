class Phone:
  def __init__(self,brand,color,battery):
    self.brand=brand 
    self.color=color 
    self.battery=battery 
  def __repr__(self):
    return f"Phone(brand={self.brand!r}, color={self.color!r}, battery={self.battery!r})"
apple=Phone("I-phone","Black",4500)
realme=Phone("Realme","Blue",6500)
print(apple)
print(realme)
print(apple.battery)
