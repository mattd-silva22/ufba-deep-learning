
import re
import pandas as pd
import seaborn as sns

def getScore(score) :
    if score <= 2:
        return 'bad'
    elif score == 3:
        return 'neutral'
    else:
        return 'good'


def getFormatedData(path):
    rawdata = pd.read_csv(path)
    rawdata.drop(columns=["review_id", "order_id", "review_creation_date", "review_answer_timestamp"], inplace=True)
    rawdata = rawdata.rename(columns={
        "review_comment_title" : "title", 
        "review_comment_message" : "review", 
        "review_score" : "score"
        })
    rawdata["score"] = rawdata["score"].apply(getScore)
    rawdata["review"].fillna(rawdata['title'])
    rawdata.drop(columns=["title"], inplace=True)
    rawdata.dropna(subset=["review"], inplace=True)

    rawdata["review"].apply(lambda x: re.sub(r'<.*?>', '', x))
    rawdata["review"].apply(lambda x: re.sub(r'<.*?>', '', x))
    return rawdata
    
    

def main() :
    data = getFormatedData("data/olist_order_reviews_dataset.csv")
    pd.to_csv(data, index=False)
main()

