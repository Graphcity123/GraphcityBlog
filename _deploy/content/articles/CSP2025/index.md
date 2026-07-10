---
title: CSP2025 解题报告
date: 2025-11-01
tags:
  - OI
---

体感上今年是不是比去年简单太多了。

## A

贪心。先全部选最大的，如果有一列超过一半被选那就按照差值从小往大的顺序贪心回退成次大的。

总时间复杂度 $O(n\log n)$。

推荐用时：5min

```cpp
#include<bits/stdc++.h>
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=1e5;

int n,a[Maxn+5][4],b[Maxn+5];

inline void Solve()
{
    cin>>n;
    For(i,1,n) For(j,1,3) cin>>a[i][j];
    For(i,1,n)
    {
        if(a[i][1]>=a[i][2] && a[i][1]>=a[i][3]) b[i]=1;
        if(a[i][2]>=a[i][1] && a[i][3]>=a[i][3]) b[i]=2;
        if(a[i][3]>=a[i][1] && a[i][3]>=a[i][2]) b[i]=3;
    }
    int cnt[4]={0,0,0,0},ans=0;
    For(i,1,n) cnt[b[i]]++,ans+=a[i][b[i]];
    For(ID,1,3) if(cnt[ID]>n/2)
    {
        int m=cnt[ID]-(n/2); vector<int> vx;
        For(i,1,n) if(b[i]==ID)
        {
            int mn=INT_MAX;
            For(j,1,3) if(j!=ID) mn=min(mn,a[i][ID]-a[i][j]);
            vx.push_back(mn);
        } sort(vx.begin(),vx.end());
        For(i,0,m-1) ans-=vx[i];
        break;
    }
    cout<<ans<<endl;
}

int main()
{
    freopen("club.in","r",stdin);
    freopen("club.out","w",stdout);
    
    ios::sync_with_stdio(false);
    int T; cin>>T;
    while(T--) Solve();
    return 0;
}
```

## B

暴力枚举后面 $k$ 个点哪些选了哪些没选，然后暴力跑 Kruskal 最小生成树。

注意一开始的 $m$ 条边可以先跑一次最小生成树，只保留在生成树中的 $n-1$ 条边。

总时间复杂度 $O(2^knk)$，相信 CCF 的新机子。

推荐用时：15min

```cpp
#include<bits/stdc++.h>
#define ll long long
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=1e4+10,Maxm=1e6;

int n,m,K,lim,fa[Maxn+5];
int h[15][Maxn+5]; ll ans;
struct Edge{int a,b,c;} dx[Maxm+5];
inline bool operator<(Edge x,Edge y) {return x.c<y.c;}
inline int Find(int x) {return fa[x]==x?x:fa[x]=Find(fa[x]);}
vector<Edge> vx;

inline void Add(int id,int a,int b,int c)
{
    a=Find(a),b=Find(b);
    if(a!=b) ans+=c,fa[a]=b;
}

int main()
{
    freopen("road.in","r",stdin);
    freopen("road.out","w",stdout);
    
    ios::sync_with_stdio(false);
    cin>>n>>m>>K; lim=(1<<K)-1;
    For(i,1,m) cin>>dx[i].a>>dx[i].b>>dx[i].c;
    sort(dx+1,dx+m+1);
    For(i,1,n) fa[i]=i;
    For(i,1,m)
    {
        int a=dx[i].a,b=dx[i].b; a=Find(a),b=Find(b);
        if(a!=b) fa[a]=b,vx.push_back(dx[i]);
    }
    For(i,1,K) For(j,0,n) cin>>h[i][j];
    For(i,1,K) For(j,1,n) vx.push_back(Edge{n+i,j,h[i][j]});
    sort(vx.begin(),vx.end());
    ll all=LLONG_MAX;
    For(id,0,lim)
    {
        int chk=1; ans=0,iota(fa+1,fa+n+K+1,1);
        For(j,1,K) if(id&(1<<j-1)) ans+=h[j][0];
        for(auto [a,b,c]:vx)
        {
            if(a<=n) Add(id,a,b,c);
            else if(id&(1<<a-n-1)) Add(id,a,b,c);
        } For(i,1,n) if(Find(i)!=Find(1)) {chk=0; break;}
        if(chk) all=min(all,ans);
    } cout<<all<<endl;
    return 0;
}
```

## C

对于每个 $s_{i,1},s_{i,2}$（$t_{i,1},t_{i,2}$ 同理），设 $s_i=s_{i,1}[1]+s_{i,2}[1]+s_{i,1}[2]+s_{i,2}[2]+\cdots$，即交错着拼起来。

那么我们的问题就是：对于每个 $t_i$，我们有一个 $[l_i,r_i]$，问 $t$ 有多少子串包含 $t[l_i,r_i]$ 且等于某个 $s_j$。

对 $s$ 建 AC 自动机，对于 $s_i$ 的结尾在 AC 自动机对应结点上打标记。那么我们就相当于对于 $t_{i}[1,j]\ (j\ge r_i)$ 在 fail 树祖先链上寻找有多少个深度大于等于 $j-l_i+1$ 的标记。

注意到标记个数是 $O(n)$ 的，查询次数是 $O(L)$ 的，考虑根号平衡。

对于所有标记结点建立虚树，然后对于所有结点和询问按照深度从大往小的顺序排序，就变成了子树（区间）加，单点查的问题，使用 $O(\sqrt n)-O(1)$ 的数据结构即可。

总时间复杂度 $O(n\sqrt n+26L)$。

推荐用时：1h

```cpp
#include<bits/stdc++.h>
#define ll long long
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=2e5,Maxk=1e7,B=450;

int n,m,L[Maxn+5],R[Maxn+5],ps[Maxn+5]; string s[Maxn+5],t[Maxn+5];
int ch[Maxk+5][26],fail[Maxk+5],idx[Maxn+5],chk[Maxk+5],tot;
int to[Maxk+5],len[Maxn+5],in[Maxk+5],out[Maxk+5],cur; ll ans[Maxn+5];
vector<int> v[Maxk+5];
vector<pair<int,int>> qr[Maxk+5];

struct Block
{
    int L[Maxn+5],R[Maxn+5],dx[Maxn+5],tot;
    int sum[Maxn+5],h[Maxn+5];
    inline void Build()
    {
        for(int i=1;i<=cur;i+=B) L[++tot]=i,R[tot]=min(i+B-1,cur);
        For(i,1,tot) For(j,L[i],R[i]) dx[j]=i;
    }
    inline void Add(int x,int k)
    {
        if(!x) return; int p=dx[x];
        For(i,1,p-1) sum[i]+=k; For(i,L[p],x) h[i]+=k;
    }
    inline void Add(int l,int r,int k) {Add(r,k),Add(l-1,-k);}
    inline int Count(int x) {return h[x]+sum[dx[x]];}
} DS;

inline void dfs(int x)
{
    if(chk[x]) in[x]=++cur;
    if(x==0 || chk[x]) to[x]=x; else to[x]=to[fail[x]];
    for(auto y:v[x]) dfs(y);
    if(chk[x]) out[x]=cur;
}
inline void Build()
{
    queue<int> q;
    For(i,0,25) if(ch[0][i]) q.push(ch[0][i]);
    while(!q.empty())
    {
        int i=q.front(); q.pop();
        For(j,0,25) if(ch[i][j]) fail[ch[i][j]]=ch[fail[i]][j],q.push(ch[i][j]);
                    else ch[i][j]=ch[fail[i]][j];
    }
    For(i,1,tot) v[fail[i]].push_back(i);
    dfs(0);
}

int main()
{
    freopen("replace.in","r",stdin);
    freopen("replace.out","w",stdout);

    ios::sync_with_stdio(false);
    cin>>n>>m;
    For(i,1,n)
    {
        string s1,s2; cin>>s1>>s2; int len=s1.size();
        For(j,0,len-1) s[i].push_back(s1[j]),s[i].push_back(s2[j]);
    }
    For(i,1,m)
    {
        string t1,t2; cin>>t1>>t2; int len=t1.size(); int l=len,r=1;
        if(len!=t2.size()) {ps[i]=1; continue;}
        For(j,1,len) if(t1[j-1]!=t2[j-1]) l=min(l,j),r=j;
        For(j,0,len-1) t[i].push_back(t1[j]),t[i].push_back(t2[j]);
        L[i]=l*2-1,R[i]=r*2;
    }
    For(i,1,n)
    {
        int p=0; for(auto j:s[i])
        {
            int x=j-'a'; if(!ch[p][x]) ch[p][x]=++tot;
            p=ch[p][x];
        } idx[i]=p,chk[p]++;
    }
    Build();
    // For(i,1,tot) cerr<<i<<": "<<fail[i]<<' '<<chk[i]<<' '<<in[i]<<' '<<out[i]<<endl;
    For(i,1,m) if(!ps[i])
    {
        int p=0,len=t[i].size();
        For(j,1,len)
        {
            p=ch[p][t[i][j-1]-'a']; if(j>=R[i] && j%2==0 && to[p])
                qr[j-L[i]+1].emplace_back(to[p],i);
        }
    }
    static int dx[Maxn+5]; iota(dx+1,dx+n+1,1);
    For(i,1,n) len[i]=s[i].size();
    sort(dx+1,dx+n+1,[&](int x,int y){return len[x]>len[y];});
    DS.Build();
    for(int _=Maxk,it=1;_>=1;--_) if(!qr[_].empty())
    {
        while(it<=n && len[dx[it]]>=_)
        {
            int id=dx[it++],l=in[idx[id]],r=out[idx[id]];
            DS.Add(l,r,1);
        } for(auto [x,id]:qr[_]) ans[id]+=DS.Count(in[x]);
    }
    For(i,1,m) cout<<ans[i]<<endl;
    // cerr<<1.0*clock()/CLOCKS_PER_SEC<<endl;
    return 0;
}
```

## D

锐评：没有任何技术难度。

我们直接对 $s_i=1$ 的每一天钦定那一天的人是否被拒绝。

设 $h_i$ 为第 $i$ 天以前被拒绝的总人数。那么如果第 $i$ 天的人没被拒绝一定满足 $c>h_i$，否则 $c\le h_i$。

我们考虑容斥，把 $c>h_i$ 容斥成「无限制」减去「$c\le h_i$」。

那么我们的所有限制都形如 $c\le h_i$ 的形式。注意到 $h_i$ 单调不降，根据经典结论，设有限制的 $h_i$ 依次为 $h_{p_1},h_{p_2},\cdots,h_{p_k}$，$sum_i=\sum_{j}[c_j\le i]$，答案为 $(n-k)!\prod_{i=1}^k sum_{h_{p_i}}-(i-1)$。

我们设 $f_{i,j,k}$ 表示考虑完前 $i$ 天，有 $j$ 个人被拒，有限制的 $h_i$ 共有 $k$ 个的方案数。直接转移即可。

总时间复杂度 $O(n^3)$。

推荐用时：30min

```cpp
#include<bits/stdc++.h>
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=500,Mod=998244353;

int n,m,s[Maxn+5],c[Maxn+5],sum[Maxn+5];
int C[Maxn+5][Maxn+5],fac[Maxn+5];
int f[2][Maxn+5][Maxn+5];

int main()
{
    freopen("employ.in","r",stdin);
    freopen("employ.out","w",stdout);

    cin>>n>>m;
    For(i,1,n) scanf("%1d",&s[i]);
    For(i,1,n) cin>>c[i],sum[c[i]]++;
    For(i,1,n) sum[i]+=sum[i-1];
    C[0][0]=fac[0]=1;
    For(i,1,Maxn) fac[i]=1ll*fac[i-1]*i%Mod;
    For(i,1,Maxn)
    {
        C[i][0]=1;
        For(j,1,i) C[i][j]=(C[i-1][j]+C[i-1][j-1])%Mod;
    }
    f[0][0][0]=1;
    For(i,1,n)
    {
        int o=(i&1),p=(o^1); memset(f[o],0,sizeof(f[o]));
        if(s[i]==0) {For(j,0,i-1) For(k,0,i-1) f[o][j+1][k]=(f[o][j+1][k]+f[p][j][k])%Mod;}
        else
        {
            For(j,0,i-1) For(k,0,i-1) if(f[p][j][k])
            {
                int res=f[p][j][k];
                f[o][j+1][k+1]=(f[o][j+1][k+1]+1ll*res*max(0,sum[j]-k))%Mod;
                f[o][j][k]=(f[o][j][k]+res)%Mod;
                f[o][j][k+1]=(f[o][j][k+1]+1ll*(Mod-res)*max(0,sum[j]-k))%Mod;
            }
        }
    }
    int ans=0;
    For(i,0,n-m) For(j,0,n) if(f[n&1][i][j]) ans=(ans+1ll*f[n&1][i][j]*fac[n-j])%Mod;
    cout<<ans<<endl;
    return 0;
}
```