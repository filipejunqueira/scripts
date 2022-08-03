import numpy as np

class Fluxo_de_caixa():

    def __init__(self, tempo=1, capital = 10000, taxa = 0.1):
        self.tempo = tempo
        self.capital = capital
        self.taxa = taxa

    def flux(self,cupom=0):
        self.cupom = cupom
        self.size = self.tempo * 12 + 1
        f_caixa = np.zeros((self.size,), dtype=np.float128)
        f_caixa[0] = self.capital
        taxa_mensal = pow((1 + self.taxa), 1 / 12) - 1

        for m in range(1, self.tempo * 12 + 1):
            f_caixa[m] = f_caixa[m - 1] * (1 + taxa_mensal) - self.cupom

        return f_caixa

# income que zera


    def renda(self, chute=1, final=0 , tolerancia=0.1, lr = 0.1):

        f_renda = self.flux()
        renda_var = self.cupom + chute
        i = 0

        if self.capital < final:

            while f_renda[self.size - 1] <= final + tolerancia:
                i += 1
                renda_var = renda_var * (lr + 1)
                f_renda = self.flux(cupom=renda_var)
                print(f"Renda = {renda_var}, it = {i}")

                if f_renda[self.size - 1] > (0 + final):
                    factor = 10
                    print(f"Reducing learning rate by a factor of {factor}")
                    renda_var = renda_var * (1 / (lr + 1))
                    f_renda = self.flux(cupom=renda_var)
                    print(f"Renda = {renda_var}, it = {i}")
                    lr = lr / factor

        else:

            while f_renda[self.size-1] >= final + tolerancia:
                i += 1
                renda_var = renda_var*(lr+1)
                f_renda = self.flux(cupom=renda_var)
                print(f"Renda = {renda_var}, it = {i}")

                if f_renda[self.size-1] <  (0 + final):
                    factor = 10
                    print(f"Reducing learning rate by a factor of {factor}")
                    renda_var = renda_var*(1/(lr+1))
                    f_renda = self.flux(cupom=renda_var)
                    print(f"Renda = {renda_var}, it = {i}")
                    lr = lr/factor

        return f_renda, renda_var

