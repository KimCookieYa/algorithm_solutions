#include <cstdio>
#include <queue>

using namespace std;

struct pos {
	int x, y;
};

int n, maps[64][64];
bool visited[64][64];
const int dx[2] = {1, 0};
const int dy[2] = {0, 1};

void bfs() {
	queue<pos> q;
	q.push({0,0});
	visited[0][0] = true;
	while (!q.empty()) {
		int cur_x = q.front().x, cur_y = q.front().y;
		q.pop();
		int step = maps[cur_y][cur_x];
		
		
		if (step == -1) {
			printf("HaruHaru");
			return;
		}
		else if (step == 0) {
			printf("Hing");
			return;
		}
		
		for (int i = 0; i < 2; i++) {
			int nx = cur_x + step * dx[i];
			int ny = cur_y + step * dy[i];
			
			if (0 <= nx && nx < n && 0 <= ny && ny < n) {
				if (!visited[ny][nx]) {
					q.push({nx,ny});
					visited[ny][nx] = true;
				}
			}
		}
	}
	printf("Hing");
}

int main(void) {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &maps[i][j]);
		}
	}
	
	bfs();
	
	return 0;
}
