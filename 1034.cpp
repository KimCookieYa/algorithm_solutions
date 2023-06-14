#include <iostream>
#include <string>
using namespace std;

int table[51][51];
int n, m, k;

int max_func(int x, int y) {
	return (x > y) ? x : y;
}

int main(void) {
	cin >> n >> m;
	
	int i, j, l;
	for (i = 0; i < n; i++) {
		string temp;
		cin >> temp;
		int num = 0;
		for (j = 0; j < m; j++) {
			table[i][j] = temp[j] - ('0' - 0);
			if (table[i][j] == 0)
				num++;
		}
		table[i][m] = num;
	}
	cin >> k;
	
	int ans = 0;
	for (int i = 0; i < n; i++) {
		int max = 1;
		if (table[i][m] > k || table[i][m]%2 != k%2) {
			continue;
		}
		
		for (int j = 0; j < n; j++) {
			if (i != j) {
				for (l = 0; l < m; l++) {
					if (table[i][l] != table[j][l]) {
						break;
					}
				}
				
				if (l >= m)
					max++;
			}
		}
		
		ans = max_func(max, ans);
	}
	
	cout << ans;
	
	return 0;
}
