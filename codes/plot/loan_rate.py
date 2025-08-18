from matplotlib import pyplot as plt
import numpy as np

lam = 0.5
T = np.arange(0, 10, 0.1)
r = 1 - lam * (1 - np.exp(-T / lam)) / T

plt.plot(T, r, label="Loan Rate")
plt.title("Loan Rate Over Time")
plt.xlabel("Time (years)")
plt.ylabel("Loan Rate")
plt.grid()
plt.legend()
plt.savefig("../../docs/assets/loan_rate.png")
