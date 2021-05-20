#!/usr/bin/env python
# coding: utf-8

# #Versão da linguagem python
# from platform import python_version
# print ('Versão da linguagem python usada neste jupyter notebook é: ', python_version())

# In[13]:


#para atualizar um pacote, execute o comando abaixo no terminal ou no prompt de comando:
#pip install -U nome_pacote

#Para instalar a versão exata de um pacote, exccute o comando abaixo no terminal ou no prompt de comando:
# !pip install nome_pacote==versao_desejada

#depois de instalar ou atualizar o pacote, reinicie o jupyter notebook

#Instalar marca d'agua
#esse pacote é usado para gravar as versões de outros pacotes neste jupyter notebook
get_ipython().system('pip install -q -U watermark')


# In[5]:


# importando as bibliotecas necessárias para o projeto 
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# In[6]:


# Versões dos pacotes usados neste jupyter notebook
get_ipython().run_line_magic('reload_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-a "NatáliaOliveira-DS" --iversions')


# In[8]:


#carregando dados
dadosRH = pd.read_csv('dadosRH.csv')


# In[9]:


dadosRH.head()


# In[18]:


dadosRH.shape


# In[19]:


#limpeza e transformação de Dados

#para verificar se há valores nulos - a 1a função isnull mostrara para cada linha se sim ou não, mas nosso dataset pe muito grande, então usando a função sum para somar
dadosRH.isnull().sum()


# In[20]:


#fazer um agrupamento com a função groupyby, mas nesse caso pela coluna educação e depois a contagem
#mas desse jeito ele não considera o numeros os valores ausentes
dadosRH.groupby(['educacao']).count()


# In[22]:


#grafico para os dados acima
sns.countplot(dadosRH['educacao'])


# In[23]:


#fazer um agrupamento com a função groupyby, mas nesse caso pela coluna aval ano anterior e depois a contagem
#mas desse jeito ele não considera o numeros os valores ausentes
dadosRH.groupby(['aval_ano_anterior']).count()


# In[24]:


#grafico para os dados acima
sns.countplot(dadosRH['aval_ano_anterior'])


# In[25]:


#imputação para preencher os valores ausentes
#para preencher os valores ausentes na educação, usaremos o critério moda
#vou pegar minha base_fillna vou preencher com_calcular a moda_retornarei o maior valor, então farei o inplace para salvar o resultado na propria tabela
dadosRH['educacao'].fillna(dadosRH['educacao'].mode()[0], inplace = True)


# In[26]:


sns.countplot(dadosRH['educacao'])


# In[27]:


dadosRH.groupby(['educacao']).count()


# In[28]:


#imputação para preencher os valores ausentes
#para preencher os valores ausentes na aval, usaremos o critério mediana (pq não é afetada pelo valores ausentes)
#vou pegar minha base_fillna vou preencher com_calcular a moda_retornarei o maior valor, então farei o inplace para salvar o resultado na propria tabela
dadosRH['aval_ano_anterior'].fillna(dadosRH['aval_ano_anterior'].median(), inplace = True)


# In[29]:


dadosRH.groupby(['aval_ano_anterior']).count()


# In[30]:


sns.countplot(dadosRH['aval_ano_anterior'])


# In[31]:


dadosRH.isnull().sum()


# In[10]:


#Vamos verificar o balanceamento de classe na variável "promovido".
dadosRH.groupby(['promovido']).count()


# In[11]:


sns.countplot(dadosRH['promovido'])


# In[ ]:


#aplicando tecnica para resolver o problema de desbalanceamento da classe (no nosso caso um maior volume em 0 do que em 1 e isso para uma aplicação em machine learning poderia comprometer os resultados)


# In[14]:


#separando a classe majoritaria da minoritaria
df_classe_majoritaria = dadosRH[dadosRH.promovido==0]
df_classe_minoritaria = dadosRH[dadosRH.promovido==1]


# In[15]:


df_classe_majoritaria.shape


# In[17]:


df_classe_minoritaria.shape


# In[18]:


#aplicando tecnica UPSAMPLE para equilibrar os dois valores ao inves de deletar itens da classe 0, vamos adicionar na classe 1
#sklearn é um pacote para machine leaning que tem funções para pré processamento de dados
#dentre elas a RESAMPLE que faz reamostragem
from sklearn.utils import resample
df_classe_minoritaria_upsampled = resample(df_classe_minoritaria,
                                          replace = True,
                                          n_samples = 50140,
                                          random_state = 150)


# In[19]:


#para verificar se deu certo, concatenamos a classe majoritaria com a minoritaria
dadosRH_balanceados = pd.concat([df_classe_majoritaria, df_classe_minoritaria_upsampled])


# In[20]:


dadosRH_balanceados.promovido.value_counts()


# In[21]:


sns.countplot(dadosRH_balanceados['promovido'])


# In[22]:


#os dados estao balanceados, agora serao salvos em disco o dataset manipulado
dadosRH_balanceados.to_csv('dadosRH_modificado_v1.csv', encoding = 'utf-8', index = False)


# In[7]:


#agora carregaremos o novo dataset
#em conjunto com o power bi
dataset = pd.read_csv('dadosRH_modificado_v1.csv')
dataset.head()


# In[26]:


dataset.shape


# ### Pergunta 1 - Qual a Correlação Entre os Atributos dos Funcionários?

# In[34]:


#criamos uma matriz de correlação e usaremos um mapa de calor para poder visualizar essa correção
import matplotlib.pyplot as plt
import seaborn as sns
corr = dataset.corr()
sns.heatmap(corr, cmap = "RdPu", linewidths = 0.2)
plt.show()


# ### Pergunta 2 - Qual o tempo de serviço da maioria dos funcionários?

# In[36]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(dataset['tempo_servico'], color = 'purple')
plt.title('Distribuição de Tempo de Serviço dos Funcionários', fontsize = 15)
plt.xlabel("Tempo de Serviço em Anos", fontsize = 13)
plt.ylabel("Total", fontsize = 13)
plt.show()


# ### Pergunta 3 - Qual avaliação do ano anterior foi mais comum?

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
dataset['aval_ano_anterior'].value_counts().sort_values().plot.bar(color = 'lightpink', figsize = (10, 5))
plt.title('Distribuição da Avaliação do Ano Anterior dos Funcionários', fontsize = 15)
plt.xlabel('Avaliações', fontsize = 13)
plt.ylabel('Total')
plt.show()


# ### Pergunta 4 - Qual a Distribuição das Idades dos Funcionários?

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(dataset['idade'], color = 'magenta')
plt.title('Distribuição da Idade dos Funcionários', fontsize = 15)
plt.xlabel('Idade', fontsize = 13)
plt.ylabel('Total', fontsize = 13)
plt.show()


# ### Pergunta 5 - Qual o Número de Treinamentos Mais Frequente?

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.violinplot(dataset['numero_treinamentos'], color = 'violet')
plt.title('Número de Treinamentos Feitos Pelos Funcionários', fontsize = 15)
plt.xlabel('Número de Treinamentos', fontsize = 13)
plt.ylabel('Frequência', fontsize = 13)
plt.show()


# ### Pergunta 6 - Qual a Proporção dos Funcionários Por Canal de Recrutamento?

# In[12]:


dataset['canal_recrutamento'].value_counts()


# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns
dataset['canal_recrutamento'].value_counts()
fatias = [55375, 42358, 2547]
labels = "Outro", "Outsourcing", "Indicação"
colors = ['violet', 'purple', 'magenta']
explode = [0, 0, 0]
plt.pie(fatias, labels = labels, colors = colors, explode = explode, shadow = True, autopct = "%.2f%%")
plt.title('Percentual de Funcionários Por Canal de Recrutamento', fontsize = 15)
plt.axis('off')
plt.legend()
plt.show()


# In[ ]:


### Pergunta 7 - Qual a Relação Entre a Promoção e a Avaliação do Ano Anterior?


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns
data = pd.crosstab(dataset['aval_ano_anterior'], dataset['promovido'])
data.div(data.sum(1).astype(float), axis = 0).plot(kind = 'bar', 
                                                   stacked = True, 
                                                   figsize = (16, 9), 
                                                   color = ['purple', 'violet'])
plt.title('Relação Entre Avaliação do Ano Anterior e a Promoção', fontsize = 15)
plt.xlabel('Avaliação do Ano Anterior', fontsize = 13)
plt.legend()
plt.show()


# In[ ]:




