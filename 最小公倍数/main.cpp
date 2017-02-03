#include <iostream>
#include <algorithm>
using namespace std;
 
int cab(int A, int B) {
    while (B != 0) {
        int C = A % B;
        A = B;
        B = C;
    }
    return A;
}

int main() {
    int A, B;
    cin >> A >> B;
    cout << A * B / cab(A, B);
    return 0;
}