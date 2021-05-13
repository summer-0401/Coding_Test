#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    // Write C++ code here
    string a, b, answer, tmp;
    cin >> a >> b;
    
    int a_len = a.length();
    int b_len = b.length();
    int l, cal;
    if (a_len >= b_len){
        l = a.length();
        for(int j=0;j<a_len-b_len;j++) b = '0'+b;
    }
    else{
        l = b.length();
        for(int j=0;j<b_len-a_len;j++) a = '0'+a;
    }
        
    int extra=0;
    for(int i=l-1;i>=0;i--){
        cal = a[i]-'0' + b[i] - '0' + extra;
        tmp = to_string(cal);
        if (tmp.length()>1) extra=1;
        else extra=0;
        answer = tmp[extra] + answer;
    }
    if (extra==1) answer = '1' + answer;
    cout << answer;
    return 0;
}