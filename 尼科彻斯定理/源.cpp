#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int GetSequeOddNum(int m, string &pcSequeOddNum);

int main() { 
    int m;
    string pcSequeOddNum;
    cin >> m;
    GetSequeOddNum(m, pcSequeOddNum); 
    cout << pcSequeOddNum << endl;
    return 0;
}

int GetSequeOddNum(int m, string & pcSequeOddNum) {
    int a = m*m - m + 1;
    for (int i = 0; i < m; i++) { 
        stringstream ss;
        ss << a;
        a = a + 2;
        pcSequeOddNum.append(ss.str());
        pcSequeOddNum.push_back('+');
    }
    pcSequeOddNum.pop_back();
    return 0;
}
