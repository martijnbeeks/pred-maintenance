from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
class RecordedDate(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X["year_recording"] = pd.to_datetime(X['date_recorded']).dt.year
        X["month_recording"] = pd.to_datetime(X['date_recorded']).dt.month
        X["day_recording"] = pd.to_datetime(X['date_recorded']).dt.day
        return X

    def get_feature_names(self):
        return ['year_recording', 'month_recording', 'day_recording']