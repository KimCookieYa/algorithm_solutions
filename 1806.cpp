#include <iostream>

using namespace std;

int main(void) {
	
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, m;
	cin >> n >> m;
	
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	long long min = 10000*100000, sum;
	for (int i = 0; i < n; i++) {
		sum = 0;
		
		int start = i;
		int end;
		for (int j = i; j < n && sum < m; j++) {
			sum += a[j];
			end = j;
		}
		
		if (sum == m && min > end-start+1) {
			min = end-start+1;
		}
	}
	
	if (min == 10000*100000)
		cout << 0;
	else
		cout << min;
	return 0;
}
