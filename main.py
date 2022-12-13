def special_for(iterable):
  # the iter() function allows us to usee the next keyword
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

special_for([1,2,3])


#This is an example of how the built in range function works under the hood
class MyGen():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

      
gen = MyGen(0,100)
for i in gen:
  print(i)

  
