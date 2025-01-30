#include <iostream>
using namespace std;

int main()
{
    string str;
    cout << "Enter your string: ";
    cin >> str;
    int hash[256] = {0};
    for (int i = 0; i < 256; i++)
    {
        hash[str[i]]++;
    }
    int q;
    cout << "Enter how many queries you want to make: ";
    cin >> q;

    while (q--)
    {
        char c;
        cout << "Enter a character that you wish to check: ";
        cin >> c;
        cout << "Character " << '"' << c << '"' << " appears, ";
        cout << hash[c] << " times." << endl;
    }
    return 0;
}