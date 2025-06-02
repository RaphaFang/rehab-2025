import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person.drop_duplicates('email',keep='first',inplace=True)


#     person.sort_values(by='id').drop_duplicates(subset='email',keep='first',inplace=True)
# 你其實是對 sort_values() 的結果做 drop_duplicates(...)，
# 這個結果並沒有被儲存回 person，也無法 in-place 修改原始 person（因為是臨時物件）。