# 1 - Initialization
# 1.1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
import webbrowser
import pandas_profiling

sns.set()

# 1.2
data = pd.read_csv("./data/data_subset.csv", sep=";", index_col=0)
data = data.dropna()  # retire les données manquantes
# print(data.head())


def webbroser():
    # 2 - Webbroser
    # 2.1
    df = pd.DataFrame(data, columns=['Nationality', 'Overall', 'Potential'])
    pandas_profiling.ProfileReport(df).to_file('./data/report.html')

    # 2.2
    webbrowser.open(os.getcwd()+"./data/report.html")


def variables():
    # 3 - Variables
    print(data.info())
    print(data.dtypes)


def histograms():
    # 4 - Histograms
    def overall():
        # 4.1
        sns.distplot(overall_value, hist=True, bins=13, kde=True)
        plt.show()

    def quantitative():
        quantitative_value_1 = data['Price']
        quantitative_value_2 = data['Age']
        sns.distplot(quantitative_value_1, hist=True, bins=12, kde=True)
        plt.show()
        sns.distplot(quantitative_value_2, hist=True, bins=15, kde=True)
        plt.show()

    def categorical():
        categories_value_1 = data['International Reputation']
        categories_value_2 = data['Skill Moves']
        sns.distplot(categories_value_1, hist=True, bins=27, kde=True)
        plt.show()
        sns.distplot(categories_value_2, hist=True, bins=14, kde=True)
        plt.show()

    overall_value = data['Overall']

    overall()
    quantitative()
    categorical()

    # 4.2
    # REPONDRE ORALEMENT

    # 4.3
    def value(df):
        print('Average: ', df.mean())
        print('Median: ', df.median())
        print('Ecart-type: ', df.std())
        print('Range: ', df.max())

    value(overall_value)


def countplots():
    # 5 - Countplots
    # 5.1
    print(data['Nationality'].value_counts().head(7))
    # Réponse -> England

    sns.countplot('Nationality', order=[data['Nationality'].value_counts().head(7)],
                  data=data)
    plt.show()

    # 5.2
    # displot-> 1 thème, montre la fréquence d'une seule variable, countplot=plusieurs


def countplots_2():
    # 6 - Countplots
    sns.barplot(x="Nationality",
                y="Potential",
                order=["England", "Germany", "Spain", "France", "Argentina", "Brazil", "Italy"],
                data=data)
    plt.show()
    # -> Spain


def scatterplots():
    # 7 - Scatterplot
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'England'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'Germany'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'Spain'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'France'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'Argentina'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'Brazil'],
                    y=data['Potential'])
    sns.scatterplot(x=data['Nationality'][data['Nationality'] == 'Italy'],
                    y=data['Potential'])
    plt.show()


# webbroser()
# variables()
# histograms()
# countplots()
# countplots_2()
# scatterplots()
