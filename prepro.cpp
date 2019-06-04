#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("orignal1.txt","r",stdin);
	freopen("biryani-bar-rajarhat-new-town.txt","w",stdout);
	string s,w;
	int p=0,k=500;
	while(getline(cin, w))
	{
		if(w.size()==2)
		{
			p=5;
		}
		else if(p>0)
		p--;
		else if(p==0)
		{
			if(w!="")
			s+=w;
		}
		
	}
	cout<<s<<endl;
	return 0;
}
