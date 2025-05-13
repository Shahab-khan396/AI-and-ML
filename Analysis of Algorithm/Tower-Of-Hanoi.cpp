// Tower of Hanoi problem implementation in C++

#include <iostream>
using namespace std;

// Function to move disks recursively
void towerOfHanoi(int n, char source, char destination, char auxiliary) {
    // Base case: If only one disk, move it directly
    if (n == 1) {
        cout << "Move disk 1 from " << source << " to " << destination << endl;
        return;
    }

    // Recursive step 1: Move n-1 disks from source to auxiliary
    towerOfHanoi(n - 1, source, auxiliary, destination);

    // Move the nth disk from source to destination
    cout << "Move disk " << n << " from " << source << " to " << destination << endl;

    // Recursive step 2: Move n-1 disks from auxiliary to destination
    towerOfHanoi(n - 1, auxiliary, destination, source);
}

int main() {
    int n; // Number of disks
    cout << "Enter the number of disks: ";
    cin >> n;

    cout << "The sequence of moves to solve the Tower of Hanoi with " << n << " disks is:" << endl;
    towerOfHanoi(n, 'A', 'C', 'B'); // A is the source, C is the destination, B is auxiliary

    return 0;
}
