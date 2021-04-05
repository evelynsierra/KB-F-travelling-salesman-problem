#include <stdio.h>
#include <stdlib.h>

int source, dest, V, E, visited[20], G[20][20], cost = 0;
int found = 0;

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

int main()
{
	int i, j, v1, v2, c;
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
	for (i = 0; i < E; i++)
	{
		printf("Enter the edges(V1 V2 Cost) : ");
		scanf("%d %d %d", &v1, &v2, &c);
		G[v1][v2] = c;
	}

	printf("\nAdjacency Matrix\n");
	for (i = 1; i <= V; i++)
	{
		for (j = 1; j <= V; j++)
		{
			printf(" %d ", G[i][j]);
		}
		printf("\n");
	}

	printf("\nWeight of every edges\n");
	for (i = 1; i <= V; i++)
	{
		for (j = 1; j <= V; j++)
		{
			if (G[i][j] != 0)
			{
				printf(" %d -> %d : %d\n", i, j, G[i][j]);
			}
		}
	}

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

	return 0;
}

/* Contoh testcase

	10
	11
	1 2 2
	1 3 3
	2 4 4
	2 5 5
	3 6 6
	3 7 7
	4 8 8
	5 9 9
	6 10 1
	8 9 9
	9 10 1
	2
	10
	
*/
