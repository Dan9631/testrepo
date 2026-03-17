"""
#Funcionamiento a nivel del ciclo for 
squares = ["red","yellow","green","purple","blue"]
print(f"Antes: {squares}")

for i,square in enumerate(squares):
    print(i,' ',square)

print(f"Despues: {squares}")

#Funcionamiento a nivel del ciclo While
squares=['orange','orange','purple','blue']
newSquares=[]
i=0
print(f'Arreglo original {squares}')
while(squares[i]=='orange'):
    newSquares.append(squares[i])
    i=i+1
print(f"Arreglo de cuadros {newSquares}")

"""

#Ejercicios laboratorio
#Ejercicio2
Genres=['rock','R&B','Soundtrack','R&B','soul','pop']
for genre in Genres:
    print(genre)

print("-----------------------------------------------------")
#Ejercicio3
playListRatings= [10,9.5,10,8,7.5,5,10,10]
i=0
while(playListRatings[i] > 5 or i > len(playListRatings)):
    print(playListRatings[i])
    i=i+1


print("-----------------------------------------------------")
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(squares[i]=='orange'):
    new_squares.append(squares[i])
    i=i+1

print(new_squares)

#Ejercicio4
for i in range(1,11):
    print(f" 7  * {i} = {7*i}\t\t   6  * {i} = {6*i}")

#Ejercicio5
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_Animals = []
i=0
while(i<len(Animals)):
    if(len(Animals[i]) == 7):
        new_Animals.append(Animals[i])
    i = i + 1
print(new_Animals)

