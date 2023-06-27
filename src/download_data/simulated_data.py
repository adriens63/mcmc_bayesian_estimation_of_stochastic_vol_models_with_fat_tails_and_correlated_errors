from scipy import stats
import numpy as np








# ********************* simulate data from a particular svm ***************


def simulate_data(T: int, alpha: float = -0.368, delta: float = 0.95, sigma_nu: float = 0.26, burnin = 50):
    epsilon = stats.norm.rvs(size = T)
    v = stats.norm.rvs(size = T)
    log_h = [0]
    for t in range(1,T):
     log_h.append(alpha + delta*log_h[-1] + sigma_nu*v[t])

    log_h = np.array(log_h)

    y = np.exp(log_h/2) * epsilon

    return y[burnin:]