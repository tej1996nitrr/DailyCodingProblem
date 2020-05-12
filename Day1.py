'''Given a list of numbers, return
 whether any two sums to k. For example, given [10, 15, 3, 7] 
 and k of 17, return true since 10 + 7 is 17.'''
#%%
'''METHOD=1'''
l_num = [10,15,3,7]
k=13
ans = [(l_num[x],l_num[y]) for x in range(len(l_num)) for y in range(len(l_num)) if x!=y and l_num[x]+l_num[y]==k]
if(len(ans)==0):
    print(False)
else:
    print(True)


# %%
'''METHOD 2'''
def check(array,sum):
    sol  =set()
    for num in array:
        if num in sol:
            return True

        sol.add(sum-num)
    return False

assert check([10, 15, 3, 7], 17)