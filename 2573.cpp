#include <bits/stdc++.h>

using namespace std;

struct pos {
	int x, y;
};

int n, m;
int sea[300][300];
bool visited[300][300];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

bool melting(void) {
	bool melted = true;
	int cnt = 0;
	for (int i = 1; i < n-1; i++) {
		for (int j = 1; j < m-1; j++) {
			if (sea[i][j] < 0) {
				sea[i][j] = 0;
			}
		}
	}
	for (int i = 1; i < n-1; i++) {
		for (int j = 1; j < m-1; j++) {
			if (sea[i][j] > 0) {
				cnt++;
				int zero = 0;
				for (int k = 0; k < 4; k++) {
					if (sea[i+dy[k]][j+dx[k]] == 0) {
						zero++;
					}
				}
				
				sea[i][j] -= zero;
				if (sea[i][j] <= 0) {
					sea[i][j] = -1;
				}
			}
		}
	}
	
	if (cnt == 0) {
		melted = false;
	}
	
	return melted;
}

bool bfs(int i, int j) {
	queue<pos> q;
	q.push({j,i});
	
	visited[i][j] = true;
	while (!q.empty()) {
		pos cur = q.front();
		q.pop();
		
		for (int k = 0; k < 4; k++) {
			pos next = {cur.x + dx[k], cur.y + dy[k]};
			if (1 <= next.x && next.x < m-1 && 1 <= next.y && next.y < n-1) {
				if (sea[next.y][next.x] > 0 && !visited[next.y][next.x]) {
					q.push(next);
					visited[next.y][next.x] = true;
				}
			}
		}
	}
	
	return true;
}

int counted(void) {
	int cnt = 0;
	fill_n(visited[0], 90000, false);
	
	for (int i = 1; i < n-1; i++) {
		for (int j = 1; j < m-1; j++) {
			if (sea[i][j] > 0 && !visited[i][j]) {
				if (bfs(i, j)) {
					cnt++;
				}
			}
		}
	}
	
	return cnt;
}

int main(void) {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> sea[i][j];
		}
	}
	
	int ans = 0;
	while (1) {
		if (!melting()) {
			ans = 0;
			break;
		}
		
		ans++;
		if (counted() > 1) {
			break;
		}
	}
	
	cout << ans;
	
	return 0;
}
