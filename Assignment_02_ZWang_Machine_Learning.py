## part 1 of Assignment week2: Recode the house-price machine learning

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

def loss(y, y_hat):  # loss function 1,
    return sum((y_i - y_hat_i)**2 for y_i, y_hat_i in zip(list(y), list(y_hat)))/ len(list(y))

def loss2(y,y_hat): # try for a different Loss function
    return sum(abs(y_i - y_hat_i) for y_i, y_hat_i in zip(list(y),list(y_hat))) / len(list(y))

## 1. Random Choose Method to get optimal k and b
trying_times = 20000
min_loss = float('inf')
best_k, best_b = None, None
for i in range(trying_times):
    k = random.random() * 200 - 100
    b = random.random() * 200 - 100
    price_by_random_k_and_b = [price(r,k,b) for r in x_rm]
    current_loss = loss2(y, price_by_random_k_and_b)
    if current_loss < min_loss:
        min_loss = current_loss
        best_k, best_b = k, b
        print ('When time is : {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b, min_loss))
price_by_random_k_and_b_best = [price(r,best_k,best_b) for r in x_rm]
plt.scatter(x_rm,price_by_random_k_and_b_best) # plot according to the first method: random_generation
plt.scatter(x[:, 5], y) # plot according to the data
plt.savefig('method1.png')

## 2. Second Method: Supervised Direction to get optional k and b
trying_times = 20000
min_loss = float('inf')
best_k = random.random() * 200 - 100
best_b = random.random() * 200 - 100
direction = [(+1,-1),(+1,+1),(-1,+1),(-1,-1)] #first element: k's changing direction, second element: b's changing direction
next_direction = random.choice(direction)
scalar = 0.1
update_time = 0
for i in range(trying_times):
    k_direction, b_direction = next_direction
    current_k, current_b = best_k + k_direction * scalar, best_b + b_direction * scalar
    price_by_k_and_b = [price(r,current_k, current_b) for r in x_rm]
    current_loss = loss2(y, price_by_k_and_b)
    if current_loss < min_loss:
        min_loss = current_loss
        best_k, best_b = current_k, current_b
        next_direction = next_direction
        update_time +=1
        if update_time % 10 == 0:
            print ('2. When time is: {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b,min_loss))
    else:
        next_direction = random.choice(direction)
plt.scatter(x_rm,[price(r,current_k,current_b) for r in x_rm]) # plot according to the second method: direction adjusting
plt.scatter(x[:, 5], y) # plot according to the data
plt.savefig('method2.png')


# 3. Gradient Descent to get optimal k and b
def partial_k(x, y, y_hat):
    n = len(y)
    gradient = 0
    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        gradient += (y_i - y_hat_i) * x_i
    return -2 / n * gradient

def partial_b(x, y, y_hat):
    n = len(y)
    gradient = 0
    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        gradient += (y_i - y_hat_i)
    return -2 / n * gradient

trying_times = 20000
min_loss = float('inf')
import random
current_k = random.random() * 100
current_b = random.random() * 200 - 100
learning_rate_big = 1e-2
learning_rate_small = 1e-4
for i in range(trying_times):
    price_by_k_b_partial = [price(r, current_k, current_b) for r in x_rm]
    current_loss = loss(y, price_by_k_b_partial)
    if current_loss < min_loss:
        min_loss = current_loss
    if i%50 == 0:
        print(
            '3. When time is: {} get best_k: {} best_b: {}, and the loss is: {}'.format(i, current_k, current_b, min_loss))
    k_gradient = partial_k(x_rm, y, price_by_k_b_partial)
    b_gradient = partial_b(x_rm, y, price_by_k_b_partial)
    if current_loss <5:
        current_k = current_k + (-1 * k_gradient) * learning_rate_small
        current_b = current_b + (-1 * b_gradient) * learning_rate_small
    else:
        current_k = current_k + (-1 * k_gradient) * learning_rate_big
        current_b = current_b + (-1 * b_gradient) * learning_rate_big

plt.scatter(x_rm,[price(r,current_k,current_b) for r in x_rm]) # plot according to the third method
plt.scatter(x[:, 5], y) # plot according to the data
plt.savefig('method3.png')




