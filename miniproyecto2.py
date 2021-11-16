nombres=input("Ingrese los nombres de los jugadores de la siguiente manera:(nombre1) (nombre2)\n")

nombres_lista=nombres.split()

nombre1=nombres_lista[0][0:3].upper()
nombre2=nombres_lista[1][0:3].upper()

if nombre1==nombre2:
    nombre2+="2"

print("\n")
print(nombre1+" 501")
print(nombre2+" 501\n")

puntaje_y_lanzamientos1=[501,0,0,0]
puntaje_y_lanzamientos2=[501,0,0,0]

error=0

while puntaje_y_lanzamientos1[0]!=0 and puntaje_y_lanzamientos2[0]!=0:
    
    print("Ingrese los últimos 3 lanzamientos de "+nombres_lista[0]+" seguido de los últimos 3 lanzamientos de "+nombres_lista[1]+".")
    print("Debe ingresar: (multiplicador) (puntaje), Single Bull, Double Bull o Null (para lanzamiento perdido).\n")
    
    for i in range(1,4):
    
        lanzamientoi=input()
        if lanzamientoi.upper()=="SINGLE BULL":
            lanzamientoi=25
        elif lanzamientoi.upper()=="DOUBLE BULL":
            lanzamientoi=50
        elif lanzamientoi.upper()=="NULL":
            lanzamientoi=0
        else:
            multiplicacion=lanzamientoi.split()
            if int(multiplicacion[0])<1 or int(multiplicacion[0])>3 or int(multiplicacion[1])<1 or int(multiplicacion[1])>20:
                error=1

            lanzamientoi=int(multiplicacion[0])*int(multiplicacion[1])
        
        puntaje_y_lanzamientos1[i]=lanzamientoi
    
    puntaje_y_lanzamientos1[0]=puntaje_y_lanzamientos1[0]-puntaje_y_lanzamientos1[1]-puntaje_y_lanzamientos1[2]-puntaje_y_lanzamientos1[3]
    
    if puntaje_y_lanzamientos1[0]<0:
        puntaje_y_lanzamientos1[0]=abs(puntaje_y_lanzamientos1[0])
    
    for i in range(1,4):
        
        lanzamientoi=input()
        if lanzamientoi.upper()=="SINGLE BULL":
            lanzamientoi=25
        elif lanzamientoi.upper()=="DOUBLE BULL":
            lanzamientoi=50
        elif lanzamientoi.upper()=="NULL":
            lanzamientoi=0
        else:
            multiplicacion=lanzamientoi.split()
            if int(multiplicacion[0])<1 or int(multiplicacion[0])>3 or int(multiplicacion[1])<1 or int(multiplicacion[1])>20:
                error=1
            
            lanzamientoi=int(multiplicacion[0])*int(multiplicacion[1])
            
        puntaje_y_lanzamientos2[i]=int(lanzamientoi)

    puntaje_y_lanzamientos2[0]=puntaje_y_lanzamientos2[0]-puntaje_y_lanzamientos2[1]-puntaje_y_lanzamientos2[2]-puntaje_y_lanzamientos2[3]
    
    if puntaje_y_lanzamientos2[0]<0:
        puntaje_y_lanzamientos2[0]=abs(puntaje_y_lanzamientos2[0])
    
    if error==1:
        print("\n")
        print("Error al ingresar los lanzamientos (multiplicador o puntaje inexistentes).")
        print("El programa terminará.")
        break
    
    print("\n")
    print(nombre1+" "+str(puntaje_y_lanzamientos1[0]))
    print(nombre2+" "+str(puntaje_y_lanzamientos2[0])+"\n")
    
    if puntaje_y_lanzamientos1[0]==0 and puntaje_y_lanzamientos2[0]==0:
        print("Es un empate!")
    
    elif puntaje_y_lanzamientos1[0]==0:
        print("Gana "+nombres_lista[0]+"! Felicitaciones.")
        
    elif puntaje_y_lanzamientos2[0]==0:
        print("Gana "+nombres_lista[1]+"! Felicitaciones.")
        
    
    

