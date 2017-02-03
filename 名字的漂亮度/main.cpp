#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

char Capital(char c) {
    if (c >= 'A' && c <= 'Z') {
        return c;
    }
    else {
        return c - 'a' + 'A';
    }
}

int main() {
    int N;
    cin >> N;
    vector<string> names;
    for (int i = 0; i < N; i++) {
        string name;
        cin >> name;
        names.push_back(name);
    }
    for (int i = 0; i < N; i++) {
        vector<int> bullet(26, 0); 
        int result = 0; 
        for (char c : names[i]) {
            bullet[Capital(c) - 'A']++;
        }
        sort(bullet.begin(), bullet.end());
        for (int i = 0; i < 26; i++) {
            result += bullet[i] * (i + 1);
        }
        cout << result << endl;
    } 
    return 0;
}