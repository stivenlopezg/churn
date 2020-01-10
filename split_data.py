import pandas as pd
import logging
from sklearn.model_selection import train_test_split

filename = 'data/churn.tsv'
train_path = 'data/train.csv'
test_path = 'data/test.csv'


def load_data(file: str = None):
    if file is None:
        file = filename
    df = pd.read_csv(file, sep='\t')
    logging.info('Se ha cargado el conjunto de datos correctamente.')
    return df


def split_data(data: pd.DataFrame, label: str):
    target = data.pop(label)
    train_data, test_data, train_label, test_label = train_test_split(data, target,
                                                                      test_size=0.2, random_state=42, stratify=target)
    logging.info('Se ha hecho la partición en un conjunto de entrenamiento y otro de prueba.')
    return train_data, test_data, train_label, test_label


def concatenate_data(train_data: pd.DataFrame, test_data: pd.DataFrame,
                     train_label: pd.DataFrame, test_label: pd.DataFrame):
    train_df = pd.concat([train_data, train_label], axis=1).reset_index(drop=True)
    test_df = pd.concat([test_data, test_label], axis=1).reset_index(drop=True)
    logging.info('El conjunto de entrenamiento y prueba está listo.')
    return train_df, test_df


def export_data(train: pd.DataFrame, test: pd.DataFrame):
    logging.info('Se ha exportado el conjunto de entrenamiento y de prueba.')
    return train.to_csv(train_path, sep=';', index=False), test.to_csv(test_path, sep=';', index=False)


if __name__ == '__main__':
    data = load_data()
    train_data, test_data, train_label, test_label = split_data(data=data, label='target')
    train_df, test_df = concatenate_data(train_data=train_data, test_data=test_data,
                                         train_label=train_label, test_label=test_label)
    export_data(train=train_df, test=test_df)
