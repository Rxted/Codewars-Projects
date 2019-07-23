'''
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac". The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s

unique letters (2 <= length <= 26)

[output] a string

middle permutation.

'''
def middle_permutation(string):
  string = ''.join(sorted(string))
  strlist = []
  strlen = len(string)
  midPerm = []
  for i in string:
    strlist.append(i)
  if strlen%2 == 0:
    midPerm.append(strlist[int(strlen/2)-1])
    del strlist[int(strlen/2)-1]
    strlen-=1
    while strlen != 0:
      midPerm.append(strlist[strlen-1])
      del strlist[strlen-1]
      strlen-=1
  else:
    midPerm.append(strlist[int((strlen/2)+0.5)-1])
    del strlist[int((strlen/2)+0.5)-1]
    strlen-=1
    midPerm.append(strlist[int(strlen/2)-1])
    del strlist[int(strlen/2)-1]
    strlen-=1
    while strlen != 0:
      midPerm.append(strlist[-1])
      del strlist[-1]
      strlen-=1
  return ''.join(midPerm)