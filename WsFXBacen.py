import pandas as pd
import os
from datetime import datetime, timedelta
from FXaddsep import AddSeparator

url_download = "/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=08/02/2022&DATAFIM=07/03/2022"
url_base = url_download.split('ChkMoeda')[0]
currency = input('Digite o código da moeda (USD: 61 ou EUR: 222): ')
if currency == '222':
    curr_name = 'Euro'
elif currency == '61':
    curr_name = 'Dolar'

if os.path.isfile(f'./Cotacoes{curr_name}2022.csv'):
    cur_csv = r'C:\Users\miche\diretorio\WScrapingFXBacen\Cotacoes' + curr_name + '2022.csv'
    readfile_df = pd.read_csv(cur_csv, header= None, sep= ';')
    """Converter datas para date time antes de manipular"""
    last_date = readfile_df[0].tail(1)
    #date = str(last_date.iloc[-1])[:-6] + '/' + str(last_date.iloc[-1])[-6:-4] + '/' + str(last_date.iloc[-1])[-4:]
    dt_inicio = f"{str(last_date.iloc[-1])[:-6]}/{str(last_date.iloc[-1])[-6:-4]}/{str(last_date.iloc[-1])[-4:]}"
    dt_inicio = datetime.strptime(dt_inicio, '%d/%m/%Y') + timedelta(1)
    dt_inicio = str(dt_inicio)[:-9]
    dt_inicio = f"{dt_inicio[8:]}/{dt_inicio[5:7]}/{dt_inicio[:4]}"
    dt_final = datetime.strftime(datetime.now() - timedelta(1), '%d/%m/%Y')
    cur_csvnew = f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}'
    readnewfile_df = pd.read_csv(cur_csvnew, header= None, sep= ';')
    readnewfile_df.to_csv(f'./Cotacoes{curr_name}2022.csv', mode= 'a', sep= ';', index= False, header= False)

    """Próximo passo criar .csv caso ele não exista"""
    """Passo seguinte criar 'temporizador para rodar o código todo dia após determinada hora"""
else:
    dt_inicio = input('Digite a data inicial (dd/mm/aaaa): ')
    dt_final = input('Digite a data final (dd/mm/aaaa): ')
    cur_csvnew = f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}'
    print(cur_csvnew)
    readnewfile_df = pd.read_csv(cur_csvnew, header= None, sep= ';', names= ['Data', 'Codigo da moeda', 'Nao sei', 'Moeda', 'Taxa compra', 'Taxa venda', 'Paridade dolar compra', 'Paridade dolar venda'])
    readnewfile_df.to_csv(f'./Cotacoes{curr_name}2022.csv', sep= ';', index= False, header= True)

AddSeparator(curr_name).addSep()
    
    
    #print('File does not exist')

#url_download = "/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=08/02/2022&DATAFIM=07/03/2022"
#url_base = url_download.split('ChkMoeda')[0]
#currency = input('Digite o código da moeda (USD: 61 ou EUR: 222): ')
##print(f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}')
#cur_csv = f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}'
#readfile_df = pd.read_csv(cur_csv, header= None, sep= ';')
#print(readfile_df)


