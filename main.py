from art import logo
print(logo)

def add(n1,n2):
  return n1+n2

def substract (n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def modulo(n1,n2):
  return n1%n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/":divide,
  "%":modulo
}
def calculator ():
  exit = False
  for operation in operations:
   print(operation)
  num1 = float(input("Dati primul numar "))  
  while not exit:  
     num2 = float(input("Dati urmatorul numar = "))
     symbol = input("Alege un operator (semn) pentru a efectua calculul : ")
     function = operations[symbol]
     answer = function(num1,num2)
     print(f" {num1} {symbol} {num2} = {answer}")
     if input(f"Scrie y pentru a continua cu {answer} sau n pentru a initia un nou calcul: ") == "y":
      num1 = answer
     else:
      exit = True
      calculator()
calculator()      
  
  
  
  