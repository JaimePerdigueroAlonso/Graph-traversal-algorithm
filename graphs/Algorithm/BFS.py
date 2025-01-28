from Resources.Padre import Padre #Importamos la clase padre para poder utilizar las variables.

class BFS(Padre):

    def bfs(self):
        visited = [] #Creamos una lista vacía para poder almacenar los nodos visitados y asi no voler a pasar por ellos y no crear ciclos en el grafo
        self.path = [(self.start,[self.start], 0)] #Creamos una lista de tuplas, esta tupla consta de una variable que es el nodo en el que nos encontramos en el momento específico, una lista con el camino de nodos que llevamos y el costo almacenado que llevamos

        while self.path: #Mientras haya algun elemento en la cola
            current, path, cost = self.path.pop(0) #Extraemos la primera tupla de la lista, es decir la primera que se almacenó y almacenamos esos valores en current_node y path

            if current == self.finish: #Comprobamos si el nodo en el que nos encontramos es el destino, si es asi devolvemos el camino dee nodos que hemos utilizado
                return path, cost

            if current not in visited: #Comprobamos que el nodo no esta en la lista visited, es decir si ya lo hemos analizado antes
                visited.append(current) #Si el nodo no esta en la lista lo metemos
                for neighbor, costoso in self.station[current].items(): #Ahora recorremos todos los vecinos que tiene el nodo, es decir damos a neighbor el valor de cada vecino y lo analizamos uno a uno
                    self.path.append((neighbor, path + [neighbor], cost + costoso)) #Añadimos a la lista la tupla con el nodo en el que estamos en el momento y el camino que hemos relaizado hasta llegar a este con su coste

        return None 
