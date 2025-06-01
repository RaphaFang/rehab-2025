import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by='user_id')
    # 這邊也不用選定回吐什麼，整張表給他


# 下面這作法很不直覺
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str[0].str.upper() + users["name"].str[1:].str.lower()
    return users[["user_id", "name"]].sort_values(by='user_id')

# 為什麼需要.str
# 是因為這些函數都是在str屬性底下，所以一定要掛str才能呼叫