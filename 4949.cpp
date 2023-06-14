#include <bits/stdc++.h>

using namespace std;

int main(void) {
	while (1) {
		string str;
		getline(cin, str);
		
		if (str[0] == '.') {
			return 0;
		}
		
		stack<char> s;
		for (int i = 0; i < str.size(); i++) {
			if (str[i] == '(') {
				s.push('(');
			}
			else if (str[i] == ')') {
				if (s.empty()) {
					s.push(')');
					break;
				}
				
				if (s.top() == '(') {
					s.pop();
				}
				else {
					break;
				}
			}
			else if (str[i] == '[') {
				s.push('[');
			}
			else if (str[i] == ']') {
				if (s.empty()) {
					s.push(']');
					break;
				}
				
				if (s.top() == '[') {
					s.pop();
				}
				else {
					break;
				}
			}
			
		}
		
		if (s.empty()) {
			cout << "yes" << endl;
		}
		else {
			cout << "no" << endl;
		}
	}
	
	return 0;
}
