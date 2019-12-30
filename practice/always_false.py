# An if statement that is always false is called a contradiction. 
# You will rarely want to do this while programming, but it is 
# important to realize it is possible to do this.

def always_false(num):
  if (num > 0) and (num < 0):
    return True
  else:
    return False

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
