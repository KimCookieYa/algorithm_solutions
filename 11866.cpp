#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n, k;
	cin >> n >> k;
	
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	
	int ans[n] = {0, };
	int i = 0, cnt = 1;
	while (!q.empty()) {
		int temp = q.front();
		q.pop();
		
		if (cnt%k == 0) {
			ans[i++] = temp;
		}
		else {
			q.push(temp);
		}
		
		cnt++;
	}
	
	cout << '<';
	for (i = 0; i < n-1; i++) {
		cout << ans[i] << ", ";
	}
	cout << ans[n-1] << '>';
	
	return 0;
}
