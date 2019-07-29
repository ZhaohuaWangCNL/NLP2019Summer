
## get data
from sklearn.datasets import load_boston
data = load_boston()
x,y = data['data'],data['target']
x_rm = x[:, 5]
def price(rm, k, b):
    """f(x) = k * x + b"""
    return k * rm + b

import matplotlib.pyplot as plt
import random

def loss(y,y_hat): # try for MAE Loss function
    return sum(abs(y_i - y_hat_i) for y_i, y_hat_i in zip(list(y),list(y_hat))) / len(list(y))

# Gradient Descent to get optimal k and b
def partial_k(x, y, y_hat):
    n = len(y)
    gradient = 0
    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        if y_i > y_hat_i:
            gradient += -1 * x_i
        else:
            gradient += x_i
    return -1 / n * gradient


def partial_b(y,y_hat):
    n = len(y)
    gradient = 0
    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        if y_i > y_hat_i:
            gradient += - 1
        if y_i < y_hat_i:
            gradient += 1
    return -1 / n * gradient

trying_times = 20000
min_loss = float('inf')
current_k = random.random() * 200 - 100
current_b = random.random() * 200 - 100
learning_rate = 1e-2
for i in range(trying_times):
    price_by_k_b_partial = [price(r, current_k, current_b) for r in x_rm]
    current_loss = loss(y, price_by_k_b_partial)
    if current_loss < min_loss:
        min_loss = current_loss
    if i%50 == 0:
        print(
            'When time is: {} get best_k: {} best_b: {}, and the loss is: {}'.format(i, current_k, current_b, min_loss))
    k_gradient = partial_k(x_rm, y, price_by_k_b_partial)
    b_gradient = partial_b(y, price_by_k_b_partial)
    current_k = current_k + (-1 * k_gradient) * learning_rate
    current_b = current_b + (-1 * b_gradient) * learning_rate
plt.scatter(x_rm,[price(r,current_k,current_b) for r in x_rm]) # plot according to the third method
plt.scatter(x[:, 5], y) # plot according to the data
plt.savefig('method3.png')


