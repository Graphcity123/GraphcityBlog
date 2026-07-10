---
title: CSP2024 解题报告
date: 2024-10-27
tags:
  - OI
---

宝刀未老！

省流：没有上 392pts 的自行反思

## Duel

排序，后一个打前一个。$O(n\log n)$。

参考用时：5min

```cpp
#include<bits/stdc++.h>
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=2e5;

int n,a[Maxn+5];

int main()
{
    cin>>n;
    For(i,1,n) cin>>a[i];
    sort(a+1,a+n+1);
    int it=1;
    For(i,2,n) if(a[i]>a[it]) it++;
    cout<<n-it+1<<endl;
    return 0;
}
```

## Detect

运动学，这不是我的优势区吗？

主要就是利用公式 $v_1^2-v_0^2=2ax$，求出固定位移后的速度。每个车辆被拦截的一定是一段区间，所以第二问直接贪心即可。$O(n\log n)$。

参考用时：15min

```cpp
#include<bits/stdc++.h>
#define ll long long
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=2e5;

int T,n,m,L,V,p[Maxn+5];
int d[Maxn+5],v[Maxn+5],a[Maxn+5];
int cl[Maxn+5],cr[Maxn+5];

inline int Check(int id,int x)
{
    x=p[x]-d[id];
    if(a[id]==0) return (v[id]>V);
    if(a[id]<0)
    {
        ll res=2*a[id]*x+1ll*v[id]*v[id];
        if(res<=0) return 0;
        return (res>1ll*V*V);
    }
    if(a[id]>0)
    {
        ll res=2*a[id]*x+1ll*v[id]*v[id];
        return (res>1ll*V*V);
    }
}
inline void Solve()
{
    cin>>n>>m>>L>>V;
    For(i,1,n) cin>>d[i]>>v[i]>>a[i];
    For(i,1,m) cin>>p[i];
    For(i,1,n)
    {
        cl[i]=1,cr[i]=0;
        int ql=lower_bound(p+1,p+m+1,d[i])-p;
        if(a[i]>=0)
        {
            int l=ql,r=m+1;
            while(l<r)
            {
                int mid=(l+r)/2;
                if(Check(i,mid)) r=mid; else l=mid+1;
            } cl[i]=l,cr[i]=m;
        }
        else
        {
            int l=ql-1,r=m;
            while(l<r)
            {
                int mid=(l+r+1)/2;
                if(Check(i,mid)) l=mid; else r=mid-1;
            } cl[i]=ql,cr[i]=l;
        }
    }
    int cnt=0;
    For(i,1,n) cnt+=(cl[i]<=cr[i]);
    if(cnt==0) {cout<<0<<' '<<m<<endl; return;}
    vector<pair<int,int>> vx;
    For(i,1,n) if(cl[i]<=cr[i]) vx.emplace_back(cl[i],cr[i]);
    sort(vx.begin(),vx.end(),[&](auto a,auto b){
        return a.second<b.second;
    });
    int all=0,it=0;
    for(auto [l,r]:vx) if(l>it) all++,it=r;
    cout<<cnt<<' '<<m-all<<endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin>>T;
    while(T--) Solve();
    // cerr<<1.0*clock()/CLOCKS_PER_SEC<<endl;
    return 0;
}
```

## Color

注意到红蓝颜色等价，考虑使用差分。对于两个下标分别为 $l,r$ 的相同数字，如果需要造成贡献，那么就必须要在差分数组的第 $l+1,r$ 项为 1，中间的为 0。如果 $r=l+1$ 那么只需要要求第 $r$ 项为 0 就好了。

第二种情况在对应位置打个标记就好了。对于第一种情况，注意到所有的限定区间至多只能够首尾重合，设 $f_i$ 表示最后一个 1 在第 $i$ 项的最大值，想怎么转移怎么转移。$O(n)$。

参考用时：15min

```cpp
#include<bits/stdc++.h>
#define ll long long
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=1e6;
const ll inf=1e18;

int T,n,a[Maxn+5]; ll sum[Maxn+5],f[Maxn+5],ans;
ll mx[Maxn+5]; int ps[Maxn+5];

inline void Solve()
{
    cin>>n;
    For(i,1,n) cin>>a[i],mx[a[i]]=-inf;
    Rof(i,n,1) ps[a[i]]=i;
    For(i,1,n) if(a[i]==a[i-1]) sum[i]+=a[i];
    For(i,1,n) sum[i]+=sum[i-1];
    ll cur=0;
    For(i,1,n)
    {
        if(ps[a[i]]<i)
        {
            int k=ps[a[i]];
            f[i]=sum[i-1]-sum[k+1];
            f[i]=max(f[i],mx[a[i]]+sum[i-1]);
            f[i]+=a[i];
        }
        cur=max(cur,f[i]-sum[i]);
        if(i>1)
        {
            mx[a[i-1]]=max(mx[a[i-1]],cur-sum[i]+sum[i-1]);
        }
    } ans=sum[n];
    For(i,1,n) ans=max(ans,f[i]+sum[n]-sum[i]);
    cout<<ans<<endl;
    For(i,0,n) sum[i]=f[i]=0;
}

int main()
{
    cin>>T;
    while(T--) Solve();
    return 0;
}
```

## Arena

考虑首先将序列后面补零，填成 $2^k$ 的长度。然后我们考虑时间倒流：从后往前擦除数字。这里只考虑通关到根结点的答案。

如果一个结点的胜者可以是被擦除的点，我们称其为「未定义点」。注意到如下性质：

1. 第 $k$ 轮的未定义点的取值范围可以是 $[k,+\infty)$。
2. 所有连通的未定义点等价。
3. （性质二推广）任何一个未定义点都可以通关到它所在连通块的最顶层。
4. 对于任意一个时刻，一个结点的取值要么跟最开始相同，要么是未定义点。

然后考虑未定义点和定义点之间的合并：

1. 定义点+定义点：按照原有规则判断胜负。
2. 左定义点+右未定义点：如果擂主是左边而且能赢，那么父亲结点仍然取左儿子的值。否则父亲结点是未定义点。
3. 未定义点+未定义点：父亲显然是未定义点。

显然左未定义点+右定义点的合并是不存在的，因为我们从后往前擦除数字。

这样我们就可以通过模拟求出每个结点变成未定义点的时刻。注意到每个点至多变化一次，所以这个是 $O(n)$ 的。

接下来考虑判断一个点能否通关。对于定义点我们存在三个判句：

1. 它到根结点的链上，如果有结点擂主指向它，那么它的值就必须大于等于那个结点对应的轮数。
2. 否则，如果它是右儿子，那么左儿子不能够获胜。（由于当然结点还是定义点，所以左儿子一定也是定义点，这个可以直接在最开始就进行判断）
3. 如果它是左儿子，那么如果右儿子在原有情况能够获胜，那么能够通关意味着它要变成未定义点。

对于未定义点的通关判句很简单：它与根结点连通（它到根结点的链上一定都是未定义点）。

所以我们只需要维护：

1. 根结点到某一结点的链上，时间戳的最大值。（对应未定义点判句）
2. 根结点到某一结点的链上，所有擂主边的轮数最大值（对应定义点判句 1）
3. 根结点到某一结点的链上，是否存在定义点判句 2 中的不合法情况。
4. 根结点到某一结点的链上，所有在判句 3 中需要变成未定义点的结点，时间戳的最大值。

显然都可以 $O(n)$ 求出。

显然一个结点能够获胜的 $c$ 一定是一段前缀（仅考虑通关到根结点的情况）。我们求出每个结点能够通关的最先时刻，然后前缀和一下就好了。

但是这题的通关结点不一定是根结点。比如 $c<n/2$ 的时候通过到根结点的左儿子即可，$c<n/4$ 的时候只需要通过到根结点的左儿子的左儿子即可，$\cdots\cdots$。一个比较粗鲁的解决办法是对于每个通关结点都执行一遍上面的过程。这样做是 $O(n+n/2+n/4+\cdots)=O(n)$ 的。

当然这样做是过不去的，你会收获 88~92pts 的好成绩。

我们考虑分析通关结点的变化会导致什么改变。

1. 每个结点变成未定义点的时间戳不变。
2. 定义点的判句 2 不改变。
3. 实际上定义点的判句 3 也不会改变。因为如果通关结点下移的时刻一定要晚于判句 3 中需要变成未定义点的结点，变成未定义点的时刻。
4. 同理，对于未定义点的判句也不改变。
5. 第一个改变在于定义点的判句 1。通关结点的下移可能会导致原来的一些限制消失。这个是好解决的，只需要对每个点考虑阻碍它的第一条擂主边在哪里。如果通关结点在这条边下面判句 1 成立，否则不成立。
6. 第二个改变在于一个点的生效时刻不再是一段前缀，而是一个区间。好在这个区间的左端点很好求（就是它不再在通关结点子树中的时刻）

总时间复杂度 $O(n)$。

参考用时：思考 30min + 实现 30min + 卡常 1h~1.5h

```cpp
#include<bits/stdc++.h>
#define ll long long
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Rof(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
const int Maxn=3e5,Maxk=3e5,inf=1e9;

inline int read()
{
    char ch=getchar();
    int f=1,x=0;
    while(ch>'9' || ch<'0')
    {
        if(ch=='-') f=-1;
        ch=getchar();
    }
    while(ch>='0' && ch<='9')
    {
        x=x*10+ch-'0';
        ch=getchar();
    }
    return x*f;
}

int T,m,s,a1[Maxn+5],a[Maxn+5],c[Maxn+5],tim; ll ans[Maxn+5],num[Maxn+5];
int h[Maxn+5],d[Maxn+5],mx[Maxn+5],cnt[Maxn+5];
int g[Maxn+5],f[Maxn+5],tmn[Maxn+5],smx[Maxn+5];
int N,dx[22][Maxk+5],w[Maxn+5],chk[Maxn+5],lst[Maxn+5];
// h: 擂主方
// d: 深度
// w: 本原赢家
// f: 占领时间

#define ls(x) (x<<1)
#define rs(x) (x<<1|1)

inline void Add(int x)
{
    f[x]=tim;
    for(int fa=(x>>1);fa>=1;fa>>=1,x>>=1)
    {
        if(f[fa]!=-1) break;
        if(x==ls(fa)) f[fa]=tim;
        if(x==rs(fa) && h[fa]==0 && w[ls(fa)]>=d[fa]) break;
        f[fa]=tim;
    }
}

inline void Work(int n)
{
    memset(ans,0,sizeof(ll)*(n+2));
    memset(f,-1,sizeof(int)*(n*2+2));
    for(int r=n-1,op=1;r;r/=2,op++)
    {
        int l=(r+1)/2; int it=0;
        For(i,l,r) h[i]=dx[op][++it];
    }
    For(i,n,n*2-1) d[i]=0; Rof(i,n-1,1) d[i]=d[i*2]+1;
    For(i,n,n*2-1) w[i]=a[i-n+1];
    Rof(i,n-1,1)
    {
        int p=i*2+h[i],q=p^1;
        if(w[p]>=d[i]) w[i]=w[p];
        else w[i]=w[q];
    }
    mx[1]=cnt[1]=0;
    for(int fa=1,i=2;i<n*2;i+=2,fa++)
    {
        mx[i]=mx[fa],cnt[i]=cnt[fa];
        mx[i+1]=mx[fa],cnt[i+1]=cnt[fa];
        int p=i+h[fa]; mx[p]=max(mx[p],d[fa]);
        if(!h[fa] && w[i]>=d[fa]) cnt[i+1]++;
    }
    Rof(i,n,1) tim=i-1,Add(n+i-1); smx[1]=f[1],tmn[1]=n;
    for(int fa=1,i=2;i<n*2;i+=2,fa++)
    {
        tmn[i]=tmn[fa]; smx[i]=min(smx[fa],f[i]);
        tmn[i+1]=tmn[fa]; smx[i+1]=smx[fa];
        if(h[fa] && w[i+1]>=d[fa]) tmn[i]=min(tmn[i],f[i+1]);
    }
    For(i,n,n*2-1)
    {
        int res=smx[i];
        if(!cnt[i])
        {
            int k=tmn[i],p=0;
            for(p=i;p;p>>=1)
            {
                if(p==1) break; int fa=(p>>1);
                if(h[fa]==(p&1) && w[i]<d[fa]) break;
            }
            if(chk[p]) res=max(res,min(tmn[i],chk[p]));
        }
        g[i]=res;
    }
    for(int l=n/2,r=n;r;r/=2,l/=2)
        {For(k,l+1,r) if(g[k+n-1]>l) ans[g[k+n-1]]+=k,ans[l]-=k;}
    Rof(i,n-1,1) ans[i]+=ans[i+1];
    For(i,1,n) num[i]=ans[i];
}
inline void Solve()
{
    static int X[4]; For(i,0,3) X[i]=read();
    For(i,1,N) if(a1[i]!=-1) a[i]=a1[i]^X[i%4];
    Work(N); num[1]=1; ll all=0;
    For(i,1,m) all^=(1ll*i*num[c[i]]);
    printf("%lld\n",all);
}

int main()
{
    int n; n=read(),m=read();
    For(i,1,n) a1[i]=read();
    For(i,1,m) c[i]=read();
    int _n=1; while(_n<n) _n*=2; n=_n;
    for(int r=n-1,op=1;r;r/=2,op++)
    {
        int l=(r+1)/2; string ch; cin>>ch; int it=0;
        For(i,1,r-l+1) dx[op][i]=ch[it++]-'0';
    }
    for(int i=1,k=n;i<n*2;i=ls(i),k/=2) chk[i]=k,lst[d[i]]=i;
    T=read(); N=n;
    while(T--) Solve();
    return 0;
}
```