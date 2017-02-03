#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> redraiment(n); 
    for (int i = 0; i < n; i++) {
        cin >> redraiment[i];
    }
    vector<int> mark(n, 1);
    for (int i = n - 1; i>=0; i--) { 
        for (int j = i + 1; j < n; j++) {
            if (redraiment[j] > redraiment[i]) { 
                mark[i] = max(mark[i], mark[j] + 1);
            }
        }
    }
    if (!mark.empty()) {
        cout << *max_element(mark.begin(), mark.end()) << endl; 
    }
    return 0;
}