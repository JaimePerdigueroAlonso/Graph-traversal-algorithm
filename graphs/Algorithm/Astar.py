from Resources.Padre import Padre #Importamos la clase padre para poder utilizar las variables.

class ASTAR(Padre):

    def Astar(self):
        heuristica = 0 #Damos el valor a la heurística, en este caso es 0 ya que no la conocemos
        visited = [] #Creamos una lista para guardar los nodos que hemos utilizado para no volver a analizarlos
        self.path = [(self.start,[self.start], 0)] #En el path que nos da la clase padre metemos la primera tupla que consta de: el primer nodo de comienzo, una lista con los nodos que hemos visitado hasta llegar a ese nodo y el costo que voy acumulando
        path_final = [] #Esta lista la creamos para guardar todos los caminos posibles hasta el destino

        while self.path: #Mientras haya algun elemento en la lista path se ejecuta el while
            current, path, cost = self.path.pop(0) #Sacamos los valores de la lista y se lo asignamos a las variables current, path, cost
            if current == self.finish: #Si el nodo en el que estamos es el final metemos en la lista final el camino y el coste para comprobarlos despues 
                path_final.append((path,cost))

            if current not in visited: #Añadimos en la lista de visited el nodo en el que estamos para no volver a analizarlo
                visited.append(current) 
                for neighbor, costoso in self.station[current].items(): #Guardamos en neighbor y costoso los valores de los vecino del nodo en el que estamos, es decir, primero será el primer vecino y el costo, luego el segundo...
                    self.path.append((neighbor, path + [neighbor], cost + costoso + heuristica)) #Vamos añadiendo a la lista path el nuevo nodo con el camino hasta llegar a el y el costo hasta llegar a el

        #Buscamos el camino menos costoso
        path_lowercost = path_final[0][0] #Le damos el valor a el camino con menos costo a el primer camino que termina en el destino que queremos
        lower_cost = path_final[0][1] #Le damos el valor del menor coste a el primer costo del primer camino 
        for path, cost in path_final: #Ahora analizamos los demas caminos y vemos si encontramos un coste menor que el primero asignado, si es asi cambiamos el valor del camino mas barato a el nuevo encontrado
            if(cost < lower_cost):
                lower_cost = cost
                path_lowercost = path

        return path_lowercost, lower_cost #Devolvemos el camino que menos costo ha requerido
    
#En este algoritmo necesitarimos una heurística para saber por donde decidimos ir estimando el coste, en este caso no se nos da 
# por ello en vez de hacer otro algoritmo para estimar ese valor que sería ineficiente simplemente pongo que heucaristica es igual a 0
     