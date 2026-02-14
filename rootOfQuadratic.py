""" Root Of Quadratic Equation """
import math 
def root_of_quadratic(a, b, c):
      """ Return the roots of a quadratic equation ax^2 + bx + c = 0 """
      d = b**2 - 4*a*c
      sqrt_d = math.sqrt(abs(d))

      if d > 0:
         print("Two distinct real roots:")
         print((-b+sqrt_d)/(2*a),"and",(-b-sqrt_d)/(2*a))
      
      elif d == 0:
         print("One real root:")
         print(-b/(2*a))
      
      else:
         print("Two complex roots:")
         real_part = -b /(2*a)
         imgarinary_part = sqrt_d / (2*a)
         print(f"{real_part} + {imgarinary_part}i and {real_part} - {imgarinary_part}i")

if __name__ == "__main__":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    root_of_quadratic(a, b, c)