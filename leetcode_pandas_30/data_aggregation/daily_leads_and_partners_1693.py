import pandas as pd

data = {
    "date_id": [
        "2020-12-8", "2020-12-8", "2020-12-8", "2020-12-7", "2020-12-7",
        "2020-12-8", "2020-12-8", "2020-12-7", "2020-12-7", "2020-12-7"
    ],
    "make_name": [
        "toyota", "toyota", "toyota", "toyota", "toyota",
        "honda", "honda", "honda", "honda", "honda"
    ],
    "lead_id": [
        0, 1, 1, 0, 0,
        1, 2, 0, 1, 2
    ],
    "partner_id": [
        1, 0, 2, 2, 1,
        2, 1, 1, 2, 1
    ]
}

daily_sales = pd.DataFrame(data)

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (daily_sales
         .groupby(['date_id','make_name'], as_index=False)   # 如果停在這，沒有加上後續的 agg() 這時回傳出去的 type 會是 groupby type, not df
         .agg(
             unique_leads = ('lead_id', 'nunique'),
             unique_partners = ('partner_id', 'nunique')
         ).sort_values(['make_name','date_id'], ascending=False))

daily_leads_and_partners(daily_sales)
