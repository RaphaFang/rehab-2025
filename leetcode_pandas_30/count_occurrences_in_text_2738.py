import pandas as pd

data = pd.DataFrame({
    "content": [
        "Hello world",
        "Hello Leetcode",
        "Leetcode is the best"
    ]
})

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    p = files['content'].str.lower().str.split().explode()
    print(p) # 這邊都還是序列
    
    words_df = p.value_counts().reset_index()
    print(words_df)
    
    words_df.columns = ['words', 'count']
    print(words_df)
    return words_df.sort_values(by='words').reset_index(drop=True)


count_occurrences(data)


# .str.split() 這拆開後會是list，要透過.explode() 把他變成挖出來的字
# 這時候都是壓到[content]這欄位裡面

# .reset_index()
# 讓series 變成 dataframe
# 他如果本來就沒有index不護有差

# reset_index(drop=True)
# 原本有的，你排序後舊index變亂，相重製，就加上drop