import pandas as pd

# ref:
# https://towardsdatascience.com/how-to-get-the-row-count-of-a-pandas-dataframe-be67232ad5de
#


class FileLoader():

    def __init__(self) -> None:
        pass

    def load(self, path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions",
              len(df.index), "x", len(df.columns))
        return df

    def display(self, df, n):
        if (n < 0):
            print(df.tail(abs(n)))
        else:
            print(df.head(n))


if __name__ == "__main__":
    loader = FileLoader()
    # data got from:
    # https://www.kaggle.com/datasets/wenruliu/adult-income-dataset?resource=download
    data = loader.load("../data/adult_data.csv")

    loader.display(data, 12)
