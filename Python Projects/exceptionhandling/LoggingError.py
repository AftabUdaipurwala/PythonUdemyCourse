import logging

logging.basicConfig(filename='mylog.log', level = logging.DEBUG) # all logs above debug will be logged in the mylog file

try:
  f = open('exceptionfile','w')
  a,b= [int(x) for x in input('Enter 2 numbers : ').split()]
  c = a/b
  logging.info('Division in progress')
  print(c)
  f.write('writing in %d file'%c) # here %d means digit calculated and stored in the c variable
except ZeroDivisionError: # this takes care of only zero division error
  print("Divided by 0, hence wont run, please enter non zero 2nd number")
  logging.error('Division by 0')
except: # this takes care of all kinds of error
  print("Invalid input")
  logging.error('Invalid error')
else: # use this only when we want certain logic to be executed only when no exceptions are raised
  print('No Exception raised')

finally:
  f.close()
  print('File closed')

