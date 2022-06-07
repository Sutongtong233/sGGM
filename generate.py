import numpy as np

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
    print("ground truth")
    print(prec_mat.round(3))
    # reorder the cov_mat
    
    reorder = np.random.permutation(range(p)) # need to be recorded!
    # print(reorder)
    cov_mat_prime = cov_mat[reorder]
    cov_mat_prime = cov_mat_prime[:, reorder]  # TODO: perturb!

    return cov_mat_prime, reorder, prec_mat, X

if __name__ == "__main__":
    pass