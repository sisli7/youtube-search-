import re 
from youtube_search import YoutubeSearch
import pandas as pd 
results =YoutubeSearch('food',max_results=40).to_dict()
df = pd.DataFrame(results)
print(df)
k =1 
for i in results:
    i['thumbnails']= []
    print(k,i)
    k = k+1 

df.to_csv('food.csv',index=False,encoding='utf-8')

#search with fish word
# new_result=re.search(r'fish',df)
# print(new_result)