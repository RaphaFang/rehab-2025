SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;


-- LENGTH 是計算全部的符號，所以空格，特別符號都會算