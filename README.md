# KB-F-travelling-salesman-problem #
## Anggota Kelompok ##

NRP | NAMA
------------- | -------------
05111940000111  | Evelyn Sierra
05111940000042  | Bayu Eka Prawira

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

