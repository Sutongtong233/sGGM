# sGGM
## FST
Implementation of FST algorithm in [FST-IJCAI2020]([地址]https://www.ijcai.org/Proceedings/2020/0410.pdf "FST-IJCAI2020")

run `python ./main/FST.py`


# SIMULE

### Method

linear programming problem:

$$
\sum_{j=1}^{(K+1) p} \mathbf{u}_{j}
$$


Use **pulp** to solve the LP problem.

### Simulated dataset

$$
\Omega^{(i)}=\mathbf{B}_I^{i}+\mathbf{B}_S+\delta^{(i)}I
$$



### baselines

- JGL-fused
- JGL-group
- SIMONE

