'''This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, 
and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, 
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. 
For example, '001' is not allowed.'''

#%%
# 112
# aab
# kb 
# al 
dictionary = {1:'a',2:'b',12:'l',11:'k'}
string = '112'



# %%
dictionary = {1:'a',2:'b',12:'l',11:'k'}
dictionary[111%10]+dictionary[111%100]

# %%
num = len('1111')
div = num-1
div

# %%

#%%
num = len('1111')
div = num-1
div
