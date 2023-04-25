#include <iostream>

int main(void) {

    int a;

    std::cin >> a ;

    const int b = a ;

    std::cout << b << std::endl;

    int arr[b];

    for (int i : arr) {
        std::cout << i << " ";
    }

    std::cout << std::endl;

    return 0;
}