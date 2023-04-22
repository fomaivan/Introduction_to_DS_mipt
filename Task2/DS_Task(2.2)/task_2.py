from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp


class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv('RUvideos_short.csv', sep=',', parse_dates=['trending_date'], dayfirst=True)
        self.df['trending_date'] = pd.to_datetime(self.df['trending_date'], format='%y.%d.%m')
        self.df['trending_date'] = pd.to_datetime(self.df.trending_date)

    def task1(self) -> pd.DataFrame:
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df.drop(columns=['video_id', 'title', 'channel_title', 'tags', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description', 'publish_time'], inplace=True)
        self.df['trending_date'] = self.df['trending_date'].dt.day
        return self.df

    def task3(self) -> Figure:
        sns.boxplot(data=self.df, y='views', x='trending_date')
        plt.xlabel('Дни')
        plt.ylabel('Просмотры')
        plt.title('Аналитика просмотров по дням')
        plt.ylim(5000)
        return plt.gcf()

    def task4(self) -> Figure:
        with sns.axes_style('darkgrid'):
            sns.boxplot(data=self.df, y='views', x='trending_date')
            plt.ylim((-5, 800000))
            plt.xlabel('Дни')
            plt.ylabel('Просмотры')
            plt.title('Аналитика просмотров по дням')
        return plt.gcf()

    def task5(self) -> Figure:
        with sns.axes_style('darkgrid'):
            sns.jointplot(data=self.df, x='views', y='likes', alpha=0.5)
            plt.ylim((-5, 500000))
            plt.title('Совместное распределение')
            plt.xlabel('Просмотры')
            plt.ylabel('Лайки')
        return plt.gcf()

    def task6(self) -> Figure:
        with sns.axes_style('darkgrid'):
            new_df = self.df[self.df['views'] < 300000][self.df['likes'] < 10000]
            sns.jointplot(data=new_df, x='views', y='likes', alpha=0.5)
            plt.title('Совместное распределение')
            plt.xlabel('Просмотры')
            plt.ylabel('Лайки')
        return plt.gcf()
