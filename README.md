# KB-F-travelling-salesman-problem #
## Anggota Kelompok ##

NRP | NAMA | Pembagian Kerja
------------- | ------------- | --------------
05111940000111  | Evelyn Sierra | Uninformed Search (DFS, UCS Search)
05111940000042  | Bayu Eka Prawira | Informed Search (Greedy-Best First Search, A*)

## Pendahuluan ##
The travelling salesman problem (atau yang biasa disebut dengan TSP) menanyakan pertanyaan berikut: "Diberikan daftar kota dan jarak antara setiap pasangan kota, apa rute terpendek yang mungkin mengunjungi setiap kota tepat satu kali dan kembali ke kota asal? " 
Untuk memecahkan masalah ini, digunakan informed search dan uninformed search. Khusus untuk uninformed search, setiap salesman tersebut pernah mengunjungi kota tersebut, kota itu akan ditandai sehingga tidak memunculkan looping yang berulang.

## Using DFS Search ##
Langkah pertama adalah memasukkan total vertices dan total edges yang diinginkan. Kemudian gunakan looping untuk membuat isi Graph menjadi 0. 
```C
printf("Minimum cost\n");
	printf("Input total vertices: ");
	scanf("%d", &V);

	// Ubah isi Graph menjadi 0
	for (i = 0; i <= V; i++)
	{
		for (j = 0; j <= V; j++)
		{
			G[i][j] = 0;
		}
	}

	printf("Input total edges: ");
	scanf("%d", &E);
```

Selanjutnya, untuk setiap edge tambahkan cost. Kemudian, cost tersebut akan menjadi nilai dari setiap array 2-dimensi `G[i][j]`.
```C
for (i = 0; i < E; i++)
	{
		printf("Enter the edges(V1 V2 Cost) : ");
		scanf("%d %d %d", &v1, &v2, &c);
		G[v1][v2] = c;
	}
```

Masukkan nilai source dan destination yang diinginkan. Apabila nilai source atau destination lebih besar daripada jumlah vertices, hasilnya tidak akan keluar. Sebaliknya, function `DFS()` akan berjalan dengan memasukkan parameter `source`
```C
printf("\nEnter the source: ");
	scanf("%d", &source);
	printf("Enter the destination: ");
	scanf("%d", &dest);
	dest = dest;

	if (source > V || dest > V)
	{
		printf("Wrong input\n");
	}
	else
	{
		DFS(source);
		if (found == 1)
		{
			printf("%d Cost: %d\n", dest, cost);
		}
		else
		{
			printf("\nThere's no way\n");
		}
	}
```
Pada function `DFS()`, tandai visited[i] = 1, sebagai tanda telah dikunjungi, dan lakukan looping.
```C
void DFS(int i)
{
	int j;
	visited[i] = 1;

	printf("%d -> ", i);
	for (j = 1; j <= V; j++)
	{
		//		printf("j: %d\n",j);
		if (G[i][j] != 0 && visited[j] == 0)
		{
			cost = cost + G[i][j];
			//			printf("j yang masuk %d\n",j);
			if (j != dest)
			{
				if (j != V)
				{
					DFS(j);
				}
				else
				{
					printf("%d\n", j);
					cost = 0;
					DFS(source);
				}
			}
			else
			{
				found = 1;
				break;
			}
		}

		if (found == 1)
		{
			break;
		}
	}
}
```
Jika `G[i][j]` memiliki isi, dan `visited[j]` belum pernah ditandai, cost akan ditambah. Jika `j` belum mencapai destinasi yang dituju dan belum mencapai maksimal vertices yang ditentukan, function `DFS()` tetap akan dilanjutkan. Jika destinasi belum tercapai tapi telah mencapai maksimal vertices, maka DFS akan ulang dari source. 

Dari penjelasan diatas, dapat disimpulkan bahwa DFS tidak dapat mendapatkan nilai minimum cost, karena DFS tidak bisa balik ke keadaan semula dan membandingkan seluruh jalan yang telah dilewati.


## Using UCS Search ##
Uniform-Cost Search adalah variant dari algoritma Dijikstra. Di dalam codingan ini, kita hanya memasukkan source saja dan memasukkan satu per satu apabila diperlukan. Setiap langkahnya, akan dicek apakah sudah berada di dalam array. Jika iya, maka key akan di kurangi, Jika tidak, maka kita memasukkannya.

Penjelasan codingannya adalah sebagai berikut.
Langkah pertama adalah menginisiasi `graph`, `edge`, dan `cost`
```C
 graph.resize(7);
 
    // add edge
    graph[0].push_back(1);
    graph[0].push_back(3);
    graph[3].push_back(1);
    graph[3].push_back(6);
    graph[3].push_back(4);
    graph[1].push_back(6);
    graph[4].push_back(2);
    graph[4].push_back(5);
    graph[2].push_back(1);
    graph[5].push_back(2);
    graph[5].push_back(6);
    graph[6].push_back(4);
 
    // add the cost
    cost[make_pair(0, 1)] = 2;
    cost[make_pair(0, 3)] = 5;
    cost[make_pair(1, 6)] = 1;
    cost[make_pair(3, 1)] = 5;
    cost[make_pair(3, 6)] = 6;
    cost[make_pair(3, 4)] = 2;
    cost[make_pair(2, 1)] = 4;
    cost[make_pair(4, 2)] = 4;
    cost[make_pair(4, 5)] = 3;
    cost[make_pair(5, 2)] = 6;
    cost[make_pair(5, 6)] = 3;
    cost[make_pair(6, 4)] = 7;
```

Setelah itu, buatlah goal state dan set goal tersebut. Untuk mendapatkan jawabannya, kita gunakan function `uniform_cost_search()`
```C

    vector<int> goal;
 
    goal.push_back(6);

    vector<int> answer = uniform_cost_search(goal, 0);
```

Pada function `uniform_cost_search()`, kita akan menggunakan priority queue. Set semua isi vector ke value maksimal. Selanjutnya, kita akan membuat index awal. Untuk menyimpan node yang telah kunjungi, kita menggunakan `map<int, int> visited`.

```C
    vector<int> answer;

    priority_queue<pair<int, int> > queue;

    for (int i = 0; i < goal.size(); i++)
    {
    	answer.push_back(INT_MAX);
    }

    queue.push(make_pair(0, start));
 
    map<int, int> visited;

    int count = 0;
```
Saat queuenya tidak kosong, kita akan mengambil nilai yang teratas dari queue tersebut. Setelah itu, kita akan mengecek apakah elemen tersebut bagian dari goal. 
```C
while (queue.size() > 0) {
        pair<int, int> p = queue.top();

        queue.pop();

        p.first *= -1;

        if (find(goal.begin(), goal.end(), p.second) != goal.end()) {

            int index = find(goal.begin(), goal.end(),
                             p.second) - goal.begin();

            if (answer[index] == INT_MAX)
                count++;

            if (answer[index] > p.first)
                answer[index] = p.first;

            queue.pop();

            if (count == goal.size())
                return answer;
        }

        if (visited[p.second] == 0)
            for (int i = 0; i < graph[p.second].size(); i++) {

                queue.push(make_pair((p.first +
                  cost[make_pair(p.second, graph[p.second][i])]) * -1,
                  graph[p.second][i]));
            }

        visited[p.second] = 1;
    }
 
    return answer;
```
Untuk mendapatkan posisi yang sedang ditempati
```C
int index = find(goal.begin(), goal.end(),
                             p.second) - goal.begin();
```
Jika goal terbaru telah tertuju, maka `count` akan ditambah
```C
if (answer[index] == INT_MAX)
                count++;
```
Dan pada saat `cost` lebih kecil, maka
```C
 if (answer[index] > p.first)
          answer[index] = p.first;
```
jika seluruh goal telah tercapai, maka akan return `answer`. Sedangkan untuk mengecek nodes yang belum dikunjungi menggunakan kondisi berikut
```C
if (visited[p.second] == 0)
            for (int i = 0; i < graph[p.second].size(); i++) {

                queue.push(make_pair((p.first +
                  cost[make_pair(p.second, graph[p.second][i])]) * -1,
                  graph[p.second][i]));
```
Apabila nodes telah dikunjungi, maka array `visited[i]` akan bernilai 1. 

# Informed Search #

## Using Greedy-Best First Search ##

Algoritma *Greedy* adalah sebuah algoritma yang memecahkan masalah langkah demi langkah, pada setiap langkah:
1. Mengambil pilihan yang terbaik yang dapat diperoleh saat program itu berjalan.
2. Terdapat harapan dengan memilih lokal optimum pada setiap langkah akan mencapai global optimum. Di dalam algoritma ini, diasumsikan bahwa lokal optimum merupakan bagian dari global optimum.

Berikut adalah implementasi *Greedy* untuk problem Travelling Salesman Problem

Input Testcase :
```
-1 10 15 20
10 -1 35 25
15 35 -1 30
20 25 30 -1
```

Langkah pertama yang dilakukan adalah memasukkan input testcase yang sudah didefinisikan di dalam code :
```CPP
int main()
{
	vector<vector<int> > tsp = { { -1, 10, 15, 20 },
								 { 10, -1, 35, 25 },
								 { 15, 35, -1, 30 },
								 { 20, 25, 30, -1 } };
	findMinRoute(tsp);
	return 0;
}
```
Lalu memanggil fungsi ```findMinRoute(tsp)``` untuk melanjutkan proses pencarian minimal cost dan dengan mem-*passing* parameter vector yang berisi inputan testcase. 

Di dalam fungsi ```findMinRoute```, terjadi proses inisialisasi map yang digunakan untuk menandai bahwa rute tersebut sudah dilalui. Node 0 dianggap sebagai start state sehingga dianggap telah dilalui, oleh karena itu diinisialisasi dengan 1. \
Kemudian menginisialisasi array yang digunakan untuk menyimpan alur route yang dilalui sebesar ukuran vector tsp.
```CPP
map<int, int> visitedRouteList;
visitedRouteList[0] = 1;
int route[tsp.size()];
```

Kemudian dilakukan perulangan untuk menjelajahi node - node di dalam graf tsp
```CPP
while (i < tsp.size() && j < tsp[i].size())
{
	// Menentukan batas - batas dari graf
	if (counter >= tsp[i].size() - 1)
	{
		break;
	}

	if (j != i && (visitedRouteList[j] == 0))
	{
		if (tsp[i][j] < min)
		{
			min = tsp[i][j];
			route[counter] = j + 1;
		}
	}
	j++;
	if (j == tsp[i].size())
	{
		sum += min;
		min = INT_MAX;
		visitedRouteList[route[counter] - 1] = 1;
		j = 0;
		i = route[counter] - 1;
		counter++;
	}
}
```

Kemudian untuk mencari rute yang belum dilalui, dilakukan perulangan dengan mengecek semua tetangga yang berhubungan dengan node, yaitu sebagai berikut
```cpp
if (j != i && (visitedRouteList[j] == 0))
{
	if (tsp[i][j] < min)
	{
		min = tsp[i][j];
		route[counter] = j + 1;
	}
}
j++;
```
Jika node tetangga tersebut belum pernah dilalui dan costnya lebih kecil dibandingkan node sebelumnya, maka akan dipilih tetangga tersebut dan melakukan update untuk nilai costnya.

Kemudian untuk mengecek semua node dari kota ke-i, dilakukan menyimpan minimum cost sebelumnya ke dalam variabel sum dengan menjumlahkan dengan nilai sebelumnya. Kemudian variabel minimum cost diinisialisasi lagi dengan INT_MAX, menandai node tersebut telah dilalui, dan kemudian variabel penyimpan rutenya dikurangi 1 serta dilakukan increment pada counter (penanda berapa langkah yang telah dilakukan).
```CPP
if (j == tsp[i].size())
{
	sum += min;
	min = INT_MAX;
	visitedRouteList[route[counter] - 1] = 1;
	j = 0;
	i = route[counter] - 1;
	counter++;
}
```
Kemudian dilakukan update untuk node terakhir dari node sebelumnya yang terakhir dikunjungi dan besar costnya dijumlahkan dengan nilai variabel sum sebelumnya dan disimpan ke dalam variabel sum
```CPP
i = route[counter - 1] - 1;

for (j = 0; j < tsp.size(); j++)
{
	if ((i != j) && tsp[i][j] < min)
	{
		min = tsp[i][j];
		route[counter] = j + 1;
	}
}
sum += min;
```
Kemudian mencetak besar minimum cost yang telah disimpan di dalam variabel sum.
```CPP
cout << "Minimum Cost is : " << sum << endl;
```
Sehingga dengan menggunakan algoritma greedy-best first search, dihasilkan nilai minimum cost sebesar 80 path.

## Using A* Search ##

Algoritma A* adalah algoritma pencarian rute terpendek yang merupakan algoritma yang dituntun oleh fungsi heuristiknya, yang menentukan urutan node mana yang akan dikunjungi terlebih dahulu. Heuristik merupakan penilai yang memberi harga pada tiap simpul yang memandu A* mendapatkan solusi yang diinginkan.

Berbeda dengan algoritma Greedy, algoritma ini menghitung semua kemungkinan dan menyimpangnya sehingga jika setiap memilih jalan. Algoritma A* juga membandingkan dengan jalan lain yang disimpan. Sehingga hasil pencarian sikel terpendek dangan menggunakan algoritma ini akan menghasilkan hasil yang efisien. Namun karena ia terus membandingkan, algoritma ini memakan waktu yang cukup lama. Sehingga jika simpulnya sangat banyak akan memakan waktu yang sangat lama.

Hal pertama yang dilakukan adalah menginisialisasi besar graf dan mengisi vertex antarnode
```py
V = 4
graph = [[-1,10,15,20],[10,-1,35,25],[15,35,-1,30],[20,25,30,-1]]
```
Kemudian menginisialisasi tree dengan menggunakan library treelib (https://treelib.readthedocs.io/en/latest/) untuk mengisi node pada tree. Dan memanggil fungsi ```startTSP(graph, tree, V)```
```py
tree = Tree()
ans = startTSP(graph,tree,V)
```
Kemudian di dalam fungsi startTSP, dilakukan beberapa operasi sebagai berikut :
```py
#menginisialisasi goal state
goalState = 0
#memanggil TreeNode untuk memperlebar
toExpand = TreeNode(0,0,0,0,0)
```
Di dalam class TreeNode, dilakukan inisialisasi tree nodes untuk pelebaran jalan A*
```py
class TreeNode(object): 
        def __init__(self, c_no, c_id,  f_value, h_value, parent_id): 
            self.c_no = c_no
            self.c_id = c_id
            self.f_value = f_value
            self.h_value = h_value
            self.parent_id = parent_id
```
Lalu menginisialisasi heuristic untuk node 0 (pertama) di dalam tree dengan memanggil fungsi heuristic.
```py
heu = heuristic(tree,-1,0,V,graph)
```
Fungsi heuristic digunakan untuk membentuk graph dari semua node yang belum dilalui dan membuat Minimum Spanning Tree dari graph tersebut. Memutuskan bobot dari MST dan menghubungkannya dengan node yang telah dilalui dan node pertama. Untuk MST digunakan algoritma Prim.

Di mana isi dari fungsi heuristic adalah
```py
def heuristic(tree, p_id, t, V, graph):
	visited = set()	# Set untuk menyimpan node yang telah dilalui
	visited.add(0)
	visited.add(t)
	if(p_id != -1):
		tnode=tree.get_node(str(p_id))
		# Mencari semua node yang telah dilalui dan menambahkannya ke dalam set
		while(tnode.data.c_id != 1):
			visited.add(tnode.data.c_no)
			tnode=tree.get_node(str(tnode.data.parent_id))
	l = len(visited)
	num = V - l		# Urutan node yang belum dilalui
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
```

Kemudian membuat node pertama di dalam tree, menginisialiasi list Fringe
```py
tree.create_node("1", "1", data=TreeNode(0,1,heu,heu,-1))
fringe_list = {}
fringe_list[key] = FringeNode(0, heu)S
key = key + 1
```
Class FringeNode :
```py
class FringeNode(object): 
        def __init__(self, c_no,  f_value): 
            self.f_value = f_value
            self.c_no = c_no
```
Kemudian melakukan perulangan selama belum mencapai goalState untuk memilih node yang memiliki cost paling kecil di dalam fringe list
```py
while(goalState == 0):
		minf = sys.maxsize
		# Pick node having min f_value from the fringe list
		for i in fringe_list.keys():
			if(fringe_list[i].f_value < minf):
				toExpand.f_value = fringe_list[i].f_value
				toExpand.c_no = fringe_list[i].c_no
				toExpand.c_id = i
				minf = fringe_list[i].f_value
```
Lalu mengambil nilai heuristic h(n) dan nilai dari besar vertex g(n) dari node yang terpilih
```py
while(goalState == 0):
		...
		h = tree.get_node(str(toExpand.c_id)).data.h_value	#nilai h(n)
		val=toExpand.f_value - h #nilai g(n)
```
Kemudian mengecek node terpilih apakah sudah tidak ada cabang lagi atau masih ada
```py
while(goalState == 0):
		...
		path = checkPath(tree, toExpand, V)
```
Fungsi checkPath :
```py
def checkPath(tree, toExpand, V):
	tnode=tree.get_node(str(toExpand.c_id))	# Mengambil node dari tree untuk melebar
	list1 = list()	# List untuk menyimpan rute
	# Untuk node pertama
	if(tnode.data.c_id == 1):
		return 0
	else:
		depth = tree.depth(tnode) # Mengecek kedalaman tree
		s = set() # Set untuk menyimpan node di dalam rute
		# Berjalan ke atas dalam tree menggunakan parent pointer dan menambahkan semua node yang sejalan dengan set dan list
		while(tnode.data.c_id != 1):
			s.add(tnode.data.c_no)
			list1.append(tnode.data.c_no)
			tnode=tree.get_node(str(tnode.data.parent_id))
		list1.append(0)
		if(depth == V and len(s) == V and list1[0]==0):
			print("Path complete")
			list1.reverse()
			print(list1) # Mencetak node - node yang dilalui dalam algoritma ini
			return 1
		else:
			return 0
```
Kemudian jika node yang melebar adalah 0 dan rutenya tidak ada child lagi, maka program selesai. Selain itu, kita mengecek node saat ekspansi dan bukan saat inisialisasi
```py
while(goalState == 0):
		...
		if(toExpand.c_no==0 and path==1):
			goalState=1
			cost=toExpand.f_value
		else:
			del fringe_list[toExpand.c_id] # Menghapus node dari List Fringe
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
```
Setelah selesai menjalankan semua fungsi di atas, maka di dalam main, kita mencetak besar cost yang dihasilkan dari algoritma A* tersebut. Sehingga dihasilkan besar minimum costnya adalah 79.

Jadi dapat disimpulkan bahwa dengan menggunakan algoritma A* search, kita bisa mendapatkan hasil yang optimal daripada hasil dari algoritma Greedy-Best First Search. Meskipun proses algoritma A* terbilang membutuhkan waktu lebih lama, dari algoritma ini dapat dihasilkan cost yang optimal.