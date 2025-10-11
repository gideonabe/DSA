class Car:
  # constructor - uses dunder method (because it uses double underscore)
  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def drive(self):
    print(f"You drive the {self.color} {self.model}")

  