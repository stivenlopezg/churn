import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from classification_model.config import *
import os

# Transformation
state_categories = STATE_CATEGORIES
area_categories = AREA_CATEGORIES
international_plan_categories = INTERNATIONAL_PLAN_CATEGORIES
voice_mail_categories = VOICE_MAIL_CATEGORIES


class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.loc[:, self.columns]
        return X


class Mapper(BaseEstimator, TransformerMixin):
    def __init__(self, column: str, map: dict):
        if not isinstance(column, str):
            self.column = str(column)
        else:
            self.column = column
        if map is None:
            map = mapper
        self.map = map

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X[self.column] = X[self.column].map(self.map)
        return X


class ConvertDtypes(BaseEstimator, TransformerMixin):
    def __init__(self, numerical: list, categorical: list):
        if not isinstance(numerical, list):
            self.numerical = [numerical]
        else:
            self.numerical = numerical
        if not isinstance(categorical, list):
            self.categorical = [categorical]
        else:
            self.categorical = categorical

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        for numeric in self.numerical:
            X[numeric] = pd.to_numeric(X[numeric])
        for category in self.categorical:
            if category == 'state':
                categories = state_categories
            elif category == 'area code':
                categories = area_categories
            elif category == 'international plan':
                categories = international_plan_categories
            else:
                categories = voice_mail_categories
            X[category] = pd.Categorical(X[category], categories=categories)
        return X


class GetDataFrame(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = pd.DataFrame(X, columns=self.columns)
        return X


class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = pd.get_dummies(X, columns=self.columns, drop_first=True)
        return X
