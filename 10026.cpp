#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

int n;
char a[100][100];
bool visited[100][100];
int dir_x[4] = {1,-1,0,0};
int dir_y[4] = {0,0,1,-1};

bool inArea(int x, int y) {
	if (0 <= x && x < n && 0 <= y && y < n)
		return true;
	
	return false;
}

void bfs(int x, int y) {
	char color = a[x][y];
	
	queue<pair<int,int>> q;
	q.push(make_pair(x, y));
	visited[x][y] = true;
	while (!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		q.pop();
		
		if (a[cur_x][cur_y] == 'G') a[cur_x][cur_y] = 'R';
		
		for (int i = 0; i < 4; i++) {
			int next_x = cur_x + dir_x[i];
			int next_y = cur_y + dir_y[i];
			
			if (inArea(cur_x + dir_x[i], cur_y + dir_y[i])) {
				if (!visited[next_x][next_y]) {
					if (color == a[next_x][next_y]) {
						q.push(make_pair(next_x, next_y));
						visited[next_x][next_y] = true;
					}
				}
			}
		}
	}
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}
	
	int ans1 = 0;
	int ans2 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				bfs(i, j);
				ans1++;
			}
		}
	}
	
	memset(visited, false, sizeof(visited));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				bfs(i, j);
				ans2++;
			}
		}
	}
	
	cout << ans1 << ' ' << ans2;
	
	return 0;
}
