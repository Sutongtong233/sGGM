# sGGM
## FST
Implementation of FST algorithm in ..

# SIMULE

### Method

linear programming:
$$
\underset{\mathbf{u}_{j}, \theta}{\operatorname{argmin}} \sum_{j=1}^{(K+1) p} \mathbf{u}_{j}
\\s.t.
$$

$$
\begin{aligned}
&-\theta_{j} \leq \mathbf{u}_{j}, \quad j=1, \ldots,(K+1) p \\
&\theta_{j} \leq \mathbf{u}_{j}, \quad j=1, \ldots,(K+1) p \\
&-\mathbf{A}_{k,}^{(i)^{T}} \theta+\boldsymbol{b}_{k} \leq c, \quad k=1, \ldots, p, i=1, \ldots, K \\
&\mathbf{A}_{k,}^{(i)^{T}} \theta-\boldsymbol{b}_{k} \leq c, \quad k=1, \ldots, p, i=1, \ldots, K
\end{aligned}
$$



### Simulated dataset

$$
\Omega^{(i)}=\mathbf{B}_I^{i}+\mathbf{B}_S+\delta^{(i)}I
$$



### baselines

- JGL-fused
- JGL-group
- SIMONE

