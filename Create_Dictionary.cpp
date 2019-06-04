#include<bits/stdc++.h>
using namespace std;
int main()
{
	map < string , map < string , int > > mp;
	freopen("out.txt","r",stdin);
	string s;
	while(getline(cin,s))
	{
		istringstream ss(s);
		string a,b;
		getline(ss,a,',');
		getline(ss,b,',');
		transform(a.begin(), a.end(), a.begin(), ::tolower); 
		transform(b.begin(), b.end(), b.begin(), ::tolower);
		cout<<a<<"-"<<b<<endl;
		mp[a][b]++;
	}
	
	cin.clear();
	freopen("out_file.txt","r",stdin);
	while(getline(cin,s))
	{
		istringstream ss(s);
		string a,b;
		getline(ss,a,',');
		getline(ss,b,',');
		transform(a.begin(), a.end(), a.begin(), ::tolower); 
		transform(b.begin(), b.end(), b.begin(), ::tolower);
		cout<<a<<"-"<<b<<endl;
		mp[a][b]++;
	}
	
	freopen("dic.txt","w",stdout);
	
	for(map < string , map < string , int > >:: iterator mt = mp.begin();mt!=mp.end();mt++)
	{
		if(mt->first ==" ")
			continue;
	    map < string,int > m = mt->second;
	    int x = 0;
		for(map<string,int> :: iterator it = m.begin();it!=m.end();it++)
	    {
	    	x += it->second;
		}
		if(x<5)
			continue;
		cout<< mt->first<<endl;
	    for(map<string,int> :: iterator it = m.begin();it!=m.end();it++)
	    {
	    	cout<<it->first<<","<<it->second<<endl;
		}
		cout<<"end"<<endl;
	}
}
