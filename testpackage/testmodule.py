import sys
class testclass:
 @staticmethod
 def works():
  return sys.version

 @staticmethod
 def broken():
  import greet
  greet.greet('World')
  return sys.platform
