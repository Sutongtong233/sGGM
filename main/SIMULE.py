from re import A
import numpy as np
from pulp import *
import sys
sys.path.append('.')
from generate import *
    

def SIMULE(X_ls, epsilon, lamb_n):
    '''
    params: sample list for K tasks
    return: Omega list for K+1, K task-specific and 1 shared
    ''' 
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
    # for j-th column of Omega
    Omega_ls = [np.zeros([p, p]) for i in range(K+1)]
    
    for j in range(p):
        bj = np.zeros([p, 1])
        bj[j] = 1
        problem = LpProblem("SIMULE", LpMinimize)
        u = LpVariable.dicts("u", range(p*(K+1)), lowBound = 0)
        # print(list(u.values()))
        # theta = LpVariable.dicts("theta", range(p*(K+1)), lowBound = [-val for val in list(u.values())], upBound = list(u.values()))
        theta = []
        for i in range(p*(K+1)):
            theta.append(LpVariable("theta_{}".format(i)))
        objective = lpSum(u[j]for j in range(p*(K+1)))
        problem += objective, "minimize sum of slack variable u"  # objective function
        for i in range(p*(K+1)):
            problem += theta[i] - u[i] <= 0, "constraint_0_{}".format(i)
            problem += -theta[i] - u[i] <= 0, "constraint_1_{}".format(i)
        for task_id in range(K):
            for dim_id in range(p):
                problem += lpSum(-A_ls[task_id][dim_id][k] * theta[k] for k in range(p*(K+1))) + bj[dim_id] - lamb_n <= 0, "constraint_2_{}_{}".format(task_id, dim_id)
                problem += -lpSum(-A_ls[task_id][dim_id][k] * theta[k] for k in range(p*(K+1))) + bj[dim_id] - lamb_n <= 0, "constraint 3_{}_{}".format(task_id, dim_id)

        problem.solve()

        # print(problem.constraints)
        # print(problem.objective)
        for i in problem.variables():
            print(i.name, i.varValue)

        theta_result = np.zeros([p*(K+1), 1])
        for item in problem.variables():
            if item.name.startswith("theta"):
                true_id = int(item.name.split("_")[-1])
                theta_result[true_id] = item.varValue
        for i in range(K):
            Omega_ls[i][:, j] = theta_result[i*p:(i+1)*p][:, 0]
        Omega_ls[K][:, j] = theta_result[-p:][:, 0]
    return Omega_ls
        

if __name__ == "__main__":
    prec_ls, X_ls = generate_multi_graph(10, 5, 2, 0.1)
    Omega_ls = SIMULE(X_ls, 1, 0)    

    print(Omega_ls[0])
    print(prec_ls[0])
    print(Omega_ls[1])
    print(prec_ls[1])
    print(Omega_ls[2])



    

