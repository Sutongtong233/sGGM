import sys
sys.path.append('.')
from scipy.sparse.csgraph import connected_components
import scipy.linalg
from generate import *

n = 100
p = 10
num_blks = 2
cov_mat_prime, reorder, prec_mat, X = generate_blk_perturb(n, p, num_blks)
cov_sample = (1/n)*(X.T).dot(X) # TODO
# cov_sample /= cov_sample.max()

# print(cov_mat_prime)
# reorder using scipy
def FST(cov, nu, lamb):
    '''
    params:
    nu and lamb are two threshold
    '''
    print("estimated perturbed ")
    cov[cov<nu] = 0
    compNum, bins = connected_components(cov, directed=False)  # TODO:cluster内的节点顺序？
    print(compNum, bins)
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

    for index in range(compNum):
        start = offset
        end = compSize[index] + offset
        offset = end
        each_comp = np.linalg.inv(reorder_cov[start:end, start:end])
        if not each_comp.shape == (1, 1):
            each_comp /= np.max(abs(each_comp))
            # each_comp = softThreshold(each_comp, regPar)
            nonzero_seq.extend([ i for i in range(start, end)])
        comp_cov.append(each_comp)
    Omega = scipy.linalg.block_diag(*comp_cov)
    print("estimated:")
    print(Omega.round(3))

if __name__ == "__main__":
    FST(cov_sample, 0.3, 0)