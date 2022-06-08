import sys
sys.path.append(".")
from scipy.sparse.csgraph import connected_components
from sklearn.covariance import GraphicalLasso
import scipy.linalg
from generate import *
import time

# cov_sample /= cov_sample.max()
# reorder using scipy
def GLasso(data, alpha, lamb):
    glasso_cov = GraphicalLasso(alpha = alpha).fit(data).covariance_
    glasso_omega = np.linalg.inv(glasso_cov)
    glasso_omega[np.abs(glasso_omega) < lamb] = 0
    return glasso_omega

def EE(cov, nu, lamb):
    cov[abs(cov)<nu] = 0
    prec = np.linalg.inv(cov)
    prec[abs(prec)<lamb] = 0
    prec /= prec.max()
    return prec

def FST(cov, nu, lamb):
    '''
    params:
    nu and lamb are two threshold
    '''
    print("estimated perturbed ")
    cov[abs(cov)<nu] = 0
    compNum, bins = connected_components(cov, directed = False)  # TODO:cluster内的节点顺序？
    # print(compNum, bins)
    compSize = [0 for i in range(compNum)]
    for i in range(len(bins)):
        compSize[bins[i]] += 1
    var_seq = [(i,bins[i]) for i in range(p)]
    var_seq = [each[0] for each in sorted(var_seq,key=lambda x:x[1],reverse=False)] # The reordered sequence of vars
    reorder_cov = cov_mat_prime[var_seq]
    reorder_cov = reorder_cov[:,var_seq]
    #Split each connected component
    offset = 0
    comp_cov = []
    nonzero_seq = []
    sum_time = 0
    for index in range(compNum):  # efficiency!
        start = offset
        end = compSize[index] + offset
        offset = end
        t0 = time.time()
        each_comp = np.linalg.inv(reorder_cov[start:end, start:end])
        sum_time += time.time()-t0
        if not each_comp.shape == (1, 1):
            each_comp /= np.max(abs(each_comp))
            # each_comp = softThreshold(each_comp, regPar)
            nonzero_seq.extend([ i for i in range(start, end)])
        comp_cov.append(each_comp)
    Omega = scipy.linalg.block_diag(*comp_cov)
    Omega[abs(Omega)<lamb] = 0
    print("FST time", sum_time)
    # print(Omega.round(3))
    return Omega

if __name__ == "__main__":
    n = 1000
    p = 1000
    num_blks = 20
    lamb = 0
    cov_mat_prime, reorder, prec_mat_prime, X = generate_blk_perturb(n, p, num_blks)
    print(X)
    # print(reorder)
    cov_sample = (1/n)*(X.T).dot(X) # TODO
    
    print("ground truth")
    print(prec_mat_prime.round(3))

    
    res_FST = FST(cov_mat_prime, 0.1, lamb).round(3)
    t0 = time.time()
    reorder_back = np.argsort(reorder)
    res_FST = res_FST[reorder_back]
    res_FST = res_FST[:, reorder_back]
    print("FST estimated:")
    # print(res_FST, "time", t1)

    print("GLasso estimated:")
    
    res_GLasso = GLasso(cov_mat_prime, 0.5, lamb).round(3)
    t2 = time.time() - t0
    res_GLasso /= res_GLasso.max()
    # print(res_GLasso, "time", t1)


    print("EE estimated")
    t0 = time.time()
    res_EE = EE(cov_mat_prime, 0.5, lamb).round(3)
    t3 = time.time() - t0
    # print(res_EE, "time", t1)

    print("FST", np.linalg.norm(prec_mat_prime-res_FST),
          "GLasso", np.linalg.norm(prec_mat_prime-res_GLasso), t2,
          "EE", np.linalg.norm(prec_mat_prime-res_EE), t3
          )
    # EE(cov_sample, 0.5, 0.5)