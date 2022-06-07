import numpy as np

# 1-2-3-4-5...-p
def generate_line(n, p):
    prec_mat = np.eye(p)
    for i in range(p-1):
        prec_mat[i][i+1] = prec_mat[i+1][i] = 0.3
    cov_mat = np.linalg.inv(prec_mat)
    X = np.random.multivariate_normal(mean=np.zeros((1, p))[0], cov=cov_mat, size=n, check_valid='ignore', tol=0.1)
    return cov_mat, prec_mat, X

def generate_line_perturb(n, p):
    cov_mat, prec_mat, X = generate_line(n, p)
    # reorder the cov_mat
    reorder = np.random.permutation(range(p)) # need to be recorded!
    cov_mat_prime = cov_mat[reorder][:]  
    return cov_mat_prime, prec_mat, X

if __name__ == "__main__":
    generate_line_perturb(10, 5)