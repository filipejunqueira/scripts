import numpy as np
import pandas as pd
import scipy.stats as ss

class Condominio:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.df_condominio = pd.DataFrame()

    def add_lotes(self, csv_file):
        self.df_condominio = pd.read_csv(csv_file, sep=",", header=0, index_col=0)

    def total_area(self):
        return self.df_condominio.area.sum()

    def total_lotes(self):
        return len(self.df_condominio.index)

    def average_price(self):
        return 750

    def vgv(self):
        area = self.total_area()
        price = self.average_price()
        return area*price

def random_list(center=None, std= None, size=None, list_size=730):
    x = np.arange(0, size)
    prob = ss.norm.pdf(x, loc=center, scale=std)
    prob = prob / prob.sum()  # normalize the probabilities so their sum is 1
    prob_list = np.random.choice(x, list_size, p=prob)
    return prob_list, x, prob


