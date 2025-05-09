#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int arr[1001];
int main() {
    int n;
    cin>>n;

    for (int i=0;i<n;i++)
        cin>>arr[i];

    sort(arr, arr+n);

    int time=0, tmp=0;
    for (int i=0;i<n;i++) {
        tmp+=arr[i];
        time+=tmp;
    }
    cout<<time;
    return 0;
}