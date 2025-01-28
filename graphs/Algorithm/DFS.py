from Resources.Padre import Padre #Importamos la clase padre para poder utilizar las variables 
 
class DFS(Padre): 
    
    def dfs(self, node = None, cost = 0): #Esta función cuando la llamamos en el menú no necesitamos poner ningun argumento
        if node is None: #Para el comienzo si el nodo inicial es None le damos el valor del primer nodo de entrada que lo hemos guardado al crear el objeto clase DFS
            node = self.start

        self.path.append(node) #Introducimos en nodo en la lista utilizando self para acceder a la clase padre

        if node == self.finish: #Para devolver los valores comprobamos si el nodo actual en el que estamos es igual al nodo de destino
            return self.path, cost #Devolvemos dos valores el path con los nodos almacenados y el coste que nos ha llevado llegar hasta ahí

        for current, costoso in self.station[node].items(): #Recorremos todos los vecinos del nodo, al primer valor de la clave se lo asignamos a la variable current y costoso
            if current not in self.path: #Esto lo ponemos para ver si ya hemos examinado el nodo en el que estamos
                result = self.dfs(current, cost + costoso) #Realizamos una llamada recursiva dondo el nodo actual y el cosoto desde el inicio hasta este
                if result is not None: #Comprobamos el valor del resultado si no es None devolvemos el resultado 
                    return result

        self.path.pop() #Retrocede en el camino si no encontramos un camino válido desde el nodo actual

        return None