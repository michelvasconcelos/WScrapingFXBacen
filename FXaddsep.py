import pandas as pd

class AddSeparator():
    def __init__(self, currency):
        self.cur_csv = r'C:\Users\miche\diretorio\WScrapingFXBacen\Cotacoes' + currency + '2022.csv'
        self.readfile_df = pd.read_csv(self.cur_csv, sep= ';')
        self.currency = currency

    def addSep(self):
        for i in self.readfile_df.index:
            dt = str(self.readfile_df['Data'][i])[:-6] + '/' + str(self.readfile_df['Data'][i])[-6:-4] + '/' + str(self.readfile_df['Data'][i])[-4:]
            #dt = f"{str(self.readfile_df['Data'][i])[:-6]}/{str(self.readfile_df['Data'][i])[-6:-4]}/{str(self.readfile_df['Data'][i])[-4:]}"
            self.readfile_df.loc[i, 'Data'] = dt
            self.readfile_df.to_csv(f'./Cotacoes{self.currency}2022 v1.csv', sep= ';', index= False)
        return print("Separadores de data adicionados ao arquivo.")
#print(readfile_df)

#AddSeparator('Euro').addSep()
