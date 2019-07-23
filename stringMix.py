'''
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
'''

def mix(s1, s2):
  key = {}
  key2 = {}
  res1 = {}
  res2 = {}
  resE = {}
  resComb = {}
  s1 = sorted(s1)
  s2 = sorted(s2)
  res = ""
  for a in s1:
    if a.isalpha() and a.islower():
      try:
        key[a]+=1
      except:
        key[a]=1
  for a in s2:
    if a.isalpha() and a.islower():
      try:
        key2[a]+=1
      except:
        key2[a]=1
  for a in key:
    if key[a] > 1:
      try:
        if key2[a] > key[a]:
          res2[a]=a*key2[a]
        if key2[a] < key[a]:
          res1[a]=a*key[a]
        if a in key2 and key[a]==key2[a]:
          resE[a]=a*key[a]
      except:
        res1[a]=a*key[a]
  for a in key2:
    if key2[a] > 1:
      if a in key and key2[a] > key[a]:
          res2[a]=a*key2[a]
      if a not in key:
          res2[a]=a*key2[a]
  for a in sorted(res1.keys()):
    try:
      resComb[len(res1[a])]+=["1:"+res1[a]+"/"]
    except:
      resComb[len(res1[a])]=["1:"+res1[a]+"/"]
  for a in sorted(res2.keys()):
    try:
      resComb[len(res2[a])]+=["2:"+res2[a]+"/"]
    except:
      resComb[len(res2[a])]=["2:"+res2[a]+"/"]
  for a in sorted(resE.keys()):
    try:
      resComb[len(resE[a])]+=["=:"+resE[a]+"/"]
    except:
      resComb[len(resE[a])]=["=:"+resE[a]+"/"]
  for a in sorted(resComb.keys(), reverse=True):
    res+="".join(resComb[a])
  return res[0:-1]