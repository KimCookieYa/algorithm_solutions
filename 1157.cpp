#include <bits/stdc++.h>

using namespace std;

int num[26];

int main(void) {
	string s;
	getline(cin, s);
	
	for (int i = 0; i < s.length(); i++) {
		if (s[i] >= 'a') {
			s[i] = s[i] - ('a'-'A');
			
		}
		num[s[i] - 'A']++;
	}
	
	int ans = 0;
	bool check = true;
	for (int i = 1; i < 26; i++) {
		if (num[ans] < num[i]) {
			ans = i;
			check = true;
		}
		else if (num[ans] == num[i]) {
			check = false;
		}
	}
	
	if (!check) {
		printf("?\n");
	}
	else {
		printf("%c\n", ans + 'A');
	}
	
	return 0;
}
