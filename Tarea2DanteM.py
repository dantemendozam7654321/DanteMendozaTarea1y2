"DANTE.MENDOZA"
def OrdenacionRecursiva(unaLista):
   for llenarRanura in range(len(unaLista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if unaLista[ubicacion]>unaLista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = unaLista[llenarRanura]
       unaLista[llenarRanura] = unaLista[posicionDelMayor]
       unaLista[posicionDelMayor] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
OrdenacionRecursiva(unaLista)
print(unaLista)

