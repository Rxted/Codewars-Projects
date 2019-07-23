'''
You are writing an encoder/decoder to convert between javascript strings and a binary representation of Morse code.

Each Morse code character is represented by a series of "dots" and "dashes". In binary, a dot is a single bit (1) and a dash is three bits (111). Between each dot or dash within a single character, we place a single zero bit. (I.e. "dot dash" would become 10111.) Separate characters are separated by three zero bits (000). Words are spearated by a single space, which is represented by 7 zero bits (0000000).


Formal Syntax
Binary Morse code has the following syntax: (Where '1' and '0' are literal bits.)
    message    ::= word
                 | word 0000000 message

    word       ::= character
                 | character 000 word

    character  ::= mark
                 | mark 0 character

    mark       ::= dot
                 | dash

    dot (·)    ::= 1

    dash (–)   ::= 111
'''

class Morse:
    @classmethod
    def encode(self,message):
		binRep = []
		for i in message:
			if i == ' ':
				del binRep[-1]
				binRep.append('0000000')
			else:
				binRep.append(Morse.alpha[i])
				binRep.append('000')
		binRep = ''.join(binRep)
		binSep = []
		f = 32
		binSep = [binRep[i:i+f] for i in range(0, len(binRep), f)]
		for i in range(0, len(binSep)):
			while len(binSep[i])!=32:
				binSep[i]+='0'
		intSep = []
		for i in binSep:
			f = int(i,2)
			if(f & 0x80000000):#yep
				f = -0x100000000 + f
			intSep.append(f)
		return intSep
    @classmethod
    def decode(self,array):
		binRep = []
		for i in array:
			binRep.append(bin(((1 << 32) - 1) & i))
		fixBinRep = []
		for i in binRep:
			fixBinRep.append(str(i).replace('0b', ''))
		for i in range(0, len(fixBinRep)):
			while len(fixBinRep[i])!=32:
				fixBinRep[i] = '0' + fixBinRep[i]
		binRep = ''.join(fixBinRep)
		binSep = []
		charList = []
		words = binRep.split('0000000')
		for i in words:
			binSep = i.split('000')
			for x in binSep:
				if x == '':
					break
				if x in list(Morse.alpha.values()):
					charList.append(list(Morse.alpha.keys())[list(Morse.alpha.values()).index(x)])
			if x != '':
				charList.append(' ')
		if charList != [' ']:
			while charList[-1] == ' ':
				del charList[-1]
		return ''.join(charList)
    
    alpha={
  'A': '10111',
  'B': '111010101',
  'C': '11101011101',
  'D': '1110101',
  'E': '1',
  'F': '101011101',
  'G': '111011101',
  'H': '1010101',
  'I': '101',
  'J': '1011101110111',
  'K': '111010111',
  'L': '101110101',
  'M': '1110111',
  'N': '11101',
  'O': '11101110111',
  'P': '10111011101',
  'Q': '1110111010111',
  'R': '1011101',
  'S': '10101',
  'T': '111',
  'U': '1010111',
  'V': '101010111',
  'W': '101110111',
  'X': '11101010111',
  'Y': '1110101110111',
  'Z': '11101110101',
  '0': '1110111011101110111',
  '1': '10111011101110111',
  '2': '101011101110111',
  '3': '1010101110111',
  '4': '10101010111',
  '5': '101010101',
  '6': '11101010101',
  '7': '1110111010101',
  '8': '111011101110101',
  '9': '11101110111011101',
  '.': '10111010111010111',
  ',': '1110111010101110111',
  '?': '101011101110101',
  "'": '1011101110111011101',
  '!': '1110101110101110111',
  '/': '1110101011101',
  '(': '111010111011101',
  ')': '1110101110111010111',
  '&': '10111010101',
  ':': '11101110111010101',
  ';': '11101011101011101',
  '=': '1110101010111',
  '+': '1011101011101',
  '-': '111010101010111',
  '_': '10101110111010111',
  '"': '101110101011101',
  '$': '10101011101010111',
  '@': '10111011101011101',
  ' ': '0'}