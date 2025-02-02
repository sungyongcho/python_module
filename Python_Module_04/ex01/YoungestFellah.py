import pandas as pd


def youngest_fellah(df, year):
    print(df.loc[df['Year'] == year].groupby(
        'Sex')['Age'].agg('min').to_dict())


#
if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    # data from:
    # https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    data = loader.load('../data/athlete_events.csv')
    youngest_fellah(data, 2004)
