class Padre:

    def __init__(self,station, start, finish): 
        self.station = station
        self.start = start
        self.finish = finish
        self.path = []

#De esta clase heresaran las clases DFS, BFS y Astar ya que son variables que comparten todos en común,
#a esta fución le pasamos el grafo, la entrada y la salida y luego inicializamos una lista vacía para el path
        
