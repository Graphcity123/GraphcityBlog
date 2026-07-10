---
title: 多元微积分单核攻略，简单好抄
date: 2026-03-10
tags:
  - 数学
---

# 多元微积分单核攻略，简单好抄

## 前言

参考文献：《数学分析（II）讲义》- 张友金

本文可以作为参考文献的辅助学习资料，其中的若干记号沿用了参考文献。

说实话，在第一次读这本讲义的微分学部分的时候，我读懂了 0 个字。每个定理是什么，在干什么，每一步证明过程的动机是什么，都是完全不知道的。在与 deepseek 持之以恒的对话中，我才可以逐渐理解每个定理的意义，每一步证明的理由。

这篇文章主要就是以一种“几何直观”的方式来叙述各种定理及其证明，虽然在严谨性方面可能有些许不足，但更加容易上手，也正如标题所言“单核攻略，简单好抄”。

Take Easy！

## 从一元函数到多元函数

回顾一元微积分：

$$
\dfrac{\mathrm{d} f}{\mathrm{d} x}=f’(x)
$$

不过我们先不用这个形式，我们用另外一种形式：

$$
\mathrm{d} f(x_0)(t)=tf’(x_0)
$$

把微分符号 $\mathrm{d}$ 看成一个算子，输入原函数 $f$ 和某一个点 $x_0$，通过 $\mathrm{d}$ 后会输出一个线性函数 $\mathrm{d} f(x_0)(t)$。

这个函数有什么用？我们可以通过这个函数得到 $f(x)$ 在 $x_0$ 近旁的一个一阶线性近似：

也就是 $x_0+t\to f(x_0)+\mathrm{d} f(x_0)(t)$ 这条直线，即 $f(x)$ 在 $x_0$ 处的切线。

可能大家会觉得理解成一个“算子”很多余。明明用一个数字 $f’(x_0)$ 就可以表示，为什么要那么复杂？这个问题相信你到后面就会明白了。

现在我们来到多元函数。对多元函数微分是什么意思？类比一下一元微积分，我们希望在 $x_0$ 的近旁，找到一个最佳的线性函数来拟合 $f$。对于多元函数也是一样，我们希望在 $x_0$ 的近旁，找到一个最佳的线性函数来拟合 $f$。

怎么拟合？我们可以先回到最熟悉的一维情况。假设 $f$ 是一个二元函数，如果要考察在 $(x_0,y_0)$ 近旁的拟合，那我们就先固定 $y=y_0$，只让 $x$ 在 $x_0$ 附近自由变动（如果把值域看成 $z$ 维度，就相当于把 $f$ 的图像放到 $y=y_0$ 的截面上讨论，这样它就看起来像我们熟悉的“一条曲线”），这样 $f(x,y_0)$ 就是一个一元函数，我们可以对其求导。设 $\dfrac{\partial f}{\partial x}(x_0,y_0)=\dfrac{\mathrm{d}f(x,y_0)}{dx}(x_0)$（注意这是个数字）

那么在 $y=y_0$ 的截面上，$x_0$ 的近旁，$(x_0+t,y_0,f(x_0,y_0)+t\dfrac{\partial f}{\partial x}(x_0,y_0))$ 就是对 $f$ 的一阶线性拟合。

同理，我们再固定 $x=x_0$，只让 $y$ 在 $y_0$ 附近自由变动，我们也可以得到一个线性拟合：$(x_0,y_0+t,f(x_0,y_0)+t\dfrac{\partial f}{\partial y}(x_0,y_0))$。

看看我们最终的目的：我们希望找到一个最佳的线性函数来拟合 $f$。也就是说，我们希望这个函数是线性的，也就是每个维度都独立且线性。刚才的操作，我们刚好得到了每个维度的线性拟合，那么我们把它们合并在一起不就是那个目标的线性函数了吗？

不管是不是真的，我们先这样做再说：这个目标函数至少看起来很像：（$t=(t^1,t^2)^\mathrm{T}$ 为二维向量）

$$
(x_0+t^1,y_0+t^2)\to f(x_0,y_0)+t^1\dfrac{\partial f}{\partial x}(x_0,y_0)+t^2\dfrac{\partial f}{\partial y}(x_0,y_0)
$$

它构成了一个过 $(x_0,y_0,f(x_0,y_0))$ 的一个“切平面”。如果我们用列向量表示每个点，那就是：

$$
\begin{bmatrix}x_0 \\ y_0\end{bmatrix}+t\to f(x_0,y_0)+\begin{bmatrix}\dfrac{\partial f}{\partial x}(x_0,y_0) & \dfrac{\partial f}{\partial y}(x_0,y_0) \end{bmatrix}t
$$

对于 $n$ 元函数 $f(x)$，通过类似的方法，我们还是可以控制其它维全都不动，只有第 $i$ 维变动，然后对以 $x^i$ 为自变量的一元函数求导，得到 $\dfrac{\partial f}{\partial x^i}(x_0)=\dfrac{\mathrm{d}f(x_0^1,\cdots,x_0^{i-1},x,x_0^{i+1},\cdots,x_0^n)}{\mathrm{d}x}(x_0^i)$。

同样地，我们可以通过这些“偏导数”求出一个最佳拟合的“超平面”：

$$
x_0+t\to f(x_0)+\begin{bmatrix}\dfrac{\partial f}{\partial x^1}(x_0) & \dfrac{\partial f}{\partial x^2}(x_0) & \cdots & \dfrac{\partial f}{\partial x^n}(x_0)\end{bmatrix} t
$$

我们发现这个矩阵 $\begin{bmatrix}\dfrac{\partial f}{\partial x^1}(x_0) & \dfrac{\partial f}{\partial x^2}(x_0) & \cdots & \dfrac{\partial f}{\partial x^n}(x_0)\end{bmatrix}$ 跟我们之前的 $\mathrm df(x_0)$ 很像。它都是一个线性映射，将一个偏移向量 $t$ 映射到值的偏移。我们称它为 $f$ 在 $x_0$ 的 **Jacobi 矩阵** 或 **Jacobian**，记作 $J_f(x_0)$。

现在，类比一元微积分里面的 $x_0+t\to f(x_0)+f’(x_0)t$，我们在多元函数里面有 $x_0+t\to f(x_0)+J_f(x_0)t$。可以看到，在多元微分学里面，$J_f(x_0)$ 和一元微积分里面 $f’(x_0)$ 承担的功能很像。

但是，我们有一个问题没有解决————是的，这是一个看起来很棒的线性拟合，但我们只讨论了沿着标准向量移动的情况。如果沿着任意方向走会怎样？甚至我们不沿着一个向量走，沿着一个曲线走的话，它能否还是一个“很棒的”拟合？

首先做一个准备工作：什么拟合是“很棒的”？类比于一元微积分，对于一个线性映射 $\varphi$ 我们希望 $f(x_0+t)-(f(x_0)+\varphi(t))=o(t)$，也就是这个线性拟合的结果和原函数得到结果的差值控制在一阶以下。如果存在这样的线性映射，我们就认为 $f$ 是可微的。我们希望得到的结果是：$J_f(x_0)$ 就是这样一个好的线性映射。

现在，我们来证明：

**设 $f: X\to \mathbb{R}$ 在 $x_0$ 的某一邻域 $U\subset X$ 存在所有偏导数 $\dfrac{\partial f}{\partial x^i}$，且它们在 $x_0$ 处连续，则 $f$ 在 $x_0$ 处可微。**

> 首先偏导数只能处理只有一维变动的情况，所以我们先要把 $f(x_0+h)-f(x_0)-J_f(x_0)h$ 拆成每一维各自独立的贡献之和。对于每一维的贡献，我们需要证明它在一个可控的小范围内（$o(h)$ 级别），如果所有维度的贡献都是 $o(h)$ 级别，那它们的和也是 $o(h)$ 的，这样就可以得证了。

证明：不妨令 $U=B(x_0,\delta)\subset X$。我们考虑一个维度一个维度走，把 $x_0$ 到 $x_0+h$ 的路径拆成 $x_0\to x_0+h^1e^1\to x_0+h^1e^1+h^2e^2\to\cdots\to x_0+h$。（$e^i$ 是第 $i$ 维第标准向量）

那么 $f(x_0+h)-f(x_0)=\sum_{i=1}^n f(x_0+h^1e^1+\cdots+h^ie^i)-f(x_0+h^1e^1+\cdots+h^{i-1}e^{i-1})$

对于求和的第 $i$ 项，只有第 $i$ 维增加了 $h^i$。这提示我们用第 $i$ 维的偏导数处理问题。根据一元函数的 Lagrange 中值定理，有：

$$
f(x_0+h^1e^1+\cdots+h^ie^i)-f(x_0+h^1e^1+\cdots+h^{i-1}e^{i-1})=h^i\dfrac{\partial f}{\partial x^i}(x_0+h^1e^1+\cdots+h^{i-1}e^{i-1}+\theta h^ie^i)
$$

这里的 $\theta$ 是 $(0,1)$ 之间的实数。那么 $f(x_0+h)-f(x_0)-J_f(x_0)h$ 就可以表示成：

$$
\begin{aligned}
& \sum_{i=1}^n h^i(\dfrac{\partial f}{\partial x^i}(x_0+h^1e^1+\cdots+h^{i-1}e^{i-1}+\theta h^ie^i)-\dfrac{\partial f}{\partial x^i}(x_0))\\
\le & ||h||\sum_{i=1}^n \dfrac{\partial f}{\partial x^i}(x_0+h^1e^1+\cdots+h^{i-1}e^{i-1}+\theta h^ie^i)-\dfrac{\partial f}{\partial x^i}(x_0)
\end{aligned}
$$

由于所有偏导数都连续，所以 $h\to 0$ 的时候右边的求和趋近于 0，整个误差是 $o(h)$ 的，证毕。

综上，我们得到了：$J_f(x_0)$ 就是 $f(x)$ 在 $x_0$ 处的最佳线性拟合，通过它可以导出一个切超平面 $x_0+t\to f(x_0)+J_f(x)t$，这个平面就是 $f$ 在 $x_0$ 旁的最佳线性近似。

## 从多元函数到多元映射

首先我们注意到，对于多元映射 $f$，值域的每一维都由一个独立的函数 $f^i(x)$ 来构造。我们希望找到一个最佳的线性映射 $\varphi$ 来对映射 $f:\mathbb{R}^n\to \mathbb{R}^m$ 进行拟合。

那既然每一维是独立的，我们对于每一维分别做一次上面多元函数的微分工作不就好了吗？确实是这样。对于 $f^i(x)$，上文中我们就得到了其最佳的线性映射：

$$
x_0+t\to f^i(x_0)+J_{f^i}(x_0)t
$$

我们如果把值域也表示成列向量的形式，即 $f(x)=(f^1(x),f^2(x),\cdots,f^m(x))^\mathrm{T}$，那么我们就可以得到这样一个线性拟合：

$$
x_0+t\to f(x_0)+\begin{bmatrix}J_{f^1}(x_0)\\ J_{f^2}(x_0)\\\cdots\\ J_{f^m}(x_0)\end{bmatrix}t
$$

根据可微性的定义，对于值域的每一维都是最佳的线性拟合，显然有 $f$ 可微，且其最佳的线性映射是 $\begin{bmatrix}J_{f^1}(x_0)\\ J_{f^2}(x_0)\\\cdots\\ J_{f^m}(x_0)\end{bmatrix}=(\dfrac{\partial f^i}{\partial x^j}(x_0))$。我们也把它称为 $f$ 在 $x_0$ 处的 Jacobi 矩阵（或 Jacobian）。

不论是一元函数的所谓“切线”和多元函数的“切超平面”，这些都是值域只有一维的多元函数的特殊理解。对于多元映射，我们更需要抓住微分的线性映射本质：$J_f(x_0)$ 表示，在 $x_0$ 的近旁，$f$ 对应的变换近似于这个线性变换，这个变换原来的原点是 $x_0$，新的原点是 $f(x_0)$。

对于 $x_0$ 的一个足够小邻域，如果它是一个球，那它在经过 $f$ 的变换后会变成一个椭球。这个椭球可能会有一些小的变化（比如边界有小弯曲），但这个变化是可控且足够小的，不影响其整体近似于做一次 $J_f(x_0)$ 的线性变换。

现在我们更加应该把微分看成一种“局部的线性变换近似”，它告诉我们，虽然整体上 $f$ 代表的变换不是线性的，但它的局部可以进行线性的拟合，且很可能拥有很多线性映射类似的相关性质。下文我们将探讨这些“相关性质”。

## 逆映射定理

类似线性代数中的方阵，由于映射前后的维数不变，所以有很多独特的性质或讨论点（如行列式，逆阵，特征值等）。我们也探讨前后维数不变的映射。

设 $f:X\to Y$ 为 $x_0\in\mathbb{R}^n$ 的邻域 $X$ 到 $y_0=f(x_0)\in\mathbb{R}^n$ 的邻域 $Y$ 的映射，$f$ 连续可微。

我们知道，如果一个 $n$ 阶方阵 $A$ 满足 $\det(A)\not=0$ 则 $A$ 可逆。类比到多元映射上，如果 $\det(J_f(x_0))\not=0$，那是否存在 $x_0$ 的邻域 $U$ 和 $y_0$ 的邻域 $V$，使得 $f$ 也可逆呢？如果可逆，那是否也有 $J_{f^{-1}}(y_0)=J_f(x_0)^{-1}$ 呢？接下来我们将证明：

**（逆映射定理）存在 $x_0$ 的邻域 $U$ 和 $y_0$ 的邻域 $V$ 使得 $f|_U:U\to V$ 为 $C^1$-微分同胚，且对任意给定的 $y\in V$ 都有 $J_{f^{-1}}(y)=J_f(x)^{-1}$，其中 $x=f^{-1}(y)$**。

（$f:U\to V$ 是 $C^1$-微分同胚是指 $f$ 为一一映射，且 $f,f^{-1}$ 均连续可微）

在此之前，我们先做一点准备工作：

**（线性算子的有界性）设 $$A$$ 为可逆线性变换，存在 $\lambda>0$ 使得 $||Ax||\ge \lambda||x||$ 对任意 $x$ 成立。**

证明：$||x||=||A^{-1}Ax||\le ||A^{-1}||||Ax||$，所以 $||Ax||\ge \dfrac{1}{||A^{-1}||}||x||$，取 $\lambda=\dfrac{1}{||A^{-1}||}$ 即可。

**（拟微分中值定理推论）设 $a,b\in\mathbb{R}$，$a<b$，若映射 $f:[a,b]\to \mathbb{R}^m$ 连续且在 $(a,b)$ 可微，则存在 $t_0\in(a,b)$ 使得 $||f(b)-f(a)||\le||J_f(t_0)||(b-a)$。**

> 从物理上理解，$f(t)$ 是粒子在空间中随时间运动的轨迹。我们要证明的就是，粒子的位移 $||f(b)-f(a)||$ 小于等于某一时刻的速度 $||J_f(t_0)||$ 乘以时间差 $(b-a)$。直觉上来说必然是对的，我们直接取速度最大的那一刻就行了。
> 
> 如何证明？既然是看位移，我们就只看粒子在 $f(b)-f(a)$ 这一方向的位移大小，再通过一元的拉格朗日中值定理，知道在这个方向上某一时刻的速度等于平均速度，显然原本的速度大于等于投影方向的速度，这样就证明完了。

证明：设 $x:[a,b]\to \mathbb{R}$，$x(t)=\langle f(b)-f(a),f(t) \rangle$。根据复合函数链式求导法则，$x’(t)=\langle f(b)-f(a),\operatorname{grad} f(t)\rangle$。根据一元 Lagrange 中值定理，$x(b)-x(a)=x’(t_0)(b-a)$，其中 $t_0\in(a,b)$。

由于 $\langle p,q\rangle\le ||p||||q||$，所以：

$$
\begin{aligned}
x(b)-x(a) &= x’(t_0)(b-a) \\
\langle f(b)-f(a),f(b)-f(a)\rangle &= \langle f(b)-f(a),J_f(t)\rangle (b-a) \\
||f(b)-f(a)||^2 &\le ||f(b)-f(a)||\times ||J_f(t)||\times (b-a) \\
||f(b)-f(a)|| & \le ||J_f(t) || (b-a)
\end{aligned}
$$

证毕。

**（压缩映射定理）设 $D$ 为 $\mathbb{R}^n$ 中的闭集，$f:D\to D$ 连续，且满足存在 $0<\lambda<1$，$\forall x,y\in D$，都有 $d(f(x),f(y))\le \lambda d(x,y)$，则存在恰好一个点满足 $f(x)=x$**。

证明：首先我们证明存在一个合法点。任取一个点 $a_0$，构造点列 $a_{n+1}=f(a_n)$。根据题目，对于任意 $p<q$，我们有：

$$
\begin{aligned}
d(a_p,a_q) &\le \sum_{i=p}^{q-1}d(a_i,a_{i+1})\\
&\le d(a_p,a_{p+1})+\lambda\sum_{i=p+1}^{q-1}d(a_{i-1},a_{i-2})\\
&\le d(a_p,a_{p+1})(1+\lambda)+\lambda^2\sum_{i=p+2}^{q-1}d(a_{i-2},a_{i-3})\\
& \ \ \vdots \\
& \le d(a_p,a_{p+1})(1+\lambda+\lambda^2+\cdots+\lambda^{q-p-1})\\
& \le d(a_0,a_1)\lambda^p\times \dfrac{1-\lambda^{q-p}}{1-\lambda}\\
& \le \lambda^p \dfrac{d(a_0,a_1)}{1-\lambda} \to 0
\end{aligned}
$$

所以 $\{a_n\}$ 为 Cauchy 点列，最终会收敛至一个点（设为 $a$）。下证 $f(a)=a$：

考虑反证法，若 $f(a)\not= a$，由于 $\{a_n\}$ 收敛，当 $n$ 足够大时 $d(a_n,a)<\dfrac{d_0}{8}$，此时 $d(f(a_n),f(a))\le \lambda\dfrac{d_0}{8}<\dfrac{d_0}{8}$。而 $a_{n+1}=f(a_n)$，所以有 $d(a_{n+1},f(a))<\dfrac{d_0}{8}$，同时 $d(a_{n+1},a)<\dfrac{d_0}{8}$，所以 $d_0=d(a,f(a))\le d(a,a_{n+1})+d(a_{n+1},f(a))<\dfrac{d_0}{8}+\dfrac{d_0}{8}=\dfrac{d_0}{4}$，矛盾，所以 $f(a)=a$。

如果 $a\not=b$，$f(a)=a$，$f(b)=b$，则 $d(a,b)=d(f(a),f(b))\le \lambda d(a,b)<d(a,b)$ 矛盾，所以只有恰好一个点合法。

> 知道这个定理有什么用？这个定理重要的一点是：对于一个确定的压缩映射 $f$，只有恰好一个点 $x$ 是合法的。如果我们对于每一个 $y\in V$，都能够构造一个压缩映射 $g_y(x)$，而且只让恰好一个 $x$ 满足，而且这个 $x$ 刚好有 $y=f(x)$ 的话，那我们就找到逆映射了！
> 
> 如何构造 $g_y(x)$？结合压缩映射的条件方程 $x=g_y(x)$ 和逆映射的条件方程 $y=f(x)$，我们可以构造 $g_y(x)=x-f(x)+y$，此时 $x=g_y(x)$ 就意味着 $y=f(x)$。
> 
> 现在的问题就是，如何找到一个满足 $g_y(x)=x-f(x)+y$ 是压缩映射的定义域？根据定义，$d(g_y(x_1),g_y(x_2))\le\lambda d(x_1,x_2)$，即 $d(x_1-f(x_1),x_2-f(x_2))\le\lambda d(x_1,x_2)$，转化一下，变为 $d(x_1-x_2,f(x_1)-f(x_2))\le\lambda d(x_1-x_2,0)$，即 $||(x_1-f(x_1))-(x_2-f(x_2))||\le \lambda||x_1-x_2||$。
> 
> 由于平移函数不改变微分值，不妨令 $x_0=0$，$y_0=f(x_0)=0$。
> 
> 如果 $f$ 是恒等映射，那么 $g(x)=x-f(x)$ 几乎为零映射，且 $J_g(x_0)=O$。在 $x_2$ 处进行微分，那么 $g(x_1)-g(x_2)$ 可以通过拟微分中值定理由 $J_g(x_?)(x_1-x_2)$ 控制，完美！
> 
> 如果 $f$ 不是恒等映射，那么我们设 $g(x)=J_f(x_0)x-f(x)$ 进行类似操作即可。

**证明：** 不失一般性，令 $x_0=0$，$y_0=f(x_0)=0$。根据线性算子定理，设 $c=\dfrac{1}{||J_f(0)^{-1}||}$，对于任意向量 $x$ 都有 $||J_f(0)x||\ge c||x||$。

设 $g(x)=J_f(0)x-f(x)$，那么 $J_g(0)=O$，由于 $J_g(x)$ 也连续可微，存在 $\delta>0$ 使得任意 $x\in B(0,\delta)$ 都有 $||J_g(x)||<\dfrac{c}{2}$。

$\forall x_1,x_2\in B(0,\delta)$，令 $F(t)=g(x_2+t(x_1-x_2))$，根据链式求导法则有 $J_F(t)=J_g(x_2+t(x_1-x_2))(x_1-x_2)$。显然有 $||J_F(t)||\le ||x_1-x_2||\times ||J_g(x_2+t(x_1-x_2))||$。根据拟微分中值定理，$||g(x_1)-g(x_2)||= ||F(1)-F(0)||\le ||J_F(t_0)||(1-0)\le \dfrac{c}{2}||x_1-x_2||$。

继续推：

$$
\begin{aligned}
||g(x_1)-g(x_2)|| &\le \dfrac{c}{2} ||x_1-x_2|| \\
||J_f(0)(J_f(0)^{-1}(g(x_1)-g(x_2)))||&\le \dfrac{c}{2} ||x_1-x_2||\\
c||J_f(0)^{-1}(g(x_1)-g(x_2))|| &\le \dfrac{c}{2}||x_1-x_2|| \\
||x_1-x_2-J_f(0)^{-1}(f(x_1)-f(x_2))||&\le \dfrac{1}{2}||x_1-x_2||\\
d(x_1-J_f(0)^{-1}f(x_1),x_2-J_f(0)^{-1}f(x_2)) & \le \dfrac{1}{2}d(x_1,x_2)
\end{aligned}
$$

对于任意 $y$，设 $g_y(x)=x-J_f(0)^{-1}(f(x)-y)$。有 $d(g_y(x_1),g_y(x_2))\le\dfrac{1}{2}(x_1,x_2)$。设 $\alpha\in B(x_0,\delta)$，记 $\beta=f(\alpha)$，我们取 $r>0$ 使得 $\overline{B}(\alpha,r)\subset B(x_0,\delta)$。对任意取定的 $y\in B(\beta,\dfrac{c}{2}r)$，下证 $g_y(x)$ 在 $\overline{B}(\alpha,r)$ 上封闭：

即证 $d(g_y(x),\alpha)\le r$。

$$
\begin{aligned}
d(g_y(x),\alpha) &\le d(g_y(x),g_y(\alpha))+d(g_y(\alpha),\alpha)\\
&\le \dfrac{1}{2}(x,\alpha)+||J_f(0)^{-1}(y-\beta)||\\
&\le \dfrac{1}{2}r+||J_f(0)^{-1}||\times ||y-\beta||\\
&\le \dfrac{1}{2}r+\dfrac{1}{c}\times \dfrac{c}{2}r=r
\end{aligned}
$$

所以 $g_y(x)$ 是 $\overline{B}(\alpha,r)$ 上的一个压缩映射。根据压缩映射定理，存在唯一的 $x$ 使得 $g_y(x)=x$，即 $x=x-J_f(0)^{-1}(f(x)-y)$，由于 $J_f(0)$ 可逆，所以 $f(x)=y$。

最后是第一阶段的收尾工作：记 $U=B(x_0,\delta)$，$V=f(U)$，下证 $f|_U:U\to V$ 是 $C^1$-微分同胚。

若 $x_1\not=x_2$，取 $\alpha=x_0=0$，$r=\min(||x_1||,||x_2||)<\delta$，根据上文，$\overline{B}(x_0,r)$ 中的 $f$ 是一一映射，所以 $f(x_1)\not=f(x_2)$，所以 $f$ 在 $B(x_0,\delta)$ 中 $f$ 也是一一映射。所以 $f^{-1}$ 存在。

根据上文的不等式：

$$
\begin{aligned}
||x_1-x_2-J_f(0)^{-1}(f(x_1)-f(x_2))||&\le \dfrac{1}{2}||x_1-x_2||\\
||x_1-x_2||-||J_f(0)^{-1}(f(x_1)-f(x_2))|| &\le \dfrac{1}{2}||x_1-x_2||\\
\dfrac{1}{2}||x_1-x_2|| &\le ||J_f(0)^{-1}(f(x_1)-f(x_2))||\\
\dfrac{1}{2}||x_1-x_2|| &\le \dfrac{1}{c}||f(x_1)-f(x_2)|| \\
||f^{-1}(y_1)-f^{-1}(y_2)|| & \le \dfrac{2}{c}||y_1-y_2||
\end{aligned}
$$

所以 $f^{-1}(x)$ 连续，$f|_U$ 是微分同胚。证毕。

上文中我们说了如果 $J_f(x_0)$ 可逆，那么 $x_0$ 存在一个邻域 $U$ 使得 $f$ 限制在 $U$ 上是 $C^1$-微分同胚。不过我们还有一点没证完——为什么 $J_{f^{-1}}(y_0)=J_f(x_0)^{-1}$？

直接用复合函数的链式求导法则：$Id(x)=f^{-1}(f(x))=x$，则 $J_{Id}(x)=J_{f^{-1}}(y)\times J_f(x)=I_n$，其中 $y=f(x)$。显然有 $J_{f^{-1}}(y)=J_f(x)^{-1}$，证毕。

总结：逆映射定理告诉我们：可逆的线性近似可以推导出局部的微分同胚。

## 隐函数定理

接下来我们探讨线性方程组解的性质，并尝试通过微分的方式将其拓展到非线性函数。

对于线性方程组 $A\vec{t}=\vec{0}$，其中 $A$ 是 $n\times (n+m)$ 维矩阵，$\vec{t}$ 为 $n+m$ 维向量。这是一个有 $n+m$ 个未知数，$n$ 个方程的方程组。

根据线性代数理论，$\operatorname{rank}(A)+\dim \ker A=n+m$。若 $A$ 行满秩，假设 $A$ 的后 $n$ 列也满秩，则如果知道了前 $m$ 个未知数的取值（可以任意），对于后 $n$ 个未知数的取值是唯一确定的。

用线性代数的语言表示，就是对 $A$ 和 $t$ 进行分块，方程变为

$$
\begin{bmatrix}
X_{n\times m} & Y_{n\times n}
\end{bmatrix}
\begin{bmatrix}
\vec{x} \\ \vec{y}
\end{bmatrix}
=
\vec{0}
$$

其中 $Y$ 可逆，$\vec{x}$ 是 $m$ 维向量，$\vec{y}$ 是 $n$ 维向量。

上面的式子其实就是 $X\vec{x}+Y\vec{y}=\vec{0}$，由于 $Y$ 可逆，所以 $\vec{y}$ 可以唯一地用 $\vec{x}$ 表示：

$$
\vec{y}=-Y^{-1}X\vec{x}
$$

对于非线性的连续可微函数（可以理解为方程组）$F(x,y): \mathbb{R}^m\times \mathbb{R}^n\to \mathbb{R}^n$，由 $n$ 个函数（方程）$F^i(x,y)$ 组成。如果 $F(x_0,y_0)=0$（即 $x_0,y_0$ 是方程组的一组解），且 $J_F(x_0,y_0)$ 的后 $n$ 列可逆（即 $y$ 对应的偏导矩阵可逆），我们猜想：

**（隐函数定理）在 $(x_0,y_0)$ 的近旁，存在一个 $(x_0,y_0)$ 的邻域 $I$ 使得：在 $I$ 上 $F(x,y)=0$ 当且仅当 $y=f(x)$（即对 $x$ 可以找到唯一的 $y$ 构成解），且 $f$ 连续可微，并且：**

$$
J_f(x)=-J_{F_y}(x,f(x))^{-1}\times J_{F_x}(x,f(x))
$$

（注意到这个式子跟上文的 $\vec y=-Y^{-1}X\vec{x}$ 十分类似，这更加体现了微分作为一种“局部的线性近似”）

> 总结一下我们的问题：我们有方程 $F(x,y)=0$，想要找到解 $y=f(x)$。如果固定 $x$，问题就变成了解 $F_x(y)=0$，但 $x$ 变动的时候方程 $F_x$ 也会跟着变。我们希望找到一个办法统一处理所有 $F_x$ 的情况。
> 
> 所以我们尝试将 $(x,y)$ 映射到 $(x,F(x,y))$，这样解空间就被限制在 $(x,0)$。假设这个映射为 $G$，如果 $G$ 在 $(x_0,y_0)$ 附近可逆，那么根据逆映射定理，存在一个邻域使得 $(x,0)$ 能够被唯一地反向映射回 $(x,y)$，即我们找到了 $y=f(x)$。
> 
> 或者我们从线性代数的角度理解：已知 $\begin{bmatrix}X_{n\times m} & Y_{n\times n}\end{bmatrix}\begin{bmatrix}\vec{x} \\ \vec{y}\end{bmatrix}=\vec{0}$，怎么从 $\vec x$ 推出来 $\vec y$？假设 $\vec x=\vec{t}$，那我们发现 $x^i=t^i$ 刚好是 $m$ 个方程，再加上 $F$ 的 $n$ 个方程，刚好就是 $n+m$ 个方程。方程和未知数的个数相等，我们就可以直接解了：
> 
> $\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}\begin{bmatrix} \vec{x} \\ \vec{y}\end{bmatrix}=\begin{bmatrix}\vec t \\ \vec 0\end{bmatrix}$，$\begin{bmatrix} \vec{x} \\ \vec{y}\end{bmatrix}=\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}^{-1}\begin{bmatrix}\vec t \\ \vec 0\end{bmatrix}$
> 
> 所以 $f(\vec{t})=\begin{bmatrix}O & I_n\end{bmatrix}\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}^{-1}\begin{bmatrix}I_m \\ O\end{bmatrix}\vec{t}$，$f=\begin{bmatrix}O & I_n\end{bmatrix}\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}^{-1}\begin{bmatrix}I_m \\ O\end{bmatrix}$ 就是我们想要的那个求出解的线性映射。

证明：设 $G:\mathbb{R}^m\times \mathbb{R}^n\to \mathbb{R}^m\times \mathbb{R}^n$，$G(x,y)=(x,F(x,y))$，且 $G(x_0,y_0)=(x_0,0)$。求出 $G$ 的 Jacobi 矩阵：

$$
J_G(x,y)=\begin{bmatrix}
I_m & O \\ J_{F_x(x,y)} & J_{F_y(x,y)}
\end{bmatrix}
$$

这是一个上三角矩阵，$|J_G(x,y)|=|J_{F_y}(x,y)|$，由于 $J_{F_y}(x_0,y_0)$ 可逆，所以 $J_G(x_0,y_0)$ 也可逆。根据逆映射定理，我们可以找到 $(x_0,y_0)$ 的一个邻域 $U$，设 $V=G(U)$，则 $G|_U:U\to V$ 是 $C^1$-微分同胚。

对于 $(x,0)\in V$，我们可以找到 $U$ 中唯一的 $(x,y)$ 与其对应。即 $G^{-1}(x,0)=(x,y)$，即 $F(x,y)=0$。

设 $\sec(x,y)=y$，表示取数对的第二个数。我们可以找到 $x_0$ 的邻域 $U_1$，使得 $(U_1,0)\subset V$。设 $V’=(U_1,0)$，$U’=G^{-1}(V’)$，则 $G|_{U’}:U’\to V’$ 是 $C^1$-微分同胚，且对于任意 $x\in U_1$，总能找到唯一的 $y$ 使得 $(x,y)\in U’$，$F(x,y)=0$。设

$$
\begin{aligned}
& f:U_1 \to \mathbb{R}^n\\
& f(x)=\sec(G^{-1}(x,0))
\end{aligned}
$$

根据 $G^{-1}$ 的连续性可知 $f$ 也连续。考虑求导：（设 $\text{upd}(x)=(x,0)$）

$$
\begin{aligned}
J_f(x) &=J_{\sec}(G^{-1}(x,0))\times J_{G^{-1}}(x,0)\times J_{\text{upd}}(x)\\
&=J_{\sec}(x,f(x))\times J_G(x,f(x))^{-1}\times J_{\text{upd}}(x)\\
&=\begin{bmatrix} O & I_n \end{bmatrix}\times 
\begin{bmatrix} I_m & O \\J_{F_x}(x,f(x)) & J_{F_y}(x,f(x))\end{bmatrix}^{-1}\times \begin{bmatrix} I_m \\ O \end{bmatrix}\\
&=\begin{bmatrix} O & I_n \end{bmatrix}\times 
\begin{bmatrix} I_m & O \\-J_{F_y}(x,f(x))^{-1}J_{F_x}(x,f(x)) & J_{F_y}(x,f(x))^{-1}\end{bmatrix}\times \begin{bmatrix} I_m \\ O \end{bmatrix}\\
&=-J_{F_y}(x,f(x))^{-1}J_{F_x}(x,f(x))
\end{aligned}
$$

证毕。

隐函数定理是解方程理论的基础：如果要从方程 $F(x,y)=0$ 解出 $y=f(x)$，且 $f$ 存在、唯一、光滑，我们就得用隐函数定理。

> 其实我们看看上面的思路中得到的线性代数版本的答案：$f=\begin{bmatrix}O & I_n\end{bmatrix}\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}^{-1}\begin{bmatrix}I_m \\ O\end{bmatrix}$，这和我们在最后得到的一般函数的答案：$f(x)=\sec(G^{-1}(x,0))$ 是完全吻合的：$\sec$ 就是 $\begin{bmatrix}O & I_n\end{bmatrix}$，$G^{-1}$ 就是 $\begin{bmatrix}I_m & O \\ X & Y \end{bmatrix}^{-1}$，$\text{upd}$ 就是 $\begin{bmatrix}I_m \\ O\end{bmatrix}$。
> 
> 这告诉了我们一个深刻的道理：隐函数定理的证明，本质上就是把线性情形的“解方程组”步骤，逐字逐句地翻译成非线性语言，然后每一步用逆映射定理来保证“非线性版本的可逆性”存在。对于其它的定理，我们也可以先思考它的线性代数版本，再把过程翻译成非线性的微分语言进行证明。

## 秩定理

接下来我们通过探究线性映射中秩的性质，通过微分的方式将其拓展到非线性函数。

我们知道：一个线性映射像的维数=矩阵的秩，而一个非线性映射 $f$ 的局部行为可以由它的 Jacobi 矩阵 $J_f(x_0)$ 近似刻画。

对于任意 $n$ 阶方阵 $A$，如果 $\operatorname{rank}(A)=k$，则其存在相抵标准型：$A=P\begin{bmatrix} I_k & O \\ O & O\end{bmatrix} Q^{-1}$，其中 $P,Q$ 可逆。

其几何意义是：选取两组线性无关的基 $\{e_{1\cdots n}\}$，$\{f_{1\cdots n}\}$，$f$ 可以写成如下的线性变换：$f(e_i)=f_i$（$i\le k$），$f(e_j)=0$（$j>k$）。而 $P,Q$ 就是标准基向 $e,f$ 这两组基的过渡矩阵。

我们希望对于连续可微函数 $f:\mathbb{R}^n\to\mathbb{R}^m$，如果它在定义域上每一点 $x$ 都有 $\operatorname{rank}{J_f(x_0)}=k$，那么对于任意 $x_0$，存在 $x_0$ 的邻域 $X$ 和 $f(x_0)=y_0$ 的邻域 $Y$，可以通过 $C^1$-微分同胚（即“可逆的坐标变换函数”）$\psi:Y\to V$ 和 $\varphi:X\to U$，

使得 $\psi\circ f\circ \varphi^{-1}:U\to V$ 有表示：

$$
\psi\circ f\circ \varphi^{-1} (x^1,x^2,\cdots,x^n)=(x^1,x^2,\cdots,x^k,0,0,\cdots,0)
$$

我们把它称之为 **秩定理**。在证明之前，我们先做一些准备工作，考虑一些特殊情况：

**（秩定理：行满秩情况）设 $D$ 为 $x_0\in\mathbb{R}^{m+n}$ 的一个邻域，$f\in C^1(D,\mathbb{R}^m)$。若 $J_f(x_0)$ 行满秩，前 $m$ 列可逆，则存在 $x_0$ 的邻域 $U\subset D$ 和微分同胚 $\varphi:U\to V\subset \mathbb{R}^{m+n}$ 使得映射 $f\circ\varphi^{-1}:V\to \mathbb{R}^m$ 有表示：**

$$
f\circ\varphi^{-1}(x^1,x^2,\cdots,x^{n+m})=(x^1,x^2,\cdots,x^m,0,0,\cdots,0)
$$

> 可以类比：对于行满秩矩阵 $A_{m\times (m+n)}$，存在可逆列变换 $Q$ 使得 $AQ^{-1}=\begin{bmatrix} I_m & 0 \end{bmatrix}$。
> 
> 此时 $A=\begin{bmatrix} I_m & 0 \end{bmatrix}Q$，即 $Q$ 的前 $m$ 行为 $A$。为了让 $Q$ 可逆，我们让 $Q_{i,i}=1$（$i>m$），这样就会变成可以可逆上三角阵。这样我们就构造出了一个合法的 $Q$。对于一般函数我们也类似去做：
>
> 假设对于 $x\in \mathbb{R}^{m+n}$ 有 $x=x_1\times x_2$（$\times$ 为笛卡尔积），$x_1\in\mathbb{R}^m$，$x_2\in\mathbb{R}^n$。
> 
> 我们设 $\varphi^{-1}(x_1,x_2)=(z_1,z_2)$，由题有 $f(z_1,z_2)=x_1$，可以推导出 $\varphi(z_1,z_2)=(x_1,x_2)=(f(z_1,z_2),x_2)$。类比于上面的线性变换情况，我们如果要让 $\varphi$ 可逆，只需令 $z_2=x_2$ 即可。

证明：定义映射 $\varphi:\mathbb{R}^m\times \mathbb{R}^n\to \mathbb{R}^m\times \mathbb{R}^n$，有 $\varphi(x_1,x_2)=(f(x_1,x_2),x_2)$，由题可知 $J_\varphi(x)$ 在 $x_0$ 附近可逆。根据逆映射定理，存在 $x_0$ 的邻域 $U$ 使得 $\varphi|_U:U\to V\ (V=f(U))$ 是微分同胚。

设 $x=(x_1,x_2)\in V$，$\varphi^{-1}(x_1,x_2)=(y_1,y_2)$，由定义有 $x_1=f(y_1,y_2),x_2=y_2$。则 $f(y_1,y_2)=x_1$，即 $f\circ\varphi^{-1}(x_1,x_2)=x_1$，证毕。

**（秩定理：列满秩情况）设 $D$ 为 $x_0\in \mathbb{R}^n$，$f\in C^1(D,\mathbb{R}^{n+m})$。若 $J_f(x_0)$ 列满秩，且前 $n$ 行可逆，则存在 $x_0$ 的邻域 $U\subset D$ 和 $y_0=f(x_0)$ 的邻域 $W$，$0\in \mathbb{R}^m$ 的邻域 $V$，以及微分同胚 $\psi: W\to U\times V$，使得映射 $\psi\circ f: U\to U\times V$ 有表示：**

$$
\psi\circ f(x^1,x^2,\cdots,x^n)=(x^1,x^2,\cdots,x^n,0,0,\cdots,0)
$$

> 可以类比：对于列满秩矩阵 $A_{(n+m)\times n}$，存在可逆行变换 $P$ 使得 $PA=\begin{bmatrix}I_n \\ O\end{bmatrix}$。类似地，我们有 $A=P^{-1}\begin{bmatrix}I_n \\ O\end{bmatrix}$，即 $P^{-1}$ 的前 $n$ 列是 $A$。为了让 $P^{-1}$ 可逆，只需要让 $P^{-1}_{i,i}=1\ (i>n)$ 即可。对于一般函数，使用类似的做法即可。
> 
> 两种情况在一般函数的证法都是类似的，只需要构造 $\varphi,\psi^{-1}$ 使得它的 Jacobi 矩阵与 $Q$ 或 $P^{-1}$ 形式相同，再利用逆映射定理即可。

我们设 $\psi^{-1}(x_1,x_2)=f(x_1)+(0,x_2)$，由题可知 $\psi^{-1}(x_1,x_2)$ 在 $(x_1,0)$ 附近可逆。存在 $(x_0,0)$ 的邻域 $U\times V$，使得 $\psi^{-1}|_{U\times V}: (U\times V)\to W\ (W=f(U\times V))$ 是微分同胚。

因为 $\psi^{-1}(x_0,0)=f(x_0)$，所以 $\psi\circ f(x_0)=(x_0,0)$，证毕。

最后我们回到秩定理的证明：

**（秩定理）对于连续可微函数 $f:\mathbb{R}^n\to\mathbb{R}^m$，如果它在定义域上每一点 $x$ 都有 $\operatorname{rank}{J_f(x_0)}=k$，那么对于任意 $x_0$，存在 $x_0$ 的邻域 $X$ 和 $f(x_0)=y_0$ 的邻域 $Y$，可以通过 $C^1$-微分同胚 $\psi:Y\to V$ 和 $\varphi:X\to U$，使得 $\psi\circ f\circ \varphi^{-1}:U\to V$ 有表示：**

$$
\psi\circ f\circ \varphi^{-1} (x^1,x^2,\cdots,x^n)=(x^1,x^2,\cdots,x^k,0,0,\cdots,0)
$$

> 根据相抵标准型理论，对于 $m\times n$ 的矩阵 $A$，若 $\operatorname{rank}(A)=k$，则存在可逆阵 $P,Q$ 使得 $PAQ^{-1}=\begin{bmatrix}I_k & O \\ O & O \end{bmatrix}$，即
> $A=P^{-1}\begin{bmatrix}I_k & O \\ O & O \end{bmatrix}Q=P^{-1}\begin{bmatrix} I_k \\ O \end{bmatrix}\times \begin{bmatrix} I_k & O \end{bmatrix} Q=P_1^{-1}\times Q_1$
> 
> 其中 $P_1^{-1}$ 是 $P$ 的前 $k$ 列，$Q_1$ 是 $Q$ 的前 $k$ 行。假定 $A$ 的前 $k$ 行和前 $k$ 列形成的子矩阵可逆，那我们就令 $Q$ 的前 $k$ 行是 $A$ 的前 $k$ 行，$Q_{i,i}=1\ (i>k)$ 保证可逆。此时 $P_1$ 唯一确定且 $P_1$ 的前 $k$ 行是单位阵，然后再令 $P_{i,i}=1\ (i>k)$ 保证可逆即可。
> 
> 对于一般情况，我们只需要让 $\varphi,\psi^{-1}$ 的 Jacobi 矩阵与 $Q,P^{-1}$ 的形式一样即可。

证明：不妨令 $J_f(x_0)$ 前 $k$ 行和前 $k$ 列形成的子矩阵可逆。令 $\varphi(x^1,x^2,\cdots,x^n)=(f^1(x),f^2(x),\cdots,f^k(x),x^{k+1},x^{k+2},\cdots,x^n)$，则 $\varphi(x_0)$ 可逆。因此存在 $x_0$ 的邻域 $X$，$\varphi|_X:X\to U\ (U=\varphi(x))$ 是微分同胚。

设 $u=(u^1,u^2,\cdots,u^n)\in U$，设 $\varphi^{-1}(u)=x=(x^1,x^2,\cdots,x^n)$，则有 $u^i=f^i(x)\ (i\le k)$，$u^j=x^j\ (j>k)$。此时 $f\circ\varphi^{-1}(u)=f(x)=(u^1,u^2,\cdots,u^k,f^{k+1}(x),\cdots,f^m(x))$。设 $f^i(x)=f^i(\varphi^{-1}(u))=h^i(u)$，则 $f\circ\varphi^{-1}(u)=(u^1,u^2,\cdots,u^k,h^{k+1}(u),\cdots,h^m(u))$。

注意到 $J_{f\circ \varphi^{-1}}(u)=J_f(x)\times J_{\varphi^{-1}}(u)$，由于 $J_{\varphi^{-1}}(u)$ 可逆，所以 $\operatorname{rank}(J_{f\circ\varphi^{-1}}(u))=\operatorname{rank}(J_f(x))=k$。而 $J_{f\circ\varphi^{-1}}(u)=\begin{bmatrix}I_k & O \\ (\dfrac{\partial h^{k+i}}{\partial u^{i}})(u) & (\dfrac{\partial h^{k+i}}{\partial u^{k+i}})(u)\end{bmatrix}$。

根据秩为 $k$ 的性质，$(\dfrac{\partial h^{k+i}}{\partial u^{k+i}})(u)=O$。这意味着 $h^{k+i}(u)$ 与 $u^{k+1\cdots n}$ 无关，即 $h^{k+i}(u)$ 是 $u^{1\cdots k}$ 的函数，设为 $g^{k+i}(u^1,u^2,\cdots,u^k)$。

综上，我们有 $f\circ \varphi^{-1}(u)=(u^1,u^2,\cdots,u^k,g^{k+1}(u^{1\cdots k}),g^{k+2}(u^{1\cdots k}),\cdots,g^m(u^{1\cdots k}))$。

再设 $\psi^{-1}(u)=(u^1,u^2,\cdots,u^k,g^{k+1}(u^{1\cdots k})+u^{k+1},g^{k+2}(u^{1\cdots k})+u^{k+2},\cdots,g^m(u^{1\cdots k})+u^m)$。则 $J_{\psi^{-1}}(u)$ 是对角线均为 1 的下三角阵，必定可逆。令 $\varphi(x_0)=u_0$，则 $\psi^{-1}(u_0^1,u_0^2,\cdots,u_0^k,0,0,\cdots,0)=f\circ\varphi^{-1}(u_0)=f(x_0)=y_0$，所以必存在 $(u_0^1,u_0^2,\cdots,u_0^k,0,0,\cdots,0)$ 的邻域 $V$ 和 $y_0$ 的邻域 $Y$ 使得 $\psi^{-1}|_V:V\to Y$ 是微分同胚。

此时 $\psi\circ f\circ \varphi^{-1}(u)=\psi(u^1,u^2,\cdots,u^k,g^{k+1}(u^{1\cdots k}),g^{k+2}(u^{1\cdots k}),\cdots,g^m(u^{1\cdots k}))=(u^1,u^2,\cdots,u^k,0,0,\cdots,0)$。

证毕。

## 条件极值

现在我们回到多元函数的视角。由于值域只有一维，我们可以暂时放下微分“线性拟合”的概念，转而用更传统的分析方法和分析视角来进行研究。

这一节我们将讨论限制在区域 $D\in\mathbb{R}^n$ 的连续可微函数 $f$ 在 $m$ 个条件 $\varphi^{1\cdots m}(x)=0$ 情况下的极值。

不过在此之前，我们先做一点有趣的引入：

考虑物理意义。我们设 $f(x)$ 表示粒子在 $x$ 处的动能。而 $\operatorname{grad} f(x)$ 则表示 $x$ 这一点处的力（包括大小和方向）。而通过微分导出的切线公式 $f(x_0+t)-f(x_0)=t\cdot \operatorname{grad} f(x_0)$ 就是动能定理。

对于任意一条经过 $x_0$ 的曲线 $\gamma(x):[-1,1]\to D$，其中 $\gamma(0)=x_0$，$\gamma’(t)\not=0$，如果 $x_0$ 是粒子经过这一条曲线中动能极值所在的点，那么这一点处的功率一定为零，即 $\operatorname{grad} f(x_0)\cdot \gamma’(0)=0$。

回到正题，我们以 $n=3$，$m=1$ 为例来进行说明。

假设 $\varphi(x)\in C^1(D)$，$\varphi(x_0)=0$，$\operatorname{grad} \varphi(x)\not=0\ (\forall x\in D)$。

不妨令 $\dfrac{\partial \varphi}{\partial x^3}\not=0$，根据隐函数定理，存在 $(x_0^1,x_0^2)$ 的一个邻域 $X’\subset \mathbb{R}^2$，对于 $(x^1,x^2)\in X’$，存在恰好唯一的一个 $x^3=h(x^1,x^2)$ 使得 $\varphi(x^1,x^2,x^3)=0$。

令 $X=X’\times h(X’)$，这是包含 $x_0$ 的一个联通开邻域。再设 $S=\{x\in X\mid \varphi(x)=0\}$，它构成了 $\mathbb{R}^3$ 中的一张二维曲面。由于对于每个 $(x^1,x^2)$ 只有恰好一个 $x^3$ 符合要求，它也可以等同于 $\mathbb{R}^2$ 中的某个区域。

对于任意一条经过 $x_0$ 的曲线 $\gamma(x):[-1,1]\to X$，其中 $\gamma(0)=x_0$，$\gamma’(t)\not=0$，都可以按照如下方式表示：$\gamma(t)=(x^1(t),x^2(t),h(x^1(t),x^2(t)))$。

$\gamma(t)$ 在 $x_0$ 处的切向量可以表示为：

$$
\gamma’(0)=\begin{bmatrix}(x^1)’(0)\\ (x^2)’(0) \\ \dfrac{\partial h}{\partial x^1}(x_0^1,x_0^2)(x^1)’(0)+\dfrac{\partial h}{\partial x^2}(x_0^1,x_0^2)(x^2)’(0)\end{bmatrix}=(x^1)’(0)\vec{v_1}+(x^2)’(0)\vec{v_2}
$$

其中 $\vec{v_1},\vec{v_2}$ 在 $x_0$ 处是固定且线性无关的。当 $\gamma(t)$ 不同时，变化的只有 $(x^1)’(0)$ 和 $(x^2)’(0)$。因此 $v_1,v_2$ 在 $x_0$ 这一点张成出了一个平面，我们称之为 $S$ 在 $x_0$ 处的切平面。

上文中我们提到了 $\operatorname{grad} f(x_0)\cdot \gamma’(0)=0$，这意味着如果 $x_0$ 是 $S$ 中的极值点，那么 $\operatorname{grad} f(x_0)$ 垂直于切平面。现在我们来严格证明一下：根据复合函数链式求导法则，$f(\gamma(0))’=f’(\gamma(0))\times \gamma’(0)=\operatorname{grad} f(x_0)\cdot \gamma’(0)=0$（第一个 $\times$ 是矩阵乘法，第二个 $\cdot$ 是点积）

还有哪些向量垂直于切平面？注意到 $\varphi(x)$ 自己就是个函数，而 $\operatorname{grad}\varphi(x)$ 表示函数沿着这个方向移动最快。我们还是把 $\varphi(x)$ 想象成另一个动能函数，那么 $\operatorname{grad}\varphi(x)$ 就是力的方向，根据动能定理（切线公式） $\varphi(x_0+t)=\varphi(x_0)+\operatorname{grad}\varphi(x_0)\cdot t$。我们如果想要让 $\varphi(x_0+t)$ 等于零，那么就必须不做功，速度方向 $t$ 需要垂直于力的方向 $\operatorname{grad} \varphi(x_0)$。对应到曲线 $\gamma(t)$ 上，也就是 $\operatorname{grad}\varphi(x_0)\cdot \gamma’(0)=0$。

严谨证明一下：$\varphi(\gamma(t))\equiv 0$，所以 $\varphi(\gamma(0))’=\operatorname{grad}\varphi(x_0)\cdot \gamma’(0)=0$。

由于切平面是二维，总的空间维度是三维，这意味着法空间只能是一维。既然 $\operatorname{grad} \varphi(x_0)$，$\operatorname{grad} f(x_0)$ 都在法空间，这意味着它们线性相关，也就是说存在唯一的 $\lambda$ 使得 $\operatorname{grad} f(x_0)+\lambda\operatorname{grad}\varphi(x_0)=0$。

现在我们尝试推广到 $n,m$ 更高的情况。对于 $\varphi(x)=(\varphi^1(x),\cdots,\varphi^m(x))$，假设 $\varphi(x_0)=0$，$\operatorname{rank}(J_\varphi(x))=m$。（即所有条件互不相关，$\operatorname{grad}\varphi^1,\operatorname{grad}\varphi^2,\cdots,\operatorname{grad}\varphi^m$ 线性无关）

不妨假设 $J_{\varphi}(x_0)$ 的后 $m$ 列线性无关，根据隐函数定理，可以找到包含 $x_0$ 的联通开邻域 $X$，使得 $S=\{\varphi(x)=0\mid x\in X\}$ 构成一个 $n-m$ 维曲面，并由前 $n-m$ 维 $x^{1\cdots n-m}$ 唯一控制。也就是说，可以构造函数：$x^{n-m+i}=h^i(x^1,x^2,\cdots,x^{n-m})$。

按照同样方式定义曲线 $\gamma(t)=(x^1(t),\cdots,x^{n-m}(t),h^1(x^{1\cdots n-m}(t)),\cdots,h^m(x^{1\cdots n-m}(t)))$。可以求得

$$
\gamma’(0)=\begin{bmatrix}
(x^1)’(0)\\
(x^2)’(0)\\
\vdots \\
(x^{n-m})’(0) \\
\sum_{i=1}^{n-m}\dfrac{\partial h^1}{\partial x^i}(x_0^{1\cdots n-m})(x^i)’(0)\\
\sum_{i=1}^{n-m}\dfrac{\partial h^2}{\partial x^i}(x_0^{1\cdots n-m})(x^i)’(0)\\
\vdots \\
\sum_{i=1}^{n-m}\dfrac{\partial h^m}{\partial x^i}(x_0^{1\cdots n-m})(x^i)’(0)\\
\end{bmatrix}=\sum_{i=1}^{n-m}(x^i)’(0)\vec{v_i}
$$

$S$ 在 $x_0$ 处的切空间由 $\vec{v}_{1\cdots n-m}$ 这 $n-m$ 个线性无关的向量所张成，共 $n-m$ 维。根据之前的证明，$\operatorname{grad}\varphi^i(x_0)\cdot \gamma’(0)=0$，这 $m$ 个线性无关的向量构成了 $x_0$ 处的法空间，共 $m$ 维。同理有 $\operatorname{grad} f(x_0)=0$，它也在法空间内，因此它可以由 $\operatorname{grad}\varphi^i(x_0)$ 线性组合而成。也就是说，存在一组唯一的实数 $\lambda_0^{1\cdots m}$，使得：

$$
\operatorname{grad} f(x_0)+\sum_{i=1}^m\lambda_0^i\operatorname{grad} \varphi^i(x_0)=0
$$

我们就找到了 $x_0$ 是 $f$ 在 $\varphi^{1\cdots m}$ 这些条件下的极值的必要条件。

现在的问题是：怎么快速找到符合条件的 $x_0$？梳理一下需要的条件：首先有 $\varphi^i(x_0)=0$，其次是上面的条件。怎么样能够把它们一网打尽？

设 $F(x,\lambda^{1\cdots m}):\mathbb{R}^n\times \mathbb{R}^m\to \mathbb{R}$，有：

$$
F(x,\lambda^{1\cdots m})=f(x)+\sum_{i=1}^m\lambda^i\varphi^i(x)
$$

对 $F$ 求偏导：

$$
\begin{aligned}
\dfrac{\partial F}{\partial x^i}(x_0,\lambda_0) &=\dfrac{\partial f}{\partial x^i}(x_0)+\sum_{i=1}^m\lambda_0^i \dfrac{\partial \varphi^i}{\partial x^i}(x_0)\\
\dfrac{\partial F}{\partial \lambda^i}(x_0,\lambda_0)&=\varphi^i(x_0)
\end{aligned}
$$

注意到对 $x$ 求偏导等于零构成了 $\operatorname{grad} f(x_0)+\sum_{i=1}^m\lambda_0^i\operatorname{grad} \varphi^i(x_0)=0$ 的方程，对 $\lambda^i$ 求偏导等于零构成了 $\varphi^i(x_0)=0$ 的方程。

也就是说，如果我们对 $F$ 求偏导，得出所有的偏导均为零，我们就能找到合法的 $x_0$（当然还有对应的 $\lambda_0$）。上述求出条件极值的方法称作 **Lagrange 乘子法**。

但是这只是必要条件。对于驻点（可能不是极值点）来说，它也可能满足所有的方程。如果判断 $x_0$ 是否是真正的极值点？

一个经典的错误是直接求 $f(x)$ 在 $x_0$ 处的 Hessian 矩阵，然后看其限制在切空间方向是否是正定（或负定）的。这样做有什么问题？

事实上，这样做只能判断在切空间这个截面上 $f(x)$ 是极值。但真正的曲面绝不可能是严格按照切空间的截面在走，沿曲面移动时，位移不是纯切向量。也就是说，$x_0$ 到曲面上近旁的另一个点 $y_0$ 的位移中会不可避免的混入法方向的向量，所以这样做是有问题的。

那怎么办？下面的定理给出了一个方法：

**（条件极值的充分条件）若 $F(x,\lambda_0)$ 在 $x_0$ 处的 Hessian 二次型对于任意切空间中的 $v$ 均正定（或负定），则 $x_0$ 是条件极值点。如果是不定的，则不是条件极值点。**

> 如果我们要使用 Hessian 二次型，我们就需要想办法把条件极值变为一般的函数极值。我们之前提到过，根据隐函数定理，在 $x_0$ 的近旁形成的是一个 $k=n-m$ 维的曲面，且可以由 $k$ 个维度直接控制。假设由前 $k$ 维控制，那么我们可以令 $\Phi(u^{1\cdots k})=(u,h(u))$，其中 $h:\mathbb{R}^k\to \mathbb{R}^{n-k}$ 由隐函数定理唯一给出。令 $x_0=\Phi(u_0)$，我们只需要证明 $u_0$ 是 $\psi(u)=F(\Phi(u))$ 的一般极值点即可。（$\lambda_0$ 是定值所以省略）
> 
> 对于一阶导，注意到 $J_{\psi}(u_0)=J_F(x_0)\times J_\Phi(u_0)=O$，所以可以利用 Hessian 二次型判别极值。

证明：由 Taylor 公式可知，当 $h\to 0$ 时：

$$
\begin{aligned}
\psi(u_0+h)-\psi(u_0)&=\dfrac{1}{2}\sum_{i,j=1}^k\dfrac{\partial^2\psi}{\partial u^i\partial u^j}(x_0)h^ih^j+o(h^2)
\end{aligned}
$$

问题来了：怎么求二阶导？

先讲解一下记号：设 $\partial_iF=\dfrac{\partial F}{\partial x^i}$，$\partial _i\Phi^j=\dfrac{\partial \Phi^j}{\partial u^i}$。

先求一阶导：

$$
\dfrac{\partial \psi}{\partial u^\alpha}(u)=\sum_{i=1}^n \partial_i F(\Phi(u))\partial_\alpha \Phi^i(u)
$$

然后推式子：

$$
\begin{aligned}
\dfrac{\partial \psi}{\partial u^\alpha \partial u^\beta}(u)&=\dfrac{\partial}{\partial u^\beta}(\sum_{i=1}^n \partial_i F(\Phi(u))\partial_\alpha \Phi^i(u))\\
&= \sum_{i=1}^n\dfrac{\partial}{\partial u^\beta}(\partial_i F(\Phi(u))\partial_\alpha \Phi^i(u))\\
&= \sum_{i=1}^n \partial_i F(\Phi(u))\dfrac{\partial}{\partial u^\beta} (\partial_\alpha\Phi^i(u))+\partial_\alpha\Phi^i(u)\dfrac{\partial}{\partial u^\beta}(\partial_i F(\Phi(u)))
\end{aligned}
$$

先处理第一项：

$$
\begin{aligned}
& \sum_{i=1}^n \partial_i F(\Phi(u))\dfrac{\partial}{\partial u^\beta} (\partial_\alpha\Phi^i(u))\\
= & \sum_{i=1}^n \partial_i F(\Phi(u))\dfrac{\partial^2\Phi^i}{\partial u^\alpha\partial u^\beta}(u)
\end{aligned}
$$

当 $u=u_0$ 时，$\partial_i F(\Phi(u))=\partial_iF(x_0)=0$，所以这一项可以忽略。

再处理第二项：

$$
\begin{aligned}
& \dfrac{\partial}{\partial u^\beta}(\partial_i F(\Phi(u))) \\
= & \sum_{j=1}^n \dfrac{\partial^2 F}{\partial x^i\partial x^j}(\Phi(u))\partial_\beta\Phi^j(u)\\
& \sum_{i=1}^n \partial_\alpha\Phi^i(u)\dfrac{\partial}{\partial u^\beta}(\partial_i F(\Phi(u)))\\
=& \sum_{i=1}^n\partial_\alpha\Phi^i(u)(\sum_{j=1}^n \dfrac{\partial^2 F}{\partial x^i\partial x^j}(\Phi(u))\partial_\beta\Phi^j(u))\\
=& \sum_{i,j=1}^n\partial_\alpha\Phi^i(u)\times \partial_\beta\Phi^j(u)\times \dfrac{\partial^2 F}{\partial x^i\partial x^j}(\Phi(u))
\end{aligned}
$$

带入 $u=u_0$，就可以求出二阶导：

$$
\begin{aligned}
 \psi’’(u_0)&=(\sum_{i,j=1}^n\partial_\alpha\Phi^i(u_0)\times \partial_\beta\Phi^j(u_0)\times \dfrac{\partial^2 F}{\partial x^i\partial x^j}(x_0))_{\alpha,\beta=1}^n \\
&= \Phi’(u_0)^T\times H_F(x_0)\times \Phi’(u_0)
\end{aligned}
$$

而 $\Phi’(u_0)=\begin{bmatrix}I_k \\ h’(u_0)\end{bmatrix}=\begin{bmatrix} \vec{v_1} & \vec{v_2} &\cdots & \vec{v_k}\end{bmatrix}$。对于任意 $h\in\mathbb{R}^k$，都有 $\Phi’(u_0)h$ 是切空间中的向量。

这正是我们想要看到的：切空间中的向量，$F$ 中的 Hessian 二次型。证毕。

## 从一重积分到多重积分

先做一些符号说明：设 $I_{a,b}=\{x\mid a^i\le x^i\le b^i,i=1,2,\cdots,n\}$ 为 $\mathbb{R}^n$ 中的闭区间（长方体）。$\mu(I)=\prod_{i=1}^n b_i-a_i$ 表示它的体积。

我们先来考虑闭区间上的积分。还是一样的，我们对于每一维构造一个分点序列 $x_0^i=a^i<x_1^i<x_2^i<\cdots<x_k^i=b^i$，那么整个长方体 $I_{a,b}$ 就可以分成若干个小块 $I_{p_{1\cdots n}}=\{x\mid x^i_{p_i}\le x\le x^i_{p_{i+1}},\ i=1,2,\cdots,n \}$。当切的小块足够细时，每个小块内 $f$ 的值近似相等，所以我们求出 $\sum_{p_{1\cdots n}} f(I_p)\mu(I_p)$ 就可以作为 $f$ 在 $I$ 上的积分 $\int_I f(x)\mathrm{d} x$。

当我们需要积分的区域不是规整的长方体（即闭区间）时，我们也可以进行积分。对于有界集合 $E$，设 $\chi_E(x)=\begin{cases} 1, & x\in E\\ 0, & x\not\in E\end{cases}$ 作为其示性函数。若 $I$ 是闭区间，且 $E\subset I$，利用示性函数我们可以把有界集合上的积分变成闭区间上的积分：

$$
\int_E f(x) \mathrm{d} x=\int_I f(\chi_E(x))\mathrm{d} x
$$

我们将有界集合 $E$ 上的可积函数构成的集合记为 $\mathcal{R}(E)$。问题来了，什么样的函数可积？（这里的可积均指 Riemann 可积）

回到一重积分，我们有 Lebesgue 定理：若 $f(x)$ 在有界闭区间 $[L,R]$ 中的不连续点为零测集，则 $f(x)$ 在该区间可积。再回顾零测集的定义：对于任意 $\epsilon>0$，总存在该集合的，由至多可数个开区间组成的开覆盖 $\bigcup_{i=1}^{\infty}(a_i,b_i)$，且 $\sum_{i=1}^{\infty} b_i-a_i<\epsilon$。

推广到高维情形，就是：若 $f(x)$ 在有界闭区间 $I$ 中的不连续点为零测集，则 $f(x)$ 在该区间可积。这里的零测集定义变为：对于任意 $\epsilon>0$，总存在该集合的，由至多可数个开长方体组成的开覆盖 $\bigcup_{i=1}^{\infty}I’_{i}$，且 $\sum_{i=1}^{\infty} \mu(I’_i)<\epsilon$。（这里不仅是开长方体还是闭长方体均等价，$I’$ 表示该长方体为开长方体）

现在我们来考虑有界集合 $E$ 上的的积分。我们希望这个集合有比较好的性质——至少它的示性函数 $\chi_E(x)$ 可积。要不然，$E$ 上的绝大多数函数是没法积分的。对于示性函数 $\chi_E(x)$，它的不连续点就是集合 $E$ 的边界点。如果边界点是零测集，那么 $\chi_E(x)$ 就是可积的。接下来我们定义：

**（Jordan 可测）设 $E\subset \mathbb{R}^n$ 为一有界集合，如果 $E$ 上的常值函数 $f\equiv 1$ 在 $E$ 上可积，则称 $E$ 是 Jordan 可测的，并且记 $\mu(E)=\int_E 1\mathrm{d} x$ 为 $E$ 的 Jordan 测度。特别的，如果 $\mu(E)=0$，则称 $E$ 为 Jordan 零测集。**

我们发现 Jordan 测度的定义和体积是相容的。换句话说，一个集合的 Jordan 测度就是它的“体积”。

现在我们可以把有界闭区间上的可积性理论推广到 Jordan 可测集：如果 $E$ 为 Jordan 可测集，$f:E\to \mathbb{R}$，$f$ 可积的充要条件是它在 $E$ 上有界且不连续点为零测集。

## 变量代换公式

我们先看看一重积分里面的变量代换公式：（假设 $\varphi’(t)\ge 0$ 对 $\forall t\in[a,b]$ 均成立）

$$
\int_{\varphi(a)}^{\varphi(b)} f(x)\mathrm{d} x=\int_a^b f(\varphi(t))\varphi’(t)  \mathrm{d} t
$$

先忽略复合函数的链式求导法则，直接从几何直觉上理解这个公式。对于 $[a,b]$ 这个区间，我们把它分成若干个小部分 $[t_i,t_{i+1}]$，每个小部分的 $f\circ \varphi$ 值近似相同，我们设这个近似相同的值为 $f_i=f(\varphi(t_i))$。

在 $t_i$ 的近旁，$\varphi(t)$ 可以近似于一个线性变换。它把 $[t_{i},t_{i+1}]$ 映射到 $[\varphi(t_i),\varphi(t_{i+1})]$，且这个线性变换对于区间长度的扩大倍数为 $\det J_\varphi(t_i)=\varphi’(t_i)$。又因为 $\varphi$ 单调递增，所以 $[\varphi(t_i),\varphi(t_{i+1})]$ 这些区间可以刚好拼成 $[\varphi(a),\varphi(b)]$ 这个大区间且不重叠。

$$
\int_{\varphi(a)}^{\varphi(b)}f(x)\mathrm{d} x=\lim_{||\pi||\to 0} \sum_i f_i(\varphi(t_{i+1})-\varphi(t_i))=\lim_{||\pi||\to 0}\sum_i f_i(t_{i+1}-t_i)\varphi’(t_i)=\int_a^b f(\varphi(t))\mathrm{d} t
$$

然后我们将其推广到多重积分。设 $\varphi:D_t\to D_x$ 为 $\mathbb{R}^n$ 中有界开集之间的微分同胚，$f$ 为定义在 $D_x$ 上的函数，$\operatorname{supp} f$ 为 $D_x$ 的紧致子集。我们猜想：$f\in\mathcal{R}(D_x)$ 当且仅当 $f\circ\varphi\cdot|\det \varphi’|\in \mathcal{R}(D_t)$，并且如果 $f$ 可积则有如下的 **变量代换公式**：

$$
\int_{D_x} f(x) \mathrm{d} x=\int_{D_t} f\circ\varphi(t) \cdot |\det \varphi’(t) | \mathrm{d} t
$$

我们按照类似的方式理解：由于 $\varphi$ 是微分同胚，我们将 $D_t$ 划分为若干个小块 $D_i$，则 $\varphi(D_i)$ 可以不重不漏地拼合成 $D_x$。每个小块内 $f\circ \varphi$ 的值都大致相同，设这个值为 $f_i$。从 $D_i$ 变化成 $\varphi(D_i)$ 的过程类似于进行一次线性变换，变化的矩阵就是 $J_\varphi(x_i)\ (x_i\in D_i)$，而线性变换的体积缩放倍数就是它的行列式 $|\det J_\varphi(x_i)|$。所以我们有：

$$
\begin{aligned}
\int_{D_x} f(x) \mathrm{d} x &= \lim_{||\pi||\to 0}\mu(\varphi(D_i)) f_i \\
&= \lim_{||\pi ||\to 0}\mu(D_i) |\det J_\varphi(x_i)| f_i \\
&= \int_{D_t} f\circ \varphi(t) \cdot |\varphi'(t)| \mathrm{d} t
\end{aligned}
$$

有了直观理解，现在我们的问题是：如何证明？

在这里，我们的证明思路是：从简单到复杂，从线性到一般，从容许集到平凡集。

首先不管两边的积分结果如何，我们得保证两边的可积性是相同的。这需要我们对零测集进行讨论。

接着我们需要兵分两路：第一路需要证明 $\varphi$ 是线性映射的时候成立，第二路需要证明变量代换公式在 Jordan 可测集上成立。

然后我们把两路的结果综合起来，就得到了变量代换公式。

最后，正如一元微积分不需要保证变量代换时的 $\varphi$ 单调，对于多元微积分我们也可以证明其在退化情况下成立：不需要保证 $|\det \varphi(x)'|\not=0$，只需要保证 $\varphi$ 是连续可微的一一映射，变量代换公式仍然成立。

在证明之前，我们仍然需要做一些准备工作：

**（引理一）$\mathbb{R}^n$ 中的任意开集都可以表示为可数多个两两之间无公共内点的闭区间（可取为立方体）的并。**

证明：设 $S_0=\{I_{a,b} \mid a^i+1=b^i,\ a^i\in \mathbb{Z},\ i=1,2,\cdots, n\}$，即按照网格线把整个空间分为若干个 $1\times 1\times \cdots\times 1$ 的块。再设 $S_1=\{I_{a,b} \mid a^i+\dfrac{1}{2}=b^i,\ 2a^i\in \mathbb{Z},\ i=1,2,\cdots, n\}$，即把 $S_0$ 中的每一个块按照中心线划分为 $2^n$ 个小块后组成 $S_1$。同理，把 $S_1$ 中的每一个块按照中心线划分为 $2^n$ 个小块后组成 $S_2$，依此类推。我们有 $S_i=\{I_{a,b} \mid a^i+\dfrac{1}{2^i}=b^i,\ 2^ia^i\in \mathbb{Z},\ i=1,2,\cdots, n\}$。

由于 $S_i$ 是可数集，可数个可数集的并也是可数集，所以 $S=\bigcup_{i=1}^\infty S_i$ 可数。对于 $S$ 中的任意两个立方体，它们要么不交，要么包含。

由于 $D\subset \mathbb{R}^n$ 是开集，对于任意 $x\in D$，总能找到一个开球 $B(x,\delta)\subset D\ (\delta >0)$。而总有一个 $S$ 中的闭立方体在这个开球中。所以对于任意 $x$，我们都能找到一个 $S$ 中包含 $x$ 的一个闭立方体，且它被 $D$ 包含。我们把所有 $x$ 对应的闭立方体组成的集合（注意去重了）设为 $T$。然后，如果 $x\in T$ 存在 $y\in T$ 使得 $x\subset y$，我们就删去 $x$。这样形成的新集合 $T'$ 就满足：任意两个集合不交，且它们的并刚好是 $D$，且可数。证毕。

**（引理二）拟微分中值定理 - 切比雪夫版：设 $||x||_{\infty} :=\max_{1\le i\le n}|x^i|$，$||A||_\infty=\max_{i=1}^n \sum_{j=1}^n |A_{i,j}|$。再设 $D$ 为 $\mathbb{R}^n$ 中的区域，$f: D\to \mathbb{R}^m$，$x_1,x_2\in D$，$[x_1,x_2]\subset D$，$f$ 在 $[x_1,x_2]$ 连续，$(x_1,x_2)$ 可微，则 $||f(x_2)-f(x_1)||_\infty \le \sup_{t\in(x_1,x_2)} ||J_f(t)||_\infty\cdot ||x_2-x_1||_\infty$。**

证明：假设 $||f(x_2)-f(x_1)||_\infty$ 在第 $i$ 维取到最大值，即 $||f(x_2)-f(x_1)||_\infty=|f^i(x_2)-f^i(x_1)|$。根据拟微分中值定理，存在 $t\in(x_1,x_2)$ 使得 $f^i(x_2)-f^i(x_1)=\langle \operatorname{grad} f^i(t),x_2-x_1\rangle$。我们有：

$$
\begin{aligned}
|f^i(x_2)-f^i(x_1)| &=|\langle \operatorname{grad} f^i(t),x_2-x_1\rangle|\\
&\le \sum_{k=1}^n |\operatorname{grad} f^i(t)_k|\cdot |x_2^k-x_1^k| \\
&\le \sum_{k=1}^n |\operatorname{grad} f^i(t)_k|\cdot ||x_2-x_1||_\infty \\
&= ||J_{f^i}(t)||_\infty \cdot ||x_2-x_1||_\infty \\
||f(x_2)-f(x_1)||_\infty &\le ||J_f(t)||_\infty \cdot ||x_2-x_1||_\infty
\end{aligned}
$$

证毕。

## 变量代换公式的证明

- **第一步：对零测集进行讨论，保证两边可积性相同**

首先我们希望 $\chi_{D_x}(x)$ 和 $\chi_{D_t}(t)$ 的可积性相同（即设 $f\equiv1$ 为常值函数）。

**（定理一）记 $\psi=\varphi^{-1}:D_x\to D_t$，则 $E_x\subset D_x$ 为零测集当且仅当 $\psi(E_x)\subset D_t$ 为零测集。**

首先考虑必要性。根据引理一，任何一个开集都可以表示成可数多个闭立方体的并。我们设 $D_x=C_1+C_2+\cdots$ 为一组合法的构造。接下来我们枚举 $p$，在每个 $C_p$ 内部进行讨论。只要我们保证对于每个 $p$，$\psi(E_x\cap C_p)$ 都是零测集，由于可数多个零测集的并也是零测集，我们就可以证明了。接下来我们默认 $E_x:=E_x\cup C_p$。

又由于 $E_x$ 是零测集，所以对于任意 $\epsilon>0$，都存在可数多个立方体 $I=I_1,I_2,\cdots$ 使得 $E_x\subset \bigcup_{i=1}^\infty I_i$ 且 $\sum_{i=1}^\infty \mu(I_i)<\epsilon$。

于是我们得到了 $\psi(E_x)$ 的一个覆盖 $\psi(I)$。根据引理二，$||\psi(x)-\psi(x_0)||_\infty\le \sup_{t\in (x,x_0)} ||J_\psi(t)||_\infty \cdot ||x-x_0||_\infty$。由于 $C_p$ 紧致，$J_\psi(x)$ 连续，所以它在 $C_p$ 中存在最大值：设 $M=\max_{x\in C_p} ||J_\psi(x)||$。所以上面的公式可以改写成：$||\psi(x)-\psi(x_0)||_\infty\le M||x-x_0||_\infty$。

对于 $I_i$ 这个立方体，设 $x_0$ 为它的中心，则 $\forall x\in I_i$ 都有 $||\psi(x)-\psi(x_0)||_\infty \le M||x-x_0||_\infty$，这意味着如果把 $I_i$ 以 $x_0$ 为中心点，每条边长扩大到原来的 $M$ 倍变为 $I’_i$，然后将 $\varphi(x_0)$ 作为新的中心点，那么 $\varphi(x)$ 肯定在 $I’_i$ 内。所以 $\varphi(I_i)\subset I’_i$。

而 $\sum_{i=1}^\infty \mu(I’_i)=M^n\sum_{i=1}^\infty \mu(I_i)<M^n\epsilon$，故 $\varphi(E_x)$ 为零测集，证毕。

然后考虑充分性。注意到 $\varphi,\psi$ 互为逆函数，根据对称性，充分性也成立。

根据这个定理我们有一个简单的推论：$D_x$ 和 $D_t$ 要么同时为容许集，要么同时都不为容许集。

接下来我们再讨论 $f$ 为任意函数的情况。

**（定理二）$f\in \mathcal{R} (D_x)$ 当且仅当 $f\circ \varphi\cdot |\varphi’|\in \mathcal{R}(D_t)$。**

根据 $f$ 在上一节的设定，$\operatorname{supp} f\subset D_x$，$\varphi$ 是微分同胚，所以 $\operatorname{supp} f\circ\varphi \subset D_t$。这意味着 $f(\chi_{D_x}(x))$ 和 $f\circ \varphi(\chi_{D_t}(t))$ 分别在 $\partial D_x$ 和 $\partial D_t$ 没有不连续点。这意味着我们不需要考虑边界上的情况，可以安心的讨论 $D_x$ 和 $D_t$ 内部的情况。

根据定理一，$f$ 在 $D_x$ 上的不连续点为零测集，当且仅当 $f\circ\varphi$ 在 $D_t$ 上的不连续点为零测集。而 $\varphi$ 是微分同胚，这意味着 $|\det \varphi’|\not=0$，所以定理成立。

- **第二步：证明 $\varphi$ 是线性映射的情况下成立**

回顾我们的直观理解，最重要的一步就是告诉我们对于 $D_t$ 中的一个小区域 $D_i$，经过映射 $\varphi$ 后体积的缩放倍数为 $|\det \varphi’|$。我们先证明 $\varphi$ 是线性映射时这个几何直观是成立的。

**（定理三）设 $\varphi\in \mathbb{R}^n$ 是可逆线性变换，$E_t$ 为 $\mathbb{R}^n$ 中的 Jordan 可测集，则 $\mu(\varphi(E_t))=\mu(E_t)\cdot |\det \varphi’|$。**

证明：对于任意可逆线性变换，它都可以表示成有限个初等行变换的复合。我们先证明对于任意初等线性变换定理成立。

对于第一类初等行变换：交换第 $i,j\ (i<j)$ 行，即

$$
\varphi_1:(x^1,x^2,\cdots,x^n)\to(x^1,\cdots,x^{i-1},x^j,x^{i+1},\cdots,x_{j-1},x^i,x^{j+1},\cdots,x^n)
$$

此时 $|\det \varphi_1’|=1$。设 $E_t\subset I_{a,b}$，则

$$
\begin{aligned}
\mu(E_t) &=\int_{a_i}^{b_i}\mathrm{d} x^i\int_{a^j}^{b^j}\mathrm{d} x^j\int_{E’}\chi_{E_t}(x)\mathrm{d} x\\
\mu(\varphi(E_t)) &=\int_{a^i}^{b^i} \mathrm{d} x^j\int_{a^j}^{b^j}\mathrm{d} x^i \int_{E’} \chi_{E_t}(x)\mathrm{d} x=\mu(E_t) |\det \varphi_1’|
\end{aligned}
$$

对于第二类初等行变换：将第 $i$ 行乘上非零常数 $c$，即：

$$
\varphi_2:(x^1,x^2,\cdots,x^n)\to(x^1,\cdots,x^{i-1},cx^i,x^{i+1},\cdots,x^n)
$$

此时 $|\det \varphi_2’|=|c|$。则

$$
\begin{aligned}
\mu(\varphi_2(E_t)) &=\int_{E_x^{n-1}}\mathrm{d} x^1\cdots\mathrm{d} x^{i-1}\mathrm{d} x^{i+1}\cdots \mathrm{d} x^n |\int_{ca_i}^{cb_i}\chi_{\varphi_2(E_i)}(x)\mathrm{d} x^i|\\
&=\int_{E_x^{n-1}}\mathrm{d} x^1\cdots\mathrm{d} x^{i-1}\mathrm{d} x^{i+1}\cdots \mathrm{d} x^n \int_{a_i}^{b_i}|c|\chi_{E_i}(x)\mathrm{d} x^i\\
&= |c|\int_{E_x^{n-1}}\mathrm{d} x^1\cdots\mathrm{d} x^{i-1}\mathrm{d} x^{i+1}\cdots \mathrm{d} x^n \int_{a_i}^{b_i}\chi_{E_i}(x)\mathrm{d} x^i=|c|\mu(E_t)
\end{aligned}
$$

对于第三类初等行变换：将第 $i$ 行乘上 $c$ 倍加到第 $j$ 行，即：

$$
\varphi_3:(x^1,x^2,\cdots,x^n)\to (x^1,\cdots,x^{j-1},cx^i+x^{j},x^{j+1},\cdots,x^n)
$$

此时 $|\det \varphi_3’|=1$，则

$$
\begin{aligned}
\mu(\varphi_3(E_t)) &=\int_{E_x^{n-1}}\mathrm{d} x^1\cdots\mathrm{d} x^{j-1}\mathrm{d} x^{j+1}\cdots \mathrm{d} x^n \int_{E(x^1,\cdots,x^{j-1},x^{j+1},\cdots,x^n)} \mathrm{d} x^j\\
&=\int_{E_t^{n-1}}\mathrm{d} t^1\cdots\mathrm{d} t^{j-1}\mathrm{d} t^{j+1}\cdots \mathrm{d} t^n \int_{E(t^1,\cdots,t^{j-1},t^{j+1},\cdots,t^n)+ct^i} \mathrm{d} t^j\\
&=\mu(E_t) \cdot |\det \varphi_3’|
\end{aligned}
$$

对于初等行变换有限次复合的情况，注意到根据定理一，Jordan 可测集经过线性变换后仍是 Jordan 可测集，利用数学归纳法不断归纳，就可以得到对于任意线性变换 $\varphi$，都有 $\mu(\varphi(E_t))=\mu(E_t)\cdot |\det \varphi’|$。

- **第三步：证明 Jordan 可测集中定理成立**

我们先考虑这个 Jordan 可测集性质较好的情况，即它就是个闭区间：

**（定理四）设 $C$ 为 $D_t$ 中的一个立方体，则成立 $\mu(\varphi(C))=\int_C |\det \varphi’(t)| \mathrm{d} t$。**

> 如何证明？按照几何直观思考，将正方体分为若干块小正方体 $D_i$，我们需要证明 $\varphi(D_i)$ 和 $\varphi’(D_i)$ 形成的区域足够像，它们的误差是可以控制的。
> 
> 也就是说，$\varphi’^{-1}\circ \varphi(D_i)$ 形成的区域跟 $D_i$ 本身很像，且这两块区域的误差可以控制。如果我们能够找到两个正方体，一个完全在 $\varphi’^{-1} \circ \varphi(D_i)$ 内部，一个完全包含 $\varphi’^{-1}\circ \varphi(D_i)$，且这两个正方体在 $D_i$ 足够小时均趋近于 $D_i$，这样我们就可以证明误差可控了。
> 
> 如何证明一个正方体 $I$ 完全在 $\varphi^{-1}\circ \varphi(D_i)$ 内部？换句话说，就是 $\forall s\in I$，都能找到一个 $t\in D_t$ 使得 $\varphi^{-1}\circ \varphi(t)=s$。回顾我们证明逆映射定理的过程，这种类型的证明，可以用压缩映射定理实现。判断一个正方体包含于 $\varphi^{-1}\circ \varphi(D_i)$ 也是类似的。
> 
> 类似于逆映射定理的证明，构造函数 $\Phi_s(t)=t-\varphi^{-1}\circ \varphi(t)+s$。我们需要证明它是压缩映射。即证 $||\Phi_s(t_1)-\Phi_s(t_2)||\le \lambda||t_1-t_2||$（本定理中我们默认所用的范数均为无穷范数 $||x||=||x||_\infty$，由于压缩映射定理的证明只利用了范数的基本性质，所以对于任意范数均成立），也就是 $d_\infty(t_1-\varphi’^{-1}\circ \varphi(t_1),t_2-\varphi’^{-1}\circ \varphi(t_2))\le \lambda||t_1-t_2||$ 即可。我们只需要考虑 $t-\varphi’^{-1} \circ \varphi(t)$ 的性质就好了。类似逆映射定理，同样用拟微分中值定理进行控制即可。

证明：对给定的 $N\in \mathbb{N}_+$，将 $C$ 的每一条边进行 $N$ 等分，得到 $C$ 的一个分割 $P=\{I_j\}_{j=1}^{N^n}$。则我们有 $\mu(\varphi(C))=\sum_{j=1}^{N^n}\mu(\varphi(I_j))$。接下来我们对于每个 $j$ 进行考虑：记 $t_j$ 为 $I_j$ 的中心，$\lambda_j=\varphi'(t_j)$。不妨令 $t_j=0$，$\varphi(t_j)=x_j=0$。

由于 $I_j$ 紧致，$\varphi'(t)$ 连续，所以 $\varphi'(t)$ 一致连续，所以 $\forall \epsilon>0$，当 $N$ 足够大时，对于任意 $t_1,t_2\in I_j$，都有 $||\varphi'(t_1)-\varphi'(t_2)||<\epsilon$。

设 $f(t)=\varphi(t)-\lambda_j(t)$，则 $||f'(t)||=||\varphi'(t)-\varphi'(t_0)||<\epsilon$。根据引理二，$||f(t_1)-f(t_2)||\le \sup_{p\in I_j} ||f'(p)||\cdot ||t_1-t_2||<\epsilon ||t_1-t_2||$。

设 $||\lambda^{-1}_j(t)||=M$，有 $||\lambda^{-1}_j f(t_1)-\lambda^{-1}_j f(t_2)||\le ||\lambda^{-1}_j||\cdot ||f(t_1)-f(t_2)||<M\epsilon||t_1-t_2||$，即 $d_{\infty}(t_1-\lambda^{-1}_j\circ \varphi(t_1),t_2-\lambda^{-1}_j\circ \varphi(t_2))<\epsilon M ||t_1-t_2||$。由于 $t_j=\varphi(t_j)=0$，上式代入 $t_j$ 后变为 $||t-\lambda^{-1}_j\circ \varphi(t)||<\epsilon M ||t||$。

我们取 $\epsilon$ 足够小使得 $M\epsilon<1$。设正方体的边长为 $2a$，上面这个式子告诉我们原先正方体的边界和 $\lambda^{-1}_j\circ \varphi$ 这个变换形成的边界之间的距离不超过 $\epsilon Ma$，也就是说它至少应该包含一个边长为 $2a(1-\epsilon M)$ 的正方体。下面我们用压缩映射定理来证明这一点。

设 $\Phi_s(t)=t-\lambda_j^{-1}\circ \varphi(t)+s$，$\forall ||s||\le a(1-\epsilon M)$。我们有 $||\Phi_s(t)|| \le ||t-\lambda_j^{-1}\circ \varphi(t)||+||s||<\epsilon Ma+(1-\epsilon M)a=a$，所以 $\Phi_s(t)$ 在 $I_j$ 内封闭。而上文的不等式告诉了我们 $||\Phi_s(t_1)-\Phi_s(t_2)||<\epsilon M||t_1-t_2||$，所以我们证明了 $\Phi_s(t)$ 在 $I_j$ 内为压缩映射。

这意味着 $\forall ||s||\le a(1-\epsilon M)$，都存在恰好一个 $t$ 使得 $\Phi_s(t)=t$，即 $\lambda^{-1}_j\circ \varphi(t)=s$。这说明 $I_1=\{s \mid ||s||\le a(1-\epsilon M) \}\subset \lambda^{-1}_j\circ \varphi(I_j)$。也就是说，$\mu(I_1)=[2a(1-\epsilon M)]^n\le \mu(\lambda^{-1}_j \circ \varphi(I_j))$。

还是一样，既然原先正方体的边界和 $\lambda^{-1}_j\circ \varphi$ 这个变换形成的边界之间的距离不超过 $\epsilon Ma$，也就是说它也应该被一个边长为 $2a(1+\epsilon M)$ 的正方体包含。

这一部分较为简单：$||\lambda^{-1}\circ \varphi(t)||\le ||t||+||t-\lambda^{-1}\circ \varphi(t) || < a+\epsilon M||t||\le a(1+\epsilon M)$。所以 $\lambda^{-1}_j\circ \varphi(I_j) \subset I_2=\{ s\mid ||s||\le a(1+\epsilon M)\}$。也就是说，$\mu(\lambda^{-1}_j\circ \varphi(I_j))\le \mu(I_2)=[2a(1+\epsilon M)]^n$。

整理一下我们得到的两个不等式：

$$
\begin{aligned}
[2a(1-\epsilon M)]^n &\le \mu(\lambda^{-1}_j\circ \varphi(I_j)) &&\le [2a(1+\epsilon M)]^n \\
[2a(1-\epsilon M)]^n|\det \lambda_j| &\le \mu(\lambda_j\circ\lambda^{-1}_j\circ \varphi(I_j)) &&\le [2a(1+\epsilon M)]^n |\det \lambda_j| \\
(1-\epsilon M)^n\mu(I_j)|\det \lambda_j| &\le \mu(\varphi(I_j)) &&\le (1+\epsilon M)^n\mu(I_j) |\det \lambda_j|
\end{aligned}
$$

不等式的第二行由定理三得到。（注意到 $\lambda_j$ 是线性映射）

当 $N\to\infty$ 时，$\epsilon\to 0$，根据夹逼准则，$\mu(\varphi(I_j))\to \mu(I_j)|\det \lambda_j|$。由于 $\varphi'(t)$ 非退化，我们有 $\mu(\varphi(C))=\int_C |\det \varphi’(t)| \mathrm{d} t$，证毕。

显然这一定理可以容易地推广到 $C$ 为 $D_t$ 中任意闭区间的情形。

> 有没有觉得证明的思路和过程跟逆映射定理很像？逆映射定理告诉我们：可逆的线性近似可以推导出局部的微分同胚。而这个定理则告诉了我们：微分，这个局部的线性近似，对于体积的变换幅度和原函数相同。二者的证明思路都是一致的，就是证明原函数和微分在局部产生的变换是几乎一致的，而产生的误差可以用压缩映射定理进行控制。

现在我们将定理推广到 Jordan 可测集的情形：

**（定理五）设 $C$ 为 $D_t$ 中的 Jordan 可测集，且 $\overline{C}\subset D_t$，则 $\mu(\varphi(C))=\int_C |\det \varphi'(t)| \mathrm{d} t$。**

利用 Jordan 可测集边界点是零测集的性质：由于 $\overline{C}\subset D_t$，我们可以作 $D_t$ 中的紧致集 $K$ 使得 $\overline{C}\subset K^\circ$。由于 $C$ 是 Jordan 可测集，对于 $\forall \epsilon>0$，存在可数个闭区间 $I_{1,2,\cdots}$ 使得 $I_i\subset K$，$\partial C\subset \bigcup_{i=1}^\infty I_i^\circ$，$\sum_{i=1}^\infty \mu(I_i)<\epsilon$。由于紧致集的性质：任意开覆盖必有有限子覆盖。我们找到 $K$ 的一个开覆盖 $\{K-\partial C,I^\circ_1,I^\circ_2,\cdots\}$，其中必有有限子覆盖。这意味着存在有限个闭区间 $I_{1\cdots m}$ 使得

$$
I_i\subset K,\ \partial C\subset \bigcup_{i=1}^m I_i^\circ, \ \sum_{i=1}^m \mu(I_i)<\epsilon
$$

现取 $n$ 维区间 $I$ 使得 $D_t\subset I$，并将区间 $I_1,I_2,\cdots,I_m$ 的各边延长得到 $I$ 的一个分割 $P_0$。则对 $I$ 的任一由 $P_0$ 加细得到的分割 $P$，我们将其小区间分成如下三类：

$$
\begin{aligned}
P_1 &=\{J\in P \mid J\subset C^\circ \} \\
P_2 &=\{J\in P \mid J\cap \partial C \not= \varnothing\} \\
P_3 &=\{J\in P \mid J \cap \overline{C}=\varnothing \}
\end{aligned}
$$

> 为什么任何区间一定在这三类当中？我们其实需要证明，对于任意闭区间 $I$，如果它既包含 $\overline{C}$ 的内点和外点，那么它必然要包含一个边界点。
>
> 设 $p_0,q_0$ 分别为 $I$ 中的内点和外点，$d(p_0,q_0)=d$。考虑如下构造：若 $p_i,q_i$ 组成线段的中点是内点，则令 $p_{i+1}=\dfrac{p_i+q_i}{2}$，$q_{i+1}=q_i$；否则 $p_{i+1}=p_i$，$q_{i+1}=\dfrac{p_i+q_i}{2}$。
>
> 按照这种构造方式，$p_i$ 必定为内点，$q_i$ 必定为外点，且 $d(p_i,q_i)=\dfrac{d}{2^i}$。根据 Cauchy 收敛准则，$p,q$ 均为 Cauchy 列，且它们最终会收敛到同一个点 $p_\infty=q_\infty$。这个点必然是边界点。证毕。

记 $M=\sup_{t\in K} |\det \varphi'(t) |$。则我们有：

$$
\begin{aligned}
\underline{S}(|\det \varphi'|\chi_C, P) &=\sum_{J\in P_1} \inf_{t\in J}|\det \varphi'(t)|\mu(J)\\
& \le \sum_{J\in P_1}\int_J |\det \varphi'(t)|\mathrm{d} t\\
&=\sum_{J\in P_1}\mu(\varphi(J))\le \mu(\varphi(C))\\
\overline{S}(|\det \varphi'|\chi_C, P) &= \sum_{J\in P_1}\sup_{t\in J}|\det \varphi'(t)|\mu(J)+\sum_{J\in P_2}\sup_{t\in J} |\det \varphi'(t)| \chi_C \mu(J)\\
& \ge \sum_{J\in P_1}\sup_{t\in J}|\det \varphi'(t)|\mu(J)+\sum_{J\in P_2}\sup_{t\in J} |\det \varphi'(t)| \mu(J)-M\sum_{j\in P_2}\mu(J) \\
& \ge \sum_{J\in P_1\cup P_2} \int_J|\det \varphi'(t)| \mathrm{d} t-M\epsilon \\
& \ge \mu(\varphi(C))-M\epsilon 
\end{aligned}
$$

当 $||P||\to 0$ 时，$\epsilon\to 0$，此时可以得到：$\underline{S}(|\det \varphi'|\chi_C, P)=\overline{S}(|\det \varphi'|\chi_C, P)=\mu(\varphi(C))$，即 $\int_C |\det \varphi'(t)|\mathrm{d} t=\mu(\varphi(C))$。证毕。

- **第四步：证明变量代换公式**

证明：取 $n$ 维区间 $I$ 使得 $D_x\subset I^\circ$，考虑 $I$ 的分割 $P$ 使得其对小区间 $J$ 如果有 $J\cap \operatorname{supp} f\not=\varnothing$，则 $J\subset D_x$。记这样的小区间组成的集合为 $P'$。对于 $I$ 这样任一的分割 $P$，我们有：

$$
\begin{aligned}
\underline{S}(f\chi_{D_x},P) &= \sum_{J\in P'}\inf_{x\in J}f(x)\mu(J)=\sum_{J\in P'}\inf_{x\in J}f(x)\mu(\varphi\circ \varphi^{-1}(J))\\
&= \sum_{J\in P'}\inf_{t\in \varphi^{-1}(J)} f\circ \varphi(t)\int_{\varphi^{-1}(J)}|\det \varphi'(t)|\mathrm{d} t\\
& \le \sum_{J\in P'}\int_{\varphi^{-1}(J)}f\circ \varphi(t)\cdot |\det \varphi'(t)|\mathrm{d} t\\
& = \int_{D_t}f\circ \varphi(t)\cdot |\det \varphi'(t)| \mathrm{d} t \\
& \le \sum_{J\in P'}\sup_{t\in \varphi^{-1}(J)} f\circ \varphi(t)\int_{\varphi^{-1}(J)}|\det \varphi'(t)|\mathrm{d} t\\
& = \sum_{J\in P'}\sup_{x\in J}f(x)\mu(J)\le \overline{S}(f\chi_{D_x},P)
\end{aligned}
$$

令 $||P||\to 0$，此时 $\underline{S}(f\chi_{D_x},P)=\overline{S}(f\chi_{D_x},P)$，我们得到

$$
\int_{D_x} f(x)\mathrm{d} x=\int_{D_t}f\circ \varphi(t)\cdot |\det \varphi'(t)| \mathrm{d} t
$$

因此变量代换公式成立，证毕。

## 变量代换公式证明 - 退化情况

**（变量代换公式 - 退化情况）设 $\varphi:D_t\to D_x$ 为 $\mathbb{R}^n$ 中有界开集之间的双射，且 $\varphi$ 连续可微，$f$ 为定义在 $D_x$ 上的函数，$\operatorname{supp} f$ 为 $D_x$ 的紧致子集。如果 $f\in\mathcal{R}(D_x)$，则 $f\circ\varphi\cdot|\det \varphi’|\in \mathcal{R}(D_t)$，并且有：**

$$
\int_{D_x} f(x) \mathrm{d} x=\int_{D_t} f\circ\varphi(t) \cdot |\det \varphi’(t) | \mathrm{d} t
$$

注意上述推论中我们不再假定 $|\det \varphi'(t)|\not= 0$ 对 $\forall t\in D_t$ 成立，也即 $\varphi^{-1}:D_x\to D_t$ 不一定可微。为证明此推论，我们可以在 $D_t$ 和 $D_x$ 中分别挖去集合 $E=\{t\in D_t \mid \det \varphi'(t)=0 \}$ 以及 $\varphi(E)$。

集合 $E$ 可以不是零测集，因为被积函数在 $E$ 上取值为零，不会影响积分值。但 $\varphi(E)$ 上 $f(x)$ 不一定为零，为此我们希望 $\varphi(E)$ 足够小，最好是一个零测集。事实证明确实如此：

**（Sard 定理）设 $D$ 为 $\mathbb{R}^n$ 中的开集，$\varphi: D\to \mathbb{R}^n$ 为连续可微映射。记 $E=\{t\in D\mid \det \varphi'(t) =0\}$，则 $\varphi(E)$ 为一零测集。**

这个定理的几何直观是显然的：在 $\varphi'(t)=0$ 的附近，$\varphi$ 相当于降维打击，$\varphi(E)$ 自然是要多小就有多小。

我们先对 $n=1$ 的情况进行证明。对 $D$ 中任一闭区间 $[\alpha,\beta]$，我们来证明 $\varphi(E\cap [\alpha,\beta])$ 为零测集。因为 $\varphi'(t)$ 连续，在闭区间上则一致连续，因此 $\forall \epsilon>0$，都有 $\delta>0$ 使得 $|t_1-t_2|<\delta$ 时 $|\varphi'(t_1)-\varphi'(t_2)|<\epsilon$。

由 Lagrange 中值定理，$\varphi(x)-\varphi(x_0)=\varphi'(t)(x-x_0) \ (t\in (x,x_0))$。当 $|x-x_0|<\delta$ 时，$|\varphi'(t)-\varphi'(x_0)|<\epsilon$，因此 $|\varphi(x)-\varphi(x_0)-\varphi'(x_0)(x-x_0)|\le \epsilon|x-x_0|$。

注意到不等式左边其实是原函数和切线方程的误差，这个不等式告诉我们误差可以由 $|x-x_0|$ 控制。于是我们将 $[\alpha,\beta]$ 作 $N$ 等分使得 $\dfrac{\beta -\alpha}{N}<\dfrac{\delta}{2}$，记所得区间为 $I_{1\cdots n}$。如果 $I_k\cap E\not=\varnothing$，则对任意 $x_k\in I_k\cap E$，我们有 $\varphi'(x_k)=0$，并且 $\forall x\in I_k$ 都有：

$$
|\varphi(x)-\varphi(x_k)|<\epsilon|x-x_k|\le \epsilon\dfrac{\beta -\alpha}{N}
$$

所以

$$
\varphi(I_k\cap E)\subset \varphi(I_k)\subset (\varphi(x_k)-\epsilon\dfrac{b-a}{N},\varphi(x_k)+\epsilon\dfrac{b-a}{N})=E_k
$$

由此我们得到

$$
\varphi([\alpha,\beta]\cap E)\subset \bigcup_{i=1}^N E_i,\ \sum_{i=1}^n\mu(E_i)\le 2(b-a)\epsilon
$$

由 $\epsilon$ 的任意性可知 $\varphi([\alpha,\beta]\cap E)$ 为零测集。根据引理一，$D$ 可以写成可数个区间的不交并，$\varphi(E)$ 为零测集。

接下来我们考虑一般情况，照葫芦画瓢：

设 $I\subset D$ 为一闭立方体，我们来证明 $\varphi(I\cap E)$ 为零测集。因为 $\varphi'(t)$ 连续，所以在紧致集 $I$ 上一致连续。对于任意 $\epsilon>0$，存在 $\delta>0$ 使得 $||x_1-x_2||<\delta$ 时 $||\varphi'(x_1)-\varphi'(x_2)||<\epsilon$。

由拟微分中值定理，$\varphi(x)-\varphi(x_0)=\varphi'(t)(x-x_0)\ (t\in(x,x_0))$。当 $||x-x_0||<\delta$ 时，$||\varphi(x)-\varphi(x_0)-\varphi'(x_0)(x-x_0)||<\epsilon ||x-x_0||$。

我们将 $I$ 的每条边作 $N$ 等分使得 $\dfrac{a}{N}<\dfrac{\delta}{2}$。（设 $I$ 的边长为 $a$）记所得区间为 $I_{1\cdots N^n}$。如果 $I_k\cap E\not=\varnothing$，则对任意 $x_k\in I_k\cap E$，我们有 $\det \varphi'(x_k)=0$，并且 $\forall x\in I_k$ 都有：

$$
||\varphi(x)-\varphi(x_k)-\varphi'(x_k)(x-x_k)||<\epsilon ||x-x_k||
$$

> 这是什么意思？假如 $n=2$，$\operatorname{rank} \varphi'(x_k)=1$，这意味着参数方程 $x\to \varphi(x_k)+\varphi'(x_k)(x-x_k)$ 是一条直线，如果限制 $x\in I_k$ 就是一条线段。这个不等式告诉我们 $\varphi(x)$ 这个点与这条线段的距离 $<\epsilon ||x-x_k||\le \epsilon\dfrac{a}{N}\sqrt n$。那我们只需要算出来与这条线段距离 $\le \epsilon\dfrac{a}{N}\sqrt n$ 的点形成的集合（像一根木棍），就可以覆盖 $I_k$ 了，且木棍的体积可以用 $\epsilon$ 控制。
>
> 对于更高维的空间也是类似。

此时 $\{\varphi'(x_k)(x-x_k) \mid x\in I_k\}$ 包含于 $\mathbb{R^n}$ 的一个 $n-1$ 维子空间中 $V$ 中。而对 $\forall x\in I_k$，$\varphi(x)$ 与超平面 $\varphi(x_0)+V$ 的距离小于 $\epsilon\dfrac{a}{N}\sqrt n$。由于 $\varphi'$ 在紧致集 $I_k$ 中存在最大值 $M$，因此有 $||\varphi(y)-\varphi(x)||\le M||y-x||$ 对任意 $x,y\in I_k$ 均成立。

由此可知 $\varphi(x)$ 包含在一个柱体 $E_k$ 内，其高小于 $2\dfrac{a}{N}\sqrt n\epsilon$，其底为半径小于 $\dfrac{a}{N}M$ 的 $n-1$ 维球。因此

$$
\varphi(I\cap E)\subset \bigcup_{k=1}^{N^n} E_k,\ \sum_{k=1}^{N^n}\mu(E_k)\le N^nc\dfrac{\epsilon}{N^n}=c\epsilon
$$

其中 $c$ 为可以计算的常数。由 $\epsilon$ 的任意性和引理一，Sard 定理得证。

最后我们根据 Sard 定理来证明变量代换公式的退化情况。

还是一样，先证可积性，再证积分值正确。假设 $f\in \mathcal{R}(D_x)$，$\operatorname{supp} f\subset D_x$，则 $f$ 在 $D_x$ 上几乎处处连续。由于 $\varphi:D_t\to D_x$ 为 1-1 的连续单射，故 $\operatorname{supp} f\circ\varphi \subset D_t$。因此要证明 $f\circ \varphi \cdot |\det \varphi'|\in \mathcal{R}(D_t)$，只要证明 $g=f\circ \varphi \cdot |\det \varphi'|$ 在 $D_t$ 上几乎处处连续即可。（而不用考虑 $D_x$ 或 $D_t$ 的边界问题）

> 还记得我们原来是怎么证明可积性的吗？定理一要求 $\varphi$ 是微分同胚，如果 $\varphi$ 是微分同胚，那么 $f$ 在 $D_x$ 上是零测集，就意味着 $f\circ\varphi$ 在 $D_t$ 上是零测集。
>
> 根据 $\varphi'$ 的连续性和 $f$ 的有界性，$g$ 在满足 $\det \varphi'(t)=0$ 的点上一定连续。只要我们挖去这些点，剩下的点就满足 $\det \varphi'(t)\not= 0$，微分同胚这不就来了吗！

记 $D(f)$ 为 $f$ 在 $D_x$ 上的不连续点集合，$D(g)$ 为 $g$ 在 $D_t$ 上的不连续点集合。则由 $\varphi,\varphi'$ 的连续性，如果 $f$ 在 $x_0$ 处连续，那么 $g$ 在 $\varphi^{-1}(x_0)$ 处连续。那么它的逆否命题 $\varphi(D(g))\subset D(f)$ 也成立。

因此 $\varphi(D(g))$ 为零测集。又由 $\varphi'$ 的连续性和 $f$ 的有界性可知 $g$ 在满足 $\det \varphi'(t)=0$ 的点上一定连续，也就是说：

$$
D(g)\subset D_t\backslash E_t, \ E_t:=\{t\in D_t \mid \det \varphi'(t)=0\}
$$

注意在 $D_t\backslash E_t$ 这个范围有 $\det \varphi'(t)\not=0$，根据逆映射定理，$\varphi: D_t\backslash E_t\to D_x\backslash \varphi(E_t)$ 在定义域内任意一点的局部是微分同胚。又由于 $\varphi$ 是整体 1-1 映射，所以 $\varphi$ 整体也是微分同胚。

再根据定理一，此时 $\varphi(D(g))$ 是零测集，故 $D(g)$ 也是零测集，从而 $g\in \mathcal{R}(D_t)$。

接下来我们证明积分值正确。

> 还是一样，我们把 $\det \varphi'(t)=0$ 的点称为坏点（即 $E_t$ 中的点），其余点为好点。根据上文，好点区域是微分同胚，这意味着可以直接使用变量代换公式得到正确的积分值。而对于坏点区域，我们则必须保证 $f$ 在 $\varphi(E_t)$ 这个区域的积分为零，即证 $\varphi(E_t)$ 是 Jordan 零测集。
>
> 也就是说，$\int_{D_t} f\circ \varphi(t)\cdot |\det \varphi'(t)|\mathrm{d} t=\int_{E_t} f\circ \varphi(t)\cdot |\det \varphi'(t)|\mathrm{d} t+\int_{D_t\backslash E_t}  f\circ \varphi(t)\cdot |\det \varphi'(t)|\mathrm{d} t$，然后又等于 $0+\int_{D_t\backslash E_t}  f\circ \varphi(t)\cdot |\det \varphi'(t)|\mathrm{d} t=\int_{D_x} f(x)\mathrm{d} x$，对吧，很完美啊！
>
> 这样子就证明完了……吗？
>
> 我们做一个简单的类比：我们把 $[0,1]$ 区域划分为 $[0,1]$ 中的有理数和无理数两块分别积分。可以这样做吗？当然不可以！上面的“证明”也是一样。我们完全没有保证 $E_t$ 是 Jordan 可测集就把它拎出来积分，虽然这一部分积分确实是零没错，但你也没有保证 $D_t\backslash E_t$ 是 Jordan 可测集啊！
>
> 那我们该如何处理？
>
> 我们既然不能直接在 $E_t$ 上积分，我们就用有限个正方体组成的集合 $N$ 来覆盖 $E_t$，而 $N$ 根据定义显然是 Jordan 可测的。在 $N$ 上，我们可以积分，并且因为 $|\det \varphi'|$ 很小，可以控制它的贡献任意小；而在 $D_t\backslash N$ 上，我们就可以直接用一般的变量代换公式即可。然后我们取极限 $N\to E_t$，得到最终的退化版公式。
>
> 这样，我们就不需要 $E_t$ 本身是 Jordan 可测的，只需要它能被 Jordan 可测集任意逼近即可。

我们在 $D_t$ 中取（由有限个闭区间的并组成的）紧致集 $\Omega_t$ 使得 $\operatorname{supp} f\circ \varphi\subset \Omega_t^\circ$。设 $E_t’=E_t\cap \Omega_t$，$E_x’=\varphi(E’_t)$。

> 为什么可以是有限个闭区间的并？
> 
> $\forall x\in D_t$，由于 $D_t$ 是开集，我们总能找到一个开区间使得它的闭包在 $D_t$ 中。这些开区间都在 $D_t$ 内且形成了紧致集 $\operatorname{supp} f\circ \varphi$ 的开覆盖。
> 
> 那么它一定存在有限子覆盖。我们取这一组子覆盖中所有开区间的闭包即可构造。

由 Sard 定理可知 $E’_x$ 为零测集。注意到 $E_t$ 为紧致集（有界连续函数的零点集合紧致，证明见第二周作业），而 $E’_t$ 为两个紧致集的交一定也紧致。所以 $E’_x$ 也为紧致集。由于紧致集上任意开覆盖必有有限子覆盖，所以 $\forall \epsilon>0$ 存在有限个开区间 $I_{1\cdots k}$ 使得：

$$
\overline{I_i}\subset D_x,\ E’_x\subset \bigcup_{i=1}^k I_i,\ \sum_{i=1}^k \mu(I_i)<\epsilon
$$

而利用 $\varphi$ 和 $\varphi’$ 的连续性和 $E’_t$ 的紧致性，我们可以找到有限个开区间 $J_{1\cdots m}$ 使得：

1. $\overline{J_i}\subset \Omega_t$，$E’_t\subset \bigcup_{i=1}^m J_i$。
2. 对每一 $J_i$ 存在 $I_p$ 使得 $\varphi(\overline{J_i})\subset I_p$ 且 $\forall t\in J_i$ 都有 $|\det \varphi’(t)|<\epsilon$。

> 为什么可以这样构造？
> 
> 由于 $I_i$ 是开集，$\varphi$ 连续，对于任意 $x\in I_i$，都存在 $\delta>0$ 使得 $B(x,\delta)\subset I_i$，然后存在 $\alpha>0$ 使得 $\varphi(B(\varphi^{-1}(x),\alpha))\subset B(x,\delta)$。
> 
> 由于 $E_t’$ 紧致，所以 $\varphi’(t)$ 在其中一致连续。这告诉我们在第一步可以让 $\alpha$ 足够小，使得任意 $t\in B(\varphi^{-1}(x),\alpha)$ 都满足 $|\det \varphi’(t)|<\epsilon$。
> 
> 我们把所有的 $B(\varphi^{-1}(x),\alpha)$ 提取出来，它构成了 $E_t’$ 的一个开覆盖，且所有的 $\varphi(B(\varphi^{-1}(x),\alpha))$ 都完全在 $I$ 中的某一个区间内。而紧致集 $E_t’$ 中任意开覆盖都有有限子覆盖，我们取其中的一个有限子覆盖即可。

根据上面的分析，我们知道：$\cup\overline{J}$，$\Omega_t$，和 $\Omega_x=\varphi(\Omega_t)$ 都是 Jordan 可测集，这意味着上面的积分是良定义的。而 $\Omega_t\backslash \cup \overline{J}$ 这个区域中 $\varphi$ 是微分同胚，可以使用一般形式的变量代换公式。我们有：

$$
\begin{aligned}
\int_{\Omega_x\backslash \cup \varphi(\overline{J})} f(x) \mathrm{d} x &= \int_{\Omega_t \backslash \cup \overline{J}} f\circ \varphi(t) \cdot |\det \varphi’(t)|\mathrm{d} t\\
\int_{D_x} f(x) \mathrm{d} x-\int_{\cup \varphi(\overline{J})}f(x)\mathrm{d} x &=
\int_{D_t} f\circ \varphi(t) \cdot |\det \varphi’(t)|\mathrm{d} t-
\int_{\cup \overline{J}} f\circ \varphi(t) \cdot |\det \varphi’(t)|\mathrm{d} t
\end{aligned}
$$

设 $M=\max_{x\in D_x} |f(x)|$，我们有：

$$
\begin{aligned}
|\int_{\cup \varphi(\overline{J})}f(x)\mathrm{d} x| &\le M\sum_{i=1}^k\mu(I_i)<M\epsilon \\
|\int_{\cup \overline{J}} f\circ \varphi(t) \cdot |\det \varphi’(t)|\mathrm{d} t| &< M\epsilon\mu(E_t)
\end{aligned}
$$

当 $\epsilon\to 0$ 时，上面两式均趋近于零。这个时候我们有：

$$
\int_{D_x} f(x) \mathrm{d} x=
\int_{D_t} f\circ \varphi(t) \cdot |\det \varphi’(t)|\mathrm{d} t
$$

变量代换公式（退化情况）成立。

## *尾声：为什么我们需要 Lebesgue 积分

回到退化情况的证明。我们用一个 Jordan 可测集（$\cup \overline{J}$）逼近一个不一定 Jordan 可测的集合（$E_t$）。我们的问题是：这个跟直接拆分成 $\int_{E_t} g(t)\mathrm d t$ 和 $\int_{D_t\backslash E_t} g(t)\mathrm{d} t$（上面的经典错误做法）有什么区别？为什么我们不可以直接拆，但可以通过 Jordan 可测集逼近 + 取极限的方法来达成一样的效果？如果可以用 Jordan 可测集逼近，那什么集合是可以通过 Jordan 可测集逼近的？那 Jordan 可测集又有什么用？

我们先来回顾一个问题：Jordan 可测集是什么？

它指的是示性函数可积的区域，边界点为零测集的区域，可以用有限多个闭区间内外逼近的区域。在这个区域中，$f$ 是否可积只取决于 $f$ 在这块区域的内部不连续点是否为零测集，而不用管区域点边界情况。这告诉我们，Riemann 积分在这样子的区域才是良定义的。

如果一个区域可以写成有限多个闭区间的并集。那么通过延长所有闭区间的边，它也可以写成有限多个闭区间的不交并。那它肯定可以用有限多个区间内外逼近（内和外都一样了，那肯定能逼近）。那么这样的区间一定 Jordan 可测。在上面一章的证明中，我们就是利用这样的性质证明了 $\Omega_t$ 和 $\cup \overline{J}$ 是 Jordan 可测的。

那什么样的区域可以用 Jordan 可测集逼近？根据上一段，可以写成可数多个闭区间并集的区域自然可以用 Jordan 可测集（有限多个闭区间并集形成的区域）来逼近。根据引理一，开集可以用 Jordan 可测集逼近。开集的补集，也就是并集，也可以用 Jordan 可测集逼近。

而 $E_t,E_x$ 是闭集，所以它自然能用 Jordan 可测集逼近。上面的证明告诉我们，能够用 Jordan 可测集逼近的区域，和 Jordan 可测集看起来同样也是积分良定义的。

我们假设有一个这样的积分，它对于能用 Jordan 可测集逼近的区域也是良定义的，那上面的“经典错误”方法就对了，我们就可以直接证明了：

$$
\int_{D_t} g(t)\mathrm{d} t=\int_{D_t\backslash E_t} g(t)\mathrm{d}t+\int_{E_t} g(t)\mathrm{d} t=\int_{D_x\backslash \varphi(E_t)} f(x) \mathrm{d} x+0=\int_{D_x} f(x) \mathrm{d} x
$$

这就是我们为什么需要 Lebesgue 积分。

上面的积分就是 Lebesgue 积分。可以写成可数多个闭区间并集的区域是 Lebesgue 可测集中的一种，而退化情况的证明方法，就是用 Riemann 积分的工具，去实现 Lebesgue 积分的思想。