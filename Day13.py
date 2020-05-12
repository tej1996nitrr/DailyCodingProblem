'''This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k 
distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".'''



#%%
# string = input("string")
# k=input("distincts")
string = "abcba"
k = 2
print(max([string[i:j]  for i in range(len(string)) for j in range (i+1,len(string)+1) if(len(set(string[i:j]))==k)],key=len))


# %%
