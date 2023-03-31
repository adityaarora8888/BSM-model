#!/usr/bin/env python
# coding: utf-8

# # Black-Scholes-Merton Model in Python
# 
# 

# In[15]:


import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt
N = norm.cdf


# In[16]:


def BSM_call_price(S, K , T , r , sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma * np.sqrt(T)) 
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T) * N(d2) 


# In[86]:


def BSM_put_price(S, K , T , r , sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r*T) * N(-d2) - S * N(-d1)


# Checking the model through a graph
# 
# As the price increase, the price of call increases and the price of put decreases. As shown through the graph

# In[87]:


K = 50
r = 0.2
T = 1
sigma = 0.5

S = np.arange(50,75) 



calls = []
for s in S: 
  x = BSM_call_price(s, K , T , r ,sigma)
  calls.append(x)

puts = []
for s in S: 
  x = BSM_put_price(s, K , T , r ,sigma)
  puts.append(x)

plt.plot(S,calls, label = 'Call Price')
plt.plot(S,puts, label = 'Put Price')
plt.xlabel('Stock Price')
plt.ylabel('Option Price')
plt.title('Black-Scholes-Merton Model')
plt.legend()


# # CHECKING THE PRICE OF OPTIONS OF GOOGLE THROUGH THE MODEL

# In[18]:


import yfinance as yf


# In[70]:


Google= yf.Ticker('GOOG')
Google.options


# In[71]:


option = Google.option_chain('2023-04-06')
option
calls = option.calls

calls[calls['strike'].between(98,101)]


# In[78]:


Google2 = yf.download('GOOG', start = '2023-01-01', end = '2023-03-30')


# Determining the annualized standard deviation

# In[79]:


Google2['pct_change'] = Google2.Close.pct_change()
Google2['log_return'] = np.log(1 + Google2['pct_change'])
std = Google2['log_return'].std()
annualized_sigma = std * np.sqrt(252)
annualized_sigma


# # Determining the call price

# In[90]:


BSM_call_price(101.32,100,0.023,0.0374,annualized_sigma)


# In[84]:


option_put = Google.option_chain('2023-04-06')
option_put
puts = option.puts
puts[puts['strike'].between(105,110)]


# # Determining the put price

# In[85]:


BSM_put_price(101.32,110,0.023,0.0374,annualized_sigma)`


# In[ ]:




