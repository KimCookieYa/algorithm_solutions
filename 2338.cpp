#include <bits/stdc++.h>

using namespace std;

string myPlus(string x, string y) {
	string ans;
	int e;
	if (x.size() > y.size()) {
		e = x.size() - y.size();
	}
	eles {
		e = y.size() - x.size();
	}
	
	return ans;
}

string myMinus(string x, string y) {
	string ans;
	
	
	return ans;
}

string myMulti(string x, string y) {
	string ans;
	
	
	return ans;
}

int main(void) {
	string x, y;
	getline(cin, x); getline(cin, y);
	
	cout << myPlus(x, y) << '\n';
	cout << myMinus(x, y) << '\n';
	cout << myMulti(x, y) << '\n';
	
	return 0;
}
