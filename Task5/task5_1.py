import numpy as np
import matplotlib.pyplot as plt

# Закомментируйте строку ниже для запуска локально
# from coin import coin, uniform_pdf, norm_pdf, expon_pdf

import scipy.stats as sps

coin = sps.bernoulli(p=0.5).rvs
uniform_pdf = sps.uniform.pdf
norm_pdf = sps.norm.pdf
expon_pdf = sps.expon.pdf


def uniform(size=1, precision=30):
    tmp = int()
    if type(size) != tuple:
        tmp = coin((size,) + (precision,))
    else:
        tmp = coin(size + (precision,))
    return (tmp @ list(map(lambda x : (2**x), range(precision - 1, -1, -1)))) / (2**precision)


def plot_uniform_density(size=200):
    grid = np.linspace(-0.25, 1.25, 500)
    sample = uniform(size)
    plt.hist(sample, bins=8, density=True, alpha=0.4)
    plt.plot(grid, uniform_pdf(grid), lw=3)
    plt.scatter(x=sample, y=[0]*len(sample), alpha=0.4)
    plt.title('Нормальное распределение')
    return plt.gcf()


def plot_uniform_different_precision(size=100):
    fig, ax = plt.subplots(figsize=(15, 3))
    fig.tight_layout()

    for i, precision in enumerate([1, 2, 3, 5, 10, 30]):
        plt.subplot(3, 2, i + 1)
        sample = uniform(size, precision)
        plt.scatter(sample, np.zeros(size), alpha=0.4)
        plt.yticks([])
        if i < 4:
            plt.xticks([])
        fig.suptitle('Значение случайных величин в зависимости от precision')
    return plt.gcf()


def normal(size=1, loc=0, scale=1, precision=30):
    first = uniform(size, precision)
    second = uniform(size, precision)
    return loc + np.sqrt(np.log(first) * -2) * scale * np.cos(second * 2 * np.pi)


def plot_normal_density(size=200):
    sample = normal(size)
    grid = np.linspace(-3, 3, 600)
    plt.figure(figsize=(10, 5))
    plt.scatter(y=np.zeros(size), x=sample, alpha=0.4)
    plt.hist(sample, alpha=0.4, bins=8, density=True)
    plt.plot(grid, norm_pdf(grid))
    plt.title('Плотность нормального распределения')
    return plt.gcf()


def expon(size=1, lambd=1, precision=30):
    return np.log(uniform(size=size, precision=precision)) * -1 / lambd


def plot_expon_density(size=100):
    grid = np.linspace(-0.5, 5, 500)
    sample = expon(size=size, lambd=1)
    plt.figure(figsize=(10, 5))
    plt.scatter(y=np.zeros(size), x=sample, alpha=0.4)
    plt.plot(grid, expon_pdf(grid))
    plt.hist(sample, bins=8, alpha=0.4, density=True)
    plt.title('Плотность экспоненциального распределения')
    return plt.gcf()
