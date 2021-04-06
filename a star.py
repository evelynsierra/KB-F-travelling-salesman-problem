from treelib import Node,Tree
import sys

# Class untuk merepresentasikan node tree di pelebaran A*
class TreeNode(object): 
        def __init__(self, c_no, c_id,  f_value, h_value, parent_id): 
            self.c_no = c_no
            self.c_id = c_id
            self.f_value = f_value
            self.h_value = h_value
            self.parent_id = parent_id

# Class untuk merepresentasikan node fringe di dalam list fringe A*
class FringeNode(object): 
        def __init__(self, c_no,  f_value): 
            self.f_value = f_value
            self.c_no = c_no


class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    # Fungsi untuk mencetak MST yang disimpan di dalam parent[]
    def printMST(self, parent, g, d_temp, t): 
        sum_weight = 0
        min1 = 10000
        min2 = 10000
        r_temp = {} #Reverse dictionary
        for k in d_temp:
        	r_temp[d_temp[k]] = k
        
        for i in range(1, self.V): 
            sum_weight = sum_weight + self.graph[i][ parent[i] ]
            if(graph[0][r_temp[i]] < min1):
            	min1 = graph[0][r_temp[i]]
            if(graph[0][r_temp[parent[i]]] < min1):
            	min1 = graph[0][r_temp[parent[i]]]
            if (graph[t][r_temp[i]] < min2):
            	min2 = graph[t][r_temp[i]]
            if(graph[t][r_temp[parent[i]]] < min2):
            	min2 = graph[t][r_temp[parent[i]]]
            
        return (sum_weight + min1 + min2)%10000

  
    # Fungsi untuk mencari vertex dengan jarak minimum dari sudut yang belum termasuk ke dalam tree shortest path
    def minKey(self, key, mstSet): 
  
        # Inisialisasi nilai minimal 
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Fungsi untuk mengonstruksi dan mencetak MST untuk sebuah graf yang direpresentasikan menggunakan matriks adjacency
    def primMST(self, g, d_temp, t): 
  
        # mengambil berat minimum edge 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array untuk menyimpan MST yang terkonstruksi
        # Buat key = 0 sehingga vertex yang diambil adalah vertex pertama
        key[0] = 0 
        mstSet = [False] * self.V 
        sum_weight = 10000
        parent[0] = -1 # Node pertama selalu dari root
  
        for c in range(self.V): 
   
            # Mengambil jarak minimum vertex dari set of sudut yang belum diproses.
            # u selalu sama dengan src di iterasi pertama
            u = self.minKey(key, mstSet) 
  
            # Meletakkan jarak vertex minimum di dalam shortest path tree
            mstSet[u] = True
  
            # Update nilai dist dari vertices terdekat untuk pengambilan vertex hanya jika jarak saat ini > jarak baru dan vertex tidak di dalam shortest path tree
            for v in range(self.V): 
                # graph[u][v] hanya non zero untuk vertices terdekat dari m
                # mstSet[v] bernilai false untuk vertices yang belum termasuk di dalam MST
                # Update key hanya jika graph[u][v] < key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        return self.printMST(parent,g,d_temp,t)
    

# Fungsi heuristic digunakan untuk membentuk graph dari semua node yang belum dilalui dan membuat Minimum Spanning Tree dari graph tersebut. 
# Memutuskan bobot dari MST dan menghubungkannya dengan node yang telah dilalui dan node pertama. 
#Untuk MST digunakan algoritma Prim.
def heuristic(tree, p_id, t, V, graph):
	visited = set()							# Set untuk menyimpan node yang telah dilalui
	visited.add(0)
	visited.add(t)
	if(p_id != -1):
		tnode=tree.get_node(str(p_id))
		# Mencari semua node yang telah dilalui dan menambahkannya ke dalam set
		while(tnode.data.c_id != 1):
			visited.add(tnode.data.c_no)
			tnode=tree.get_node(str(tnode.data.parent_id))
	l = len(visited)
	num = V - l								# Urutan node yang belum dilalui
	if (num != 0 ):
		g = Graph(num)
		d_temp = {}
		key = 0
		# d_temp menyimpan hasil pemetaan nomor kota sesungguhnya sebagai (key) dan nomor urut baru sebagai nilai agar Minimum Spanning Tree bekerja
		for i in range(V):
			if(i not in visited):
				d_temp[i] = key
				key = key +1
		
		i = 0
		for i in range(V):
			for j in range(V):
				if((i not in visited) and (j not in visited)):
					g.graph[d_temp[i]][d_temp[j]] = graph[i][j]
		
		mst_weight = g.primMST(graph, d_temp, t)
		return mst_weight
	else:
		return graph[t][0]

	 
def checkPath(tree, toExpand, V):
	tnode=tree.get_node(str(toExpand.c_id))		# Mengambil node dari tree untuk melebar
	list1 = list()								# List untuk menyimpan rute
	# Untuk node pertama
	if(tnode.data.c_id == 1):
		return 0
	else:
		depth = tree.depth(tnode)				# Mengecek kedalaman tree
		s = set()								# Set untuk menyimpan node di dalam rute
		# Berjalan ke atas dalam tree menggunakan parent pointer dan menambahkan semua node yang sejalan dengan set dan list
		while(tnode.data.c_id != 1):
			s.add(tnode.data.c_no)
			list1.append(tnode.data.c_no)
			tnode=tree.get_node(str(tnode.data.parent_id))
		list1.append(0)
		if(depth == V and len(s) == V and list1[0]==0):
			print("Path complete")
			list1.reverse()
			print(list1)
			return 1
		else:
			return 0

def startTSP(graph,tree,V):
	goalState = 0
	toExpand = TreeNode(0,0,0,0,0)		# Node untuk melebar
	key = 1								# Unique Identifier untuk sebuah node dalam tree
	heu = heuristic(tree,-1,0,V,graph)	# Heurisitic untuk node = 0 di dalam tree
	tree.create_node("1", "1", data=TreeNode(0,1,heu,heu,-1))		# Membuat node pertama
	fringe_list = {}					# Fringe List(Dictionary)(FL)
	fringe_list[key] = FringeNode(0, heu)							# Menambah node pertama di FL
	key = key + 1
	while(goalState == 0):
		minf = sys.maxsize
		# Pick node having min f_value from the fringe list
		for i in fringe_list.keys():
			if(fringe_list[i].f_value < minf):
				toExpand.f_value = fringe_list[i].f_value
				toExpand.c_no = fringe_list[i].c_no
				toExpand.c_id = i
				minf = fringe_list[i].f_value

		h = tree.get_node(str(toExpand.c_id)).data.h_value		#nilai h(n)
		val=toExpand.f_value - h								# nilai g(n)
		path = checkPath(tree, toExpand, V)						# mengecek node terpilih apakah sudah tidak ada cabang lagi atau masih ada
		# jika node yang melebar adalah 0 dan rutenya tidak ada child lagi, maka program selesai. 
		# Selain itu, kita mengecek node saat ekspansi dan bukan saat inisialisasi
		if(toExpand.c_no==0 and path==1):
			goalState=1
			cost=toExpand.f_value				
		else:
			del fringe_list[toExpand.c_id]		# Menghapus node dari List Fringe
			j=0
			# Menghitung f(n) dan h(n) dari node yang berdekatan untuk melebar
			while(j<V):
				if(j!=toExpand.c_no):
					h = heuristic(tree, toExpand.c_id, j, V, graph)			# Menghitung besar h(n)
					f_val = val + graph[j][toExpand.c_no] + h				# g(parent) + g(parent->child) + h(child)
					fringe_list[key] = FringeNode(j, f_val)
					tree.create_node(str(toExpand.c_no), str(key),parent=str(toExpand.c_id), data=TreeNode(j,key,f_val,h,toExpand.c_id))
					key = key + 1
				j=j+1
	return cost

if __name__ == '__main__':
	V = 4
	graph = [[-1,10,15,20],[10,-1,35,25],[15,35,-1,30],[20,25,30,-1]]
	tree = Tree()
	ans = startTSP(graph,tree,V)
	print("Ans is "+str(ans))
