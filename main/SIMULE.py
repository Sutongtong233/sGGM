import numpy as np

    

def SIMULE(X_ls, epsilon):
    K = len(X_ls)
    n = X_ls[0].shape[0]
    p = X_ls[0].shape[1]
    
    A_ls = [np.zeros([p, (K+1)*p]) for i in range(K)]
    for i in range(K):
        X = X_ls[i]
        S = (1/n)*(X.T).dot(X)
        A_ls[i][:, i*p:(i+1)*p] = S
        A_ls[i][:, -p:] = (1/(epsilon*K))*S
    # column-wise calculation
    for j in range(p):
        bj = np.zeros([p, 1])
    

