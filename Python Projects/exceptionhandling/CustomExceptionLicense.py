class tooOld:
  def __init__(self,msg):
    self.msg=msg

class tooYoung:
  def __init__(self,msg):
    self.msg=msg

age = int(input('Enter the age for License application'))

if age>90:
  raise tooOld('Too Old to drive')
elif age<18:
  raise tooYoung('Too Young to drive')
else:
  print('License can be issued. Age is valid')