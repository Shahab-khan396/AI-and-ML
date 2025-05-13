// Algorithm to determine time complexity for accessing an element in an array
#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int SIZE = 1000000; // Size of the array
    int arr[SIZE];

    // Initialize the array with values
    for (int i = 0; i < SIZE; i++) {
        arr[i] = i;
    }

    int index = SIZE / 2; // The index to access

    // Start the clock
    auto start = high_resolution_clock::now();

    // Access the element
    int value = arr[index];

    // Stop the clock
    auto stop = high_resolution_clock::now();

    // Calculate the duration
    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Accessed element at index " << index << ": " << value << endl;
    cout << "Time taken to access element: " << duration.count() << " nanoseconds" << endl;

    return 0;
}
