#Code to calculate square of a given integer
def square(x):
 """
 This function creates the square of given
 integer

 
 :param x: 
 :return: square of a number

 
 """
 if x<=0:
  return "This function only accepts x >=0. Please change x"
 else :
  return x*x
 
def cube(x):
  """
 
  :param x:
  :return: cube of a number
  """
  return x*x*x


print(square(3))

