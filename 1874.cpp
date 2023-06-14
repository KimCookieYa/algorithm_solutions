#include <bits/stdc++.h>

using namespace std;

int a[100000];
int b[100000];

int main(void) {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	vector<char> ans;
	stack<int> s;
	int cnt = 0;
	
	for (int i = 0; i < n; i++) {
		s.push(i+1);
		ans.push_back('+');
		
		while (!s.empty() && s.top() == a[cnt]) {
			s.pop();
			ans.push_back('-');
			cnt++;
		}
	}
	
	if (!s.empty()) {
		cout << "NO";
	}
	else {
		for (int i = 0; i < ans.size(); i++) {
			cout << ans[i] << '\n';
		}
	}
	
	return 0;
}
