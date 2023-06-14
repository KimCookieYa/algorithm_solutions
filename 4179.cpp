#include <bits/stdc++.h>

using namespace std;

struct pos {
	int x, y;
};

int r, c;
char maps[1001][1001];
bool noWay[1001][1001];
pos J;
queue<pos> q2;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
	scanf(" %d %d", &r, &c);
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			scanf(" %c", &maps[i][j]);
			if (maps[i][j] == 'J') {
				J = {j,i};
				maps[i][j] = '.';
			}
			else if (maps[i][j] == 'F') {
				q2.push({j,i});
			}
			else if (maps[i][j] == '#') {
				noWay[i][j] = true;
			}
		}
	}
	
	// bfs
	int cnt = 0;
	queue<pos> q;
	q.push({J.x, J.y});
	noWay[J.y][J.x] = true;
	
	while (!q.empty()) {
		int m = q2.size();
		for (int j = 0; j < m; j++) {
			pos cf = q2.front();
			q2.pop();
			
			for (int i = 0; i < 4; i++) {
				pos nf = {cf.x + dx[i], cf.y + dy[i]};
				if (0 <= nf.x && nf.x < c && 0 <= nf.y && nf.y < r) {
					if (maps[nf.y][nf.x] == '.' || maps[nf.y][nf.x] == 'J') {
					q2.push(nf);
					maps[nf.y][nf.x] = 'F';
					}
				}
			}
		}
		
		int n = q.size();
		for (int j = 0; j < n; j++) {
			pos cur = q.front();
			q.pop();
			
			if (0 == cur.x || cur.x == c-1 || 0 == cur.y || cur.y == r-1) {
				printf("%d\n", cnt+1);
				return 0;
			}
			
			for (int i = 0; i < 4; i++) {
				pos n = {cur.x + dx[i], cur.y + dy[i]};
				
				if (0 > n.x || n.x >= c || 0 > n.y || n.y >= r) {
					continue;
				}
			
				if (maps[n.y][n.x] == '.' && !noWay[n.y][n.x]) {
					q.push(n);
					maps[n.y][n.x] = 'J';
					noWay[n.y][n.x] = true;
				}
			}
		}
		
		cnt++;
	}
	
	printf("IMPOSSIBLE\n");
	return 0;
}
