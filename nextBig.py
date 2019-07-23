'''
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
'''

from itertools import permutations
def next_bigger(n):
  x = []
  f = []
  oldN = []
  zeroExists = False
  long = False
  if n > 100000000:
    long = True
    for i in str(n):
      f.append(i)
    for i in range(0, 5):
      oldN.append(f[i])
      f[i] = 'a'
    while 'a' in f:
      f.remove('a')
    oldN = int(''.join(oldN))
    if f[0] == '0':
      zeroExists = True
    n = int(''.join(f))
  for p in permutations(str(n)):
    if int(''.join(p)) > n:
      x += [''.join(p)]
  if len(x) == 0:
    return -1

  if long == True:
    if zeroExists == False:
      return int(str(oldN) + str(int(min(x))))
    else:
      return int(str(oldN) + '0' + str(int(min(x))))
  else:
      return int(min(x))