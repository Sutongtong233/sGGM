import enum
import numpy as np
# np.random.seed(0)

# 1-2-3-4-5...-p
def generate_line(n, p):
    prec_mat = np.eye(p)
    for i in range(p-1):
        prec_mat[i][i+1] = prec_mat[i+1][i] = 0.3
    cov_mat = np.linalg.inv(prec_mat)
    X = np.random.multivariate_normal(mean=np.zeros((1, p))[0], cov=cov_mat, size=n, check_valid='ignore', tol=0.1)
    return cov_mat, prec_mat, X


def generate_blk(n, p, num_blks):
    assert p%num_blks == 0   # divide into blocks in average
    blk_size = p//num_blks
    temp = np.eye(blk_size)
    for i in range(blk_size):
        for j in range(i + 1, blk_size):
            val = 0.7 ** abs(i - j)
            temp[i][j] = val
            temp[j][i] = val
    temp = np.linalg.inv(temp)  # block precision

    # # Combine them into the final matrix
    blk_prec_mat = np.zeros([p, p])
    for index in range(num_blks):
        low=index*blk_size
        for i in range(blk_size):
            for j in range(i, blk_size):
                blk_prec_mat[low+i,low+j]=temp[i,j]
                blk_prec_mat[low + j, low + i] = temp[j,i]
    blk_cov_mat = np.linalg.inv(blk_prec_mat)
    X = np.random.multivariate_normal(mean=np.zeros((1, p))[0], cov=blk_cov_mat, size=n, check_valid='ignore', tol=0.1)
    return blk_cov_mat, blk_prec_mat, X

    
def generate_blk_perturb(n, p, num_blks):
    cov_mat, prec_mat, X = generate_blk(n, p, num_blks)
    
    # reorder the cov_mat
    reorder = np.random.permutation(range(p)) # need to be recorded!
    # print(reorder)
    cov_mat_prime = cov_mat[reorder]
    cov_mat_prime = cov_mat_prime[:, reorder]  # TODO: perturb!
    prec_mat_prime = prec_mat[reorder]
    prec_mat_prime = prec_mat_prime[:, reorder]
    X = X[:, reorder]
    return cov_mat_prime, reorder, prec_mat_prime, X

def generate_multi_graph(n, p, K, delta):
    # 0.5: p=0.1, 0:p=0.9
    share = np.random.rand(p, p)
    # print(share)
    share[share<0.9] = 0
    share[share>=0.9] = 0.5
    # 0.5: p=0.05i, 0:p=1-0.05i
    special_ls = [np.random.rand(p, p) for i in range(K)]
    prec_ls = [np.random.rand(p, p) for i in range(K)]
    cov_ls = [np.random.rand(p, p) for i in range(K)]
    X_ls = [np.random.rand(n, p) for i in range(K)]
    pos_diaginal = delta * np.eye(p)

    for i in range(K):
        special_ls[i][special_ls[i]<=1-0.05*i] = 0
        special_ls[i][special_ls[i]>1-0.05*i] = 0.5
        prec_ls[i] = special_ls[i] + share + pos_diaginal
        cov_ls[i] = np.linalg.inv(prec_ls[i])
        print(prec_ls[i])
        # according to the prec_ls, generate the X
        X_ls[i] = np.random.multivariate_normal(mean=np.zeros((1, p))[0], cov=cov_ls[i], size=n, check_valid='ignore', tol=0.1)
    return prec_ls, X_ls
    

if __name__ == "__main__":
    prec_ls, X_ls = generate_multi_graph(5, 5, 0.1)

