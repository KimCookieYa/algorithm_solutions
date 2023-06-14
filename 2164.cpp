#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	queue<int> q;
	for (int i = 0; i < n; i++) {
		q.push(i+1);
	}
	
	while (q.size() > 1) {
		q.pop();
		int temp = q.front();
		q.pop();
		q.push(temp);
	}
	
	cout << q.front();
	
	return 0;
}
