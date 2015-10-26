#include <cmath>
#include <cstdint>
#include <iostream>

using namespace std;

int con[] = {0,1,3,6,10,15,21,28,36,45};
int place[19];

int set(){
	place[0]=0;
	for(int i=1; i<19; i++)
		place[i]=pow(10,i)*(place[i-1]+con[9]);
} 

int main(){
	set();
	int test,m,dig,sum;
	uint64_t num,lag,len;
	cin>>test;
	while(test--){
		cin>>m;
		num=0;
		sum=0;
		while(m--){
			cin>>len;
			cin>>dig;
			while(len--){
				num*=10;
				num+=dig;
			}
		}
		sum+=con[num%10];
		lag=n%10;
		n/=10;
		for(int i=1; num>0; i++){
			sum+=place[i]*(num%10 - 1)+((num%10)*lag);
		}
		cout<<sum;
	}
}