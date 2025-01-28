from Algorithm.DFS import DFS
from Algorithm.BFS import BFS
from Algorithm.Astar import ASTAR
#Importamos todas las clases para poder utilizar sus funciones

class Menu():
    def __init__(self,station):
        self.station = station
        self.start = None
        self.finish = None
#Al crear la clase le daremos el grafo y crearemos las variables nulas de inicio y destino 
         
    def menu(self):
        answer = "0" #Inicializamos answer para poder meternos en el bucle while
        check = False

        while not check: #Con esto simplemente vemos si las entradas del usuario existen, si no es así volvemos a pedir que las introduzcan
            self.start = input ("Introduzca el punto de partida:") #Pedimos al usuario el inicio y el destino y lo guardamos en las variables de la clase
            self.finish = input ("Introduzca el destino:")

            if self.start not in self.station or self.finish not in self.station:
                print("Esta estación no existe")
            else: check = True #Si las entradas estan en el grafo, check será true por lo que no volverá a entrar en el bucle while


        while answer != "6": #Se ejecutará este código hasta que la respuesta sea 6 que es el mensaje de salida 
            print("Opciones:")
            print("1.- Algoritmo BFS")
            print("2.- Algoritmo DFS")
            print("3.- Algoritmo A*")
            print("4.- Todos los algoritmos")
            print("5.- Cambiar inicio y final")
            print("6.- Salir")
            answer = input("Respuesa -> ") #Guardamos la respuesta del usuario en answer 

            if answer == "1": #Si la respuesta es 1
                route = BFS(self.station, self.start, self.finish) #Creamos un objeto BFS y damos los valores del grafo, el inicio y destino
                path, cost= route.bfs() #Guardamos lo que nos devuelve la función bfs del objeto BFS y lo gurdamos en dos variables
                print("------BFS------")
                print("Camino: ", path)
                print("Coste:", cost) #Imprimimos por pantalla la lista con los nodos utilizados para llegar al destino y su costo

            elif answer == "2": #Si la respuesta es 2
                route = DFS(self.station, self.start, self.finish) #Creamos un objeto DFS y damos los valores del grafo, el inicio y destino
                path, cost= route.dfs() #Guardamos lo que nos devuelve la función dfs del objeto DFS y lo guardamos en dos variables
                print("------DFS------")
                print("Camino: ", path)
                print("Coste:", cost)

            elif answer == "3": #Si la respuesta es 3
                route = ASTAR(self.station, self.start, self.finish) #Creamos un objeto ASTAR y damos los valores del grafo, el inicio y destino
                path, cost = route.Astar() #Guardamos lo que nos devuelve la función Astar del objeto ASTAR y lo gurdamos en dos variables
                print("------ASTAR------")
                print("Camino: ", path)
                print("Coste:", cost)

            elif answer == "4": #Si la respuesta es 4
                route = BFS(self.station, self.start, self.finish)
                path, cost= route.bfs()
                print("------BFS------")
                print("Camino: ", path)
                print("Coste:", cost)

                route = DFS(self.station, self.start, self.finish)
                path, cost= route.dfs()
                print("------DFS------")
                print("Camino: ", path)
                print("Coste:", cost)

                route = ASTAR(self.station, self.start, self.finish)
                path, cost = route.Astar()
                print("------ASTAR------")
                print("Camino: ", path)
                print("Coste:", cost)

            elif answer == "5": #Si la respuesta es 5
                check = False
                while not check: 
                    self.start = input ("Introduzca el punto de partida:") 
                    self.finish = input ("Introduzca el destino:")

                    if self.start not in self.station or self.finish not in self.station:
                        print("Esta estación no existe")
                    else: check = True


            elif answer == "6": #Si la respuesta es 6, despues de esto saldremos del bucle while
                print("Adios!")

    
