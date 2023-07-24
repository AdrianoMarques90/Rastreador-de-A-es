import yfinance as yf
import matplotlib.pyplot as plt

acoes = ['AAPL', 'MFST', 'PETR4.SA', 'BBDC4.SA' ]

dados_acoes = yf.download( acoes,
                          period='1d',
                           start='2022-01-01')

dados_acoes['Close'].plot()
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Rastreador de Ações do Mauriçoca')
plt.legend(acoes, fontsize=7)
plt.show()

dados_normalizados = dados_acoes['Close'] / dados_acoes['Close'].iloc[0]
dados_normalizados.plot()
plt.xlabel('Data')
plt.ylabel("Preço Normalizado")
plt.title('Rastreador de Ações do Mauriçoca')
plt.legend(acoes, fontsize=7)
plt.show()