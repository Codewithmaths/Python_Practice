""" Solve all the possible number conversion in computer system """


"""first method: use build in function """
def numberConversion(num):
   binary = bin(num)
   octa = oct(num)
   hexa = hex(num)
   return binary, octa, hexa
if __name__ == "__main__":
   num = int(input("Enter a number: "))
   print(numberConversion(num))


"""second method: manual way"""

""" binary to decimal """
def binaryToDecimal1(binary):
   decimal = 0
   binary = binary[::-1]
   for i in range(len(binary)):
      if binary[i] == '1':
         decimal += 2**i
   return decimal 
if __name__ == "__main__":
   binary = input("Enter a binary number: ")
   print(binaryToDecimal1(binary))


def binaryToDecimal2(binary):
   decimal = 0
   for i in binary:
      decimal = decimal *2 + int(i)
   return decimal
if __name__ == "__main__":
   binary = input("Enter a binary number: ")
   print(binaryToDecimal2(binary))



""" decimal to binary """
def decimalToBinary1(n):
   if n == 0:
      return '0'
   binary = ''
   while n > 0:
      rem = n % 2
      binary = str(rem) + binary
      n //= 2
   return binary
if __name__ == "__main__":
   n = int(input("Enter a decimal number: "))
   print(decimalToBinary1(n))


""" octal to decimal"""
""" 1: Horner method """
def octalToDecimal1(octal):
   decimal = 0
   for i in octal:
      decimal = decimal * 8 + int(i)
   return decimal
if __name__ == "__main__":
   octal = input("Enter an octal number: ")
   print(octalToDecimal1(octal))
""" 2:manual method """
def octalToDecimal2(octal):
   decimal  = 0
   octal = octal[::-1]
   for i in range(len(octal)):
      decimal += int(octal[i]) * (8 ** i)
   return decimal
if __name__ == "__main__":
   octal = input("Enter an octal number: ") 
   print(octalToDecimal2(octal))


""" decimal to octal """
""" 1: manual method """
def decimalToOctal1(n):
   if n == 0:
      return '0'
   octal = ''
   while n > 0:
      rem = n % 8
      octal = str(rem) + octal
      n //= 8
   return octal
if __name__ == "__main__":
   n = int(input("Enter a decimal number: "))
   print(decimalToOctal1(n))  


""" decimal to hexadecimal """
def decimalToHexa1(n):
   if n == 0:
      return '0'
   hexa = ''
   hexa_chart = '0123456789ABCDEF'
   while n > 0:
      rem = n % 16
      hexa = hexa_chart[rem] + hexa
      n //= 16
   return hexa
if __name__=="__main__":
   n = int(input("Enter decimal number:"))
   print(decimalToHexa1(n))
   


""" hexadecimal to decimal"""
def hexadecimalToDecimal1(hexa):
   decimal  = 0
   hexa_chars = '0123456789ABCDEF'
   hexa = hexa.upper()

   for i in hexa:
      value = hexa_chars.find(i)
      decimal = decimal * 16 + value
   return decimal 
if __name__ == "__main__":
   hexa = input("Enter a hexadecimal number: ")
   print(hexadecimalToDecimal1(hexa))  

