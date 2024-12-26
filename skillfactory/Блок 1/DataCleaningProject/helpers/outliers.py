import pandas as pd
from pandas import DataFrame
import numpy as np
from typing import Union

def outliers_z_score_mod(data: Union[DataFrame, str], feature, log_scale=False, log_offset=1, left=3, right=3):
    """
    Function to identify outliers using the z-score method.
    Added the ability to apply a log transformation to the feature before calculating z-scores.
    Added the ability to specify the number of standard deviations to use for the lower and upper bounds.
    Added the ability to handle data as a file path or a DataFrame.
    Args:
        data (Union[DataFrame, str]): The input data, either as a pandas DataFrame or a file path to a CSV file.
        feature (str): The feature/column name for which to identify outliers.
        log_scale (bool, optional): Whether to apply log transformation to the feature. Defaults to False.
        log_offset (int, optional): The offset to add to the feature before applying log transformation. Defaults to 1.
        left (int, optional): The number of standard deviations to use for the lower bound. Defaults to 3.
        right (int, optional): The number of standard deviations to use for the upper bound. Defaults to 3.
    Returns:
        Tuple[DataFrame, DataFrame]: A tuple containing two DataFrames:
            - outliers: DataFrame containing the outliers.
            - cleaned: DataFrame containing the data without the outliers.
    """

    # If data is a string (file name), read the data from the file, otherwise use the DataFrame
    if isinstance(data, str):
        data = pd.read_csv(data)    
    if log_scale:
        x = np.log(data[feature] + log_offset)
    else:
        x = data[feature]
    
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
    return outliers, cleaned


def outliers_iqr_mod(data: Union[DataFrame, str], feature: str, log_scale=False, log_offset=1, left = 1.5, right = 1.5):
    """
    Detects and removes outliers from a dataset using the Interquartile Range (IQR) method. 
    Added the ability to apply a log transformation to the feature before calculating IQR.
    Added the ability to specify the multiplier for the IQR to determine the lower and upper bounds.
    Added the ability to handle data as a file path or a DataFrame.
        Args:
            data (Union[DataFrame, str]): The input data, either as a pandas DataFrame or a file path to a CSV file.
            feature (str): The name of the feature/column to analyze for outliers.
            log_scale (bool, optional): If True, applies a logarithmic transformation to the feature before calculating IQR. Defaults to False.
            log_offset (int, optional): The offset to add to the feature before applying log transformation. Defaults to 1.
            left (float, optional): The multiplier for the IQR to determine the lower bound. Defaults to 1.5.
            right (float, optional): The multiplier for the IQR to determine the upper bound. Defaults to 1.5.
        Returns:
            Tuple[DataFrame, DataFrame]: A tuple containing two DataFrames:
                - outliers: DataFrame containing the outlier rows.
                - cleaned: DataFrame containing the rows without outliers.
    """
    
    # If data is a string (file name), read the data from the file, otherwise use the DataFrame
    if isinstance(data, str):
        data = pd.read_csv(data)
    if log_scale:
        x = np.log(data[feature]+log_offset)
    else:
        x = data[feature]
    
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
    return outliers, cleaned

