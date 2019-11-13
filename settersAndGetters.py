class X(object):
   def __init__(self):
      self.__x = None         # __ names are mangled, prepended with _ClassName. To call this attribute from a class instance would be classInstance._X__x
      self._mine = "Not set"  # variables to be used as setters and getters must be declared with at least one underscore!

   @property
   def x(self):
      print "getting x"
      return self.__x

   @property
   def mine(self):
      print "getting mine"
      return self._mine

   @x.setter
   def x(self, value):
      print "setting x"
      self.__x = value

   @mine.setter
   def mine(self, value):
      print "setting mine"
      self._mine = value

test = X()
print test.x
test.x = 1
print test.x

print "`" * 100

print test.mine
test.mine = "IS SET"
print test.mine
