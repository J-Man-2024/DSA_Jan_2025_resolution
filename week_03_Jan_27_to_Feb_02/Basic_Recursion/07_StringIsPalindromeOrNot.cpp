#include <iostream>
using namespace std;

bool palindromeOrNot(string &str, int start, int end)
{
    if (start >= end)
        return true;

    if (str[start] != str[end])
    {
        return false;
    }

    return palindromeOrNot(str, start + 1, end - 1);
}
int main()
{
    string str;
    cout << "Enter a string: ";
    cin >> str;
    int len = str.length();
    if (palindromeOrNot(str, 0, len - 1))
    {
        cout << '"' << str << '"' << ", is a Palindrome!";
    }
    else
    {
        cout << '"' << str << '"' << ", is not a Palindrome!";
    }

    return 0;
}