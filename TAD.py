import collections
 

class Edge():
	def __init__(self, u, v, capacity, flow=0):
		#cada arista tiene una entrada y una salida (grafo dirigido),
		#una capacidad y un flujo que no supera a su capacidad
		self.u = u
		self.v = v
		self.capacity = capacity
		self.flow = flow

class Graph:
  
	def __init__(self,):
		self.graph = list()		#grafo en represantacion de matriz
		self.numNodes = int()
		self.nodeName = dict()
		self.nodeIndex = dict()
		self.edges = list()
		self.source = int()
		self.sink = int()

  
	def BFS(self, camino):
		#devuelve si aun existe un camino de la fuente al destino en el grafo residual.
		#si existe, llena camino[] para guardar el camino
		

		# inicializa una lista de visitados con False para cada nodo 
		visited = [False] * (self.numNodes)
		 
		#cola
		queue = collections.deque()
		 
		# el nodo fuente en la cola y se marca como visitado
		queue.append(self.source)
		visited[self.source] = True
		 

		#mientras la cola no este vacia
		while queue:
			#extrae el vertice a procesar
			u = queue.popleft()

			#recorre todos los vertices adyacentes de u
			for ind, val in enumerate(self.graph[u]):
			#para cada uno, los marca como visitados, los acopla en el camino,
			#y los acola para ser procesados
				if val > 0 and not visited[ind]:
					visited[ind] = True
					camino[ind] = u
					queue.append(ind)
					
 
		#devuelve si ha logrado llegar al destino desde la fuente
		return visited[self.sink]
			 
	#implementacion del metodo de Ford-Fulkerson, 
	def EdmondsKarp(self):
 
		#lista de camino llenada por BFS
		camino = [-1] * (self.numNodes)
 
		flujoMaximo = 0
 
		#mientras exista un camino para aumentar desde la fuente al destino:
		while self.BFS(camino):

			#inicializa el flujo con un numero maximo
			flujoCamino = float("Inf")

			#recorre el camino encontrado por BFS y encuentra la capacidad residual minima
			#es decir, el el flujo maximo en ese camino
			s = self.sink
			while s != self.source:
				flujoCamino = min(flujoCamino, self.graph[camino[s]][s])
				s = camino[s]
 
			
			#en el camino, actualiza las capacidades residuales de cada arista en el camino recorrido
			v = self.sink
			while v !=  self.source:
				u = camino[v]
				self.graph[u][v] -= flujoCamino
				self.graph[v][u] += flujoCamino
				v = camino[v]

			#suma el flujo del camino al flujo maximo total
			flujoMaximo += flujoCamino
 
		return flujoMaximo