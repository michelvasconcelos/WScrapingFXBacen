import pandas as pd



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


