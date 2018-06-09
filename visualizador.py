from leerDatos import leerGrafo
from TAD import Graph, Edge


def estado(g, f):
	
	print('el grafo:')

	
	#imprime la leyenda del grafo
	source = g.nodeIndex[g.source]
	sink = g.nodeIndex[g.sink]

	print('%9s'%'Fuente:', '%2s'%source)
	cabecera = '%9s'%'Fuente:' + '%2s'%source + '\n'
	f.write(cabecera)
	
	print('%9s'%'Destino:', '%2s'%sink)
	cabecera = '%9s'%'Destino:' + '%2s'%sink + '\n'
	f.write(cabecera)
	

	print(' u ->  v',  '%16s'%'flujo|capacidad')
	cabecera = 'u -> v' + '%21s'%'flujo|capacidad\n'		
	f.write(cabecera)


	#para cada arista, imprime su informacion

	for edge in g.edges:
		
		edge.flow = g.graph[g.nodeName[edge.v]][g.nodeName[edge.u]]

		print('%2s' % edge.u, '->','%2s'%edge.v,'%5s'%edge.flow, '|','%1s'%edge.capacity)
		line = ('%2s' % edge.u + '->' + '%2s'%edge.v + '%10s'%edge.flow+ '|' +'%1s'%edge.capacity+'\n')
		f.write(line)

def wrapper(filename):

	#crea o vacia el archivo de respuesta 
	outputname = 'respuesta' + filename
	open(outputname, 'a').close()
	f = open(outputname, 'r+')
	f.truncate()
	f.close()


	with open(outputname, 'a') as f:
		
		print('Nuevo grafo')
		print('==========================')
		f.write(('grafo de: ' + filename + '\n'))

		g = leerGrafo(filename)

		print('Antes de llenar', end = ' ')
		f.write('Antes de llenar\n')

		estado(g, f)

		maxflow = g.EdmondsKarp()

		print('Despues de llenar', end = ' ')
		f.write('\nDespues de llenar\n')

		estado(g, f)
		

		r = '\nEl maximo flujo de ' + g.nodeIndex[g.source] + ' a ' + g.nodeIndex[g.sink] + ' en el grafo es de ' + str(maxflow) + ' unidades'
		print(r)
		print('Respuesta guardada en', outputname)
		print('==========================')
		f.write(r)
