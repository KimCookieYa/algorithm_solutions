#include <bits/stdc++.h>

using namespace std;

struct pos {
	int x, y;
};

int paper[128][128];

int color[2];

void render(pos s, pos e) {
	for (int i = s.y; i <= e.y; i++) {
		for (int j = s.x; j <= e.x; j++) {
			cout << paper[i][j] << ' ';
		}
		cout << endl;
	}
	cout << endl;
}

void func(pos s, pos e, int n) {
	if (n == 1) {
		color[paper[s.y][s.x]]++;
		return;
	}
	//render(s, e);
	for (int i = s.y; i <= e.y; i++) {
		for (int j = s.x; j <= e.x; j++) {
			if (paper[i][j] != paper[s.y][s.x]) {
				func(s, {e.x-n/2, e.y-n/2}, n/2);
				func({s.x+n/2, s.y}, {e.x, e.y-n/2}, n/2);
				func({s.x, s.y+n/2}, {e.x-n/2, e.y}, n/2);
				func({s.x+n/2, s.y+n/2}, e, n/2);
				return;
			}
		}
	}
	
	color[paper[s.y][s.x]]++;
}

int main(void) {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> paper[i][j];
		}
	}
	
	func({0,0}, {n-1,n-1}, n);
	
	cout << color[0] << '\n' << color[1];
	
	return 0;
}
