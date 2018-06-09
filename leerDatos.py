from TAD import Graph, Edge


def leerGrafo(textfile):

	#se leen los datos y se almacenan localmente

	with open(textfile) as f:
		content = f.readlines()
	content = [x.strip() for x in content] 
	for i, line in enumerate(content):
		if line == 'EDGES':
			ind = i
			break
	edges = content[ind+1:]
	nodes = content[:ind]



	g = Graph()


	#se leen los nodos, y se inicializa la matriz del grafo  con ceros y la cantidad de nodos 
	for i in range(len(nodes)):
		row = []
		for j in range(len(nodes)):
			row.append(0)
		g.graph.append(row)

	g.numNodes = len(nodes)

	
	#se almacena el diccionario de nombres indices de nodos, la fuente y el destino
	ind = 0
	for u in nodes:
		g.nodeName[u] = ind
		g.nodeIndex[ind] = u
		ind += 1

	g.source = 0
	g.sink = ind-1


	#se leen las aristas, y se llena la matriz con las capacidades de cada arista 
	for e in edges:
		u, v, cap = e.split()
		arista = Edge(u,v,cap)
		g.edges.append(arista)
		g.graph[g.nodeName[u]][g.nodeName[v]] = int(cap)

	
	return g