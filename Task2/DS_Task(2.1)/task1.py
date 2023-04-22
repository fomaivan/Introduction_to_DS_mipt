import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):  # task0
        self.df = df = pd.read_csv("cat_exam_data.csv", sep=',')

    def task1(self) -> pd.DataFrame:
        return self.df.head()

    def task2(self) -> tp.List[str]:
        return self.df.columns[self.df.isna().any()].tolist()

    def task3(self) -> pd.DataFrame:
        self.df = self.df.dropna()
        return self.df

    def task4(self) -> pd.DataFrame:
        temp = self.df.describe()
        return temp

    def task5(self) -> int:
        return len(self.df[self.df['test_score'] == 100])

    def task6(self) -> pd.DataFrame:
        new_df = self.df[self.df['test_score'] == 100].sort_values('school')
        tmp = new_df.groupby(by='school').agg({'test_score': len, 'number_of_students': ['mean']}).reset_index(drop=False)
        tmp.columns = ['school', 'cnt_100', 'number_of_students']
        tmp = tmp[['school', 'number_of_students', 'cnt_100']]
        return tmp.sort_values(by=['cnt_100', 'school'], ascending=(False, True))

    def task7(self) -> pd.DataFrame:
        new_df = self.df.groupby('school').mean()
        return new_df.sort_values(by='test_score', ascending=False).reset_index(drop=False).head(10)

    def task8(self) -> pd.DataFrame:
        new_df = self.df.groupby('school').mean()
        return new_df.sort_values(by='test_score', ascending=False).reset_index(drop=False).tail(10)

    def task9(self) -> Axes:
        df_less_1000 = self.df[self.df['number_of_students'] <= 1000].reset_index()
        df_more_1000 = self.df[self.df['number_of_students'] > 1000].reset_index()

        b, a = plt.subplots()
        a.hist([df_less_1000['test_score'], df_more_1000['test_score']], bins=10, alpha=0.5, label=['Маленькие Школы', 'Большие Школы'])
        a.legend(loc = 'upper right')

        plt.title('Pаспределение баллов по большим у маленьким школам')

        a.set_ylabel('Количество студентов')
        a.set_xlabel('Очки студента')
        return plt.gca()
