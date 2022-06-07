from cv2 import log
import numpy as np
from generate import *
from sklearn.covariance import GraphicalLasso
import math

def MLE(X, thres):
    n = X.shape[0]
    p = X.shape[1]
    S = S = (1/n)*(X.T).dot(X)
    Omega_hat = np.linalg.inv(S)
    Omega_hat[Omega_hat<thres] = 0
    return Omega_hat
    

if __name__ == "__main__":
    cov_mat, prec_mat, X = generate_line(100, 5)
    # res_gd = GD(X, 0.001, 2000)
    res_MLE = MLE(X, 0.1)
    res_GLasso = GraphicalLasso(alpha=0.1).fit(X).covariance_  # tuning lambda
    res_GLasso = np.linalg.inv(res_GLasso)
    res_GLasso[res_GLasso<0.05] = 0
    print(prec_mat)
    print(res_MLE)
    print(res_GLasso)