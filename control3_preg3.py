def potencia(num,exp):
   if exp==0:
       return 1 
   else:
       return num*potencia(num,exp-1)
print("la potencia de 5 elevado a 3 es:",potencia(5,3))