import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure


class YouTube2:
    def __init__(
            self,
            trends_df_path: str="RUvideos_short.csv",
            categories_df_path: str="RU_category_id.json"
    ):
        self.trends_df = pd.read_csv('RUvideos_short.csv', sep=',', parse_dates=['trending_date'], dayfirst=True)
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'], format='%y.%d.%m')
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df.trending_date)

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )
        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        return self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')

    def task2(self) -> pd.DataFrame:
        new_df = self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')
        return pd.pivot_table(new_df, columns='trending_date', values='views', index='name', aggfunc=np.sum)

    def task3(self) -> Figure:
        new_df = self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')
        result_table = pd.pivot_table(new_df, columns='trending_date', values='views', index='name', aggfunc=np.sum).div(1000000)
        sns.heatmap(result_table, cmap= 'coolwarm', annot=True, fmt='.1f')
        plt.title("Тепловая карта просмотров")
        plt.xlabel('Дата')
        plt.ylabel('Категория')
        return plt.gcf()

    def task4(self) -> pd.DataFrame:
        new_df = self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')
        result_table = pd.pivot_table(new_df, columns='trending_date', values='views', index='name', aggfunc=np.sum)
        result_table['Всего просмотров'] = result_table.sum(axis=1)
        result_table.loc['Всего просмотров'] = result_table.sum()
        return result_table

    def task5(self) -> Figure:
        new_df = self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')
        result_table = pd.pivot_table(new_df, columns='trending_date', values='views', index='name', aggfunc=np.sum).div(1000000)
        result_table['Всего просмотров'] = result_table.sum(axis=1)
        result_table.loc['Всего просмотров'] = result_table.sum()
        sns.heatmap(result_table, annot=True, fmt='.2f', vmax=True, linewidths=.5)
        plt.title("Тепловая карта просмотров")
        plt.xlabel('Дата')
        plt.ylabel('Категория')
        return plt.gcf()
