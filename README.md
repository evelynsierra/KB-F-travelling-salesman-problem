# KB-F-travelling-salesman-problem #
## Anggota Kelompok ##

NRP | NAMA
------------- | -------------
05111940000111  | Evelyn Sierra
05111940000042  | Bayu Eka Prawira

##Pendahuluan##
The travelling salesman problem (atau yang biasa disebut dengan TSP) menanyakan pertanyaan berikut: "Diberikan daftar kota dan jarak antara setiap pasangan kota, apa rute terpendek yang mungkin mengunjungi setiap kota tepat satu kali dan kembali ke kota asal? " 
Untuk memecahkan masalah ini, digunakan informed search dan uninformed search. Khusus untuk uninformed search, setiap salesman tersebut pernah mengunjungi kota tersebut, kota itu akan ditandai sehingga tidak memunculkan looping yang berulang.

##Using DFS Search##
Langkah pertama adalah memasukkan total vertices dan total edges yang diinginkan. Kemudian gunakan looping untuk membuat isi Graph menjadi 0. 
```
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
```
for (i = 0; i < E; i++)
	{
		printf("Enter the edges(V1 V2 Cost) : ");
		scanf("%d %d %d", &v1, &v2, &c);
		G[v1][v2] = c;
	}
```

Masukkan nilai source dan destination yang diinginkan. Apabila nilai source atau destination lebih besar daripada jumlah vertices, hasilnya tidak akan keluar. Sebaliknya, function `DFS()` akan berjalan dengan memasukkan parameter `source`
```
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
```
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


##Using UCS Search##
