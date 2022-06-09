# sGGM
## FST
Implementation of FST algorithm in [Quadratic Sparse Gaussian Graphical Model Estimation Method for Massive Variables (ijcai.org)](https://www.ijcai.org/Proceedings/2020/0410.pdf)
### run
run `python ./main/FST.py`

# SIMULE
Implementation of SIMULE algorithm in [A constrained $$\ell $$ ℓ 1 minimization approach for estimating multiple sparse Gaussian or nonparanormal graphical models | SpringerLink](https://link.springer.com/article/10.1007/s10994-017-5635-7)(https://www.ijcai.org/Proceedings/2020/0410.pdf)
### method

Solving linear programming problem in Eq(11). Use **pulp** to solve the LP problem.
### run
run `python ./main/SIMULE.py`

### Simulated dataset

$$
\Omega^{(i)}=\mathbf{B}_I^{i}+\mathbf{B}_S+\delta^{(i)}I
$$



### baselines

- JGL-fused
- JGL-group
- SIMONE

