import pandas as pd
import os
from datetime import datetime, timedelta

url_download = "/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=08/02/2022&DATAFIM=07/03/2022"
url_base = url_download.split('ChkMoeda')[0]

if os.path.isfile('./CotacoesEuro2022.csv'):
    #print('File exist')
    cur_csv = r'C:\Users\miche\diretorio\WScrapingFXBacen\CotacoesEuro2022.csv'
    readfile_df = pd.read_csv(cur_csv, header= None, sep= ';')
    """Converter datas para date time antes de manipular"""
    last_date = readfile_df[0].tail(1)
    #date = str(last_date.iloc[-1])[:-6] + '/' + str(last_date.iloc[-1])[-6:-4] + '/' + str(last_date.iloc[-1])[-4:]
    dt_inicio = f"{str(last_date.iloc[-1])[:-6]}/{str(last_date.iloc[-1])[-6:-4]}/{str(last_date.iloc[-1])[-4:]}"
    dt_inicio = datetime.strptime(dt_inicio, '%d/%m/%Y') + timedelta(1)
    dt_final = datetime.strftime(datetime.now() - timedelta(1), '%d/%m/%Y')
    """Tirar horario da data inicio"""
    #currency = input('Digite o código da moeda (USD: 61 ou EUR: 222): ')
    #cur_csv = f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}'

    print(dt_inicio)
    """Buscar tail da coluna '0' adicionar 1 dia. Para isso, antes converter datas com Datetime"""
else:
    print('File does not exist')

url_download = "/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=08/02/2022&DATAFIM=07/03/2022"
url_base = url_download.split('ChkMoeda')[0]
currency = input('Digite o código da moeda (USD: 61 ou EUR: 222): ')
dt_inicio = input('Digite a data inicial (dd/mm/aaaa): ')
dt_final = input('Digite a data final (dd/mm/aaaa): ')
#print(f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}')
cur_csv = f'https://ptax.bcb.gov.br{url_base}ChkMoeda={currency}&DATAINI={dt_inicio}&DATAFIM={dt_final}'
readfile_df = pd.read_csv(cur_csv, header= None, sep= ';')
print(readfile_df)



"""Próximos passos"""
"""1- verificar se há base existente 'CotacoesEuro2022' """
"""2- criar base manualmente"""
"""3- rodar script todo e colar dados adicionais na base"""
"""4- Usar datetime para converter para data (DATETIME) e buscar link a partir da próxima data"""
"""Usar tail na coluna para identificar ultima data extraída"""


