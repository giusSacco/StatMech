import numpy as np
import matplotlib.pyplot as plt

q = 1
k =1
dt = .01
n_steps = 10000
kb = 1
T = 1

def force(q):
    return -k*q
for delta in np.logspace(-3,1,5):
    trajectory = []
    acceptance_rate = 0
    q0 = 1
    E0 = k*q0**2
    for i in range(n_steps):
        # Proposed Move
        q = q0 + np.random.uniform(-delta,delta)
        E = k*q**2
        alpha = np.amin([1, np.exp(-(E-E0)/(kb*T))])
        if alpha > np.random.uniform():
            acceptance_rate += 1
            q0 = q
            E0 = k*q0**2

        trajectory.append(q0)

    plt.plot(trajectory, label = f'delta = {delta}, acc_rate = {acceptance_rate/n_steps:.2f}')
    q_sqaured =  np.array(trajectory)**2
    print(f'delta = {delta}, q^2 avg = {np.mean( q_sqaured)}, std_dev = {np.std(q_sqaured)}')
plt.legend()
plt.show()