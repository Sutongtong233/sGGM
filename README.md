# sGGM
## FST
Implementation of FST algorithm in [FST-IJCAI2020]([地址]https://www.ijcai.org/Proceedings/2020/0410.pdf "FST-IJCAI2020")

run `python ./main/FST.py`


# SIMULE

### Method

linear programming problem:
![](http://latex.codecogs.com/svg.latex?
$$
\underset{\mathbf{u}_{j}, \theta}{\operatorname{argmin}} \sum_{j=1}^{(K+1) p} \mathbf{u}_{j}

\begin{aligned}
&-\theta_{j} \leq \mathbf{u}_{j}, \quad j=1, \ldots,(K+1) p \\
&\theta_{j} \leq \mathbf{u}_{j}, \quad j=1, \ldots,(K+1) p \\
&-\mathbf{A}_{k,}^{(i)^{T}} \theta+\boldsymbol{b}_{k} \leq c, \quad k=1, \ldots, p, i=1, \ldots, K \\
&\mathbf{A}_{k,}^{(i)^{T}} \theta-\boldsymbol{b}_{k} \leq c, \quad k=1, \ldots, p, i=1, \ldots, K
\end{aligned}
$$)

Use **pulp** to solve the LP problem.

### Simulated dataset

$$
\Omega^{(i)}=\mathbf{B}_I^{i}+\mathbf{B}_S+\delta^{(i)}I
$$



### baselines

- JGL-fused
- JGL-group
- SIMONE

