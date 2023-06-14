#include <bits/stdc++.h>

using namespace std;

deque<int> dq;

int findx(int x) {
	for (int i = 0; i < dq.size(); i++) {
		if (dq[i] == x) {
			return i;
		}
	}
	
	return dq.size()-1;
}

using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	
	int b[n];
	for (int i = 0; i < m; i++) {
		cin >> b[i];
	}
	
	
	for (int i = 0; i < n; i++) {
		dq.push_back(i+1);
	}
	
	int cnt = 0;
	int size = n;
	for (int i = 0; i < m; i++) {
		if (findx(b[i]) <= size/2) {
			while (dq.front() != b[i]) {
				int temp = dq.front();
				dq.pop_front();
				dq.push_back(temp);
				cnt++;
			}
		}
		else {
			while (dq.front() != b[i]) {
				int temp = dq.back();
				dq.pop_back();
				dq.push_front(temp);
				cnt++;
			}
		}
		dq.pop_front();
		size--;
	}
	
	cout << cnt;
	
	return 0;
}
