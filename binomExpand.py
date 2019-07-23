'''
The purpose of this kata is to write a program that can do some algebra. Write a function expand that takes in an expresion with a single, one character variable, and expands it. The expresion is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any one character long variable, and n is a natural number. If a = 1, no coeficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order. If the coeficient of a term is zero, the term should not be included. If the coeficient of a term is one, the coeficient should not be included. If the coeficient of a term is -1, only the "-" should be included. If the power of the term is 0, only the coeficient should be included. If the power of the term is 1, the carrot and power should be excluded.

Examples:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
'''
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def expand(expr):
  i = "a"
  pos = 0
  for j in range(0, 26):
     pos = expr.find(i)
     if pos!=-1:
       break
     p = ord(i)
     p+=1
     i = chr(p)
  x = expr.split("^")
  var = expr[pos]
  res = ""
  poly = x[0]
  poly = poly[1:-1]
  polN = poly.split(var)
  polNum = int(polN[1])#Number after x
  if polN[0]=="":
    coeff=1
  elif polN[0]=="-":
    coeff=-1
  else:
    coeff = int(polN[0]) #Coefficient of x
  power = int(x[1])
  if power==0:
    return "1"
  i = 0
  while i != power+1:
    resCoef = int(nCr(power, i)*(polNum**i)*coeff**(power-i))
    if resCoef>=0 and i!=0:
      res+="+"
    elif resCoef<0 and i!=0:
      res+="-"
    if resCoef==1 and i!=power:
      res+=var
    elif resCoef==-1 and i!=power:
      res+="-"+var
    elif i==0:
      res+=str(resCoef)+var
    else:
      res+=str(abs(resCoef))+var
    if power-i!=1:
      res+="^"+str((power-i))
    i+=1
  res = res[0:-3]
  return res