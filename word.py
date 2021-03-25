import redis
import time
client = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0)

while True:

 time.sleep(1)
 print("Escoger una opción")
 print("A.Agregar nueva palabra")
 print("B.Editar palabra")
 print("C.ELiminar palabra")
 print("D.Buscar significado de palabra")
 print("E.Mostrar palabras")
 print("G.Salir")

 opc = str(input("Elegir "))

 if opc == 'A':
  p = input("Escribir la palabra que desea añadir ")
  s = input("Escribir el significado de la palabra ")
  client.hset("palabras",str(p), str(s))

 if opc == 'B':
  p = input("Escribir la palabra que desea editar ")
  w = input("Escribir la nueva palabra ")
  s = input("Escribir el nuevo significado de la palabra ")
  client.hdel("palabras",str(p))
  client.hset("palabras",str(w),str(s))
  
 if opc == 'D':
  p = input("Escribir la palabra que desea buscar ")
  w = client.hget("palabras",str(p))
  print(p,"=",w)
  
 if opc == 'C':
  p = input("Escribir la palabra que desea borrar ")
  client.hdel("palabras",str(p))
  
 if opc == 'E':
  w = client.hkeys("palabras")
  for x in w: 
   print(x)

 if opc == 'G':
  break 



  




