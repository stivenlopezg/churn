import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, recall_score, precision_score, \
    accuracy_score, roc_auc_score, f1_score


def generate_report(y_true: list, y_pred: list):
    report = pd.DataFrame(classification_report(y_true=y_true, y_pred=y_pred, output_dict=True)).T
    return report


def confusion_matrix(y_true: list, y_pred: list):
    table = np.round(pd.crosstab(index=y_true, columns=y_pred,
                                 rownames=['Observed'], colnames=['Predicted'], normalize='index'), 2)
    return table


def metrics_summary(y_true: list, y_pred: list):
    print(f'El área bajo la curva ROC es: {roc_auc_score(y_true=y_true, y_score=y_pred)}')
    print(f'La exactitud es: {accuracy_score(y_true=y_true, y_pred=y_pred)}')
    print(f'La precisión es: {precision_score(y_true=y_true, y_pred=y_pred)}')
    print(f'El recall es: {recall_score(y_true=y_true, y_pred=y_pred)}')
    print(f'El puntaje F1 es: {f1_score(y_true=y_true, y_pred=y_pred)} \n')
