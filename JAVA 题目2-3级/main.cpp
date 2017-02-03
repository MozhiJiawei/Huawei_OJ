#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int product1 = 1, product2 = 1;
    for (int i = 1; i <= n; i++) {
        product1 *= m + i;
        product2 *= i; 
    }
    cout << product1 / product2 << endl;
}