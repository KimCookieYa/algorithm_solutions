#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	cin.ignore();
	vector<string> s(n);
	for (int i = 0; i < n; i++) {
		getline(cin, s[i], '\n');
	}
	
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		bool check[26] = {false, };
		
		int j;
		for (j = 0; j < s[i].size(); j++) {
			int ix = s[i][j] - 'a';
			
			if (j < s[i].size()-1) {
				if (check[ix] == false && s[i][j] == s[i][j+1]) {
					continue;
				}
			}
			
			if (check[ix] == false) {
				check[ix] = true;
			}
			else {
				break;
			}
		}
		
		if (j >= s[i].size()) {
			cnt++;
		}
	}
	
	cout << cnt;
	
	return 0;
}
