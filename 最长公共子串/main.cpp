#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void TransfromUpper(string& str) {
    for (char &c : str) {
        if (c >= 'a' && c <= 'z') {
            c += 'A' - 'a';
        }
    }
}

int main() {
    string str1, str2;
    cin >> str1 >> str2; 
    TransfromUpper(str1);
    TransfromUpper(str2);

    vector<int> DP(str1.length(), 0);
    int cur_max = 0;
    for (int i = 0; i < str2.length(); i++) {
        for (int j = str1.length() - 1; j > 0; j--) { 
            if (str2[i] == str1[j]) {
                DP[j] = DP[j - 1] + 1;
            }
            else {
                DP[j] = 0;
            }
        }
        if (str2[i] == str1[0]) {
            DP[0] = 1;
        }
        cur_max = max(cur_max, *max_element(DP.begin(), DP.end()));
    }

    cout << cur_max << endl;
    return 0;
}