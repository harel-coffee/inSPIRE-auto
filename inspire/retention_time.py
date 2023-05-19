""" Functions for calculating difference between predicted and detected
    retention times.
"""
import pandas as pd
from pyteomics import achrom
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

from inspire.constants import (
    ACCESSION_STRATUM_KEY,
    LABEL_KEY,
    PEPTIDE_KEY,
    RT_KEY,
    SPECTRAL_ANGLE_KEY,
)

def _add_achrom_rt_preds(train_df, test_df):
    """ Function to fit and predict achrom's predictor.

    Parameters
    ----------
    train_df : pd.DataFrame
        A DataFrame on which to fit the retention time predictor.
    test_df : pd.DataFrame
        A DataFrame on which to predict retention time.

    Returns
    -------
    test_df : pd.DataFrame
        The input test_df with predRT as a new column.
    """
    retention_time_model = achrom.get_RCs_vary_lcp(
        train_df[PEPTIDE_KEY],
        train_df['retentionTime'],
        lcp_range=(-1.0, 1.0),
        term_aa=False,
        rcond=None
    )

    if 'C' not in retention_time_model['aa']:
        retention_time_model['aa']['C'] = retention_time_model['aa']['P']*0.956
    if 'W' not in retention_time_model['aa']:
        retention_time_model['aa']['W'] = retention_time_model['aa']['P']*0.956

    pred_rts = test_df[PEPTIDE_KEY].apply(
        lambda x :  achrom.calculate_RT(x, retention_time_model, raise_no_mod=False)
    )
    return pred_rts

def add_delta_irt(combined_df, config, scan_file):
    """ Function to calculate difference between predicted and observed retention
        time for each PSM.

    Parameters
    ----------
    combined_df : pd.DataFrame
        A DataFrame of PSMs.

    Returns
    -------
    combined_df : pd.DataFrame
        The DataFrame updated with a deltaRT column.
    """
    if combined_df[RT_KEY].nunique() <= 1:
        combined_df['deltaRT'] = 0
        return combined_df

    kfold = KFold(n_splits=10, shuffle=True, random_state=42)
    combined_df_list = []
    coefficents = []
    intercepts = []

    if 'iRT' in combined_df.columns:
        combined_df_irt_null_count = combined_df[combined_df['iRT'].isnull()].shape[0]
    else:
        combined_df_irt_null_count = 1

    try:
        for train, test in kfold.split(combined_df):
            train_df = combined_df.iloc[train]
            test_df = combined_df.iloc[test]

            if ACCESSION_STRATUM_KEY in train_df.columns:
                train_df = train_df[train_df[ACCESSION_STRATUM_KEY] == 0]

            train_df = train_df[train_df[LABEL_KEY] == 1]
            top_spec_angle_cut = train_df[SPECTRAL_ANGLE_KEY].quantile(0.9)
            train_df = train_df[
                train_df[SPECTRAL_ANGLE_KEY] > top_spec_angle_cut
            ]

            if combined_df_irt_null_count > 0:
                test_df['predRT'] = _add_achrom_rt_preds(train_df, test_df)
            else:
                reg = LinearRegression().fit(
                    train_df[['iRT']],
                    train_df[RT_KEY]
                )
                coefficents.append(reg.coef_[0])
                intercepts.append(reg.intercept_)
                test_df['predRT'] = reg.predict(test_df[['iRT']])

            test_df['deltaRT'] = (test_df['predRT'] - test_df['retentionTime']).abs()
            combined_df_list.append(test_df)
        combined_df = pd.concat(combined_df_list)
    except ValueError:
        # Simplest way to avoid errors on tiny files.
        train_df = train_df[train_df[LABEL_KEY] == 1]
        reg = LinearRegression().fit(
            train_df[['iRT']],
            train_df[RT_KEY]
        )
        coefficents.append(reg.coef_[0])
        intercepts.append(reg.intercept_)
        combined_df['predRT'] = reg.predict(combined_df[['iRT']])
        combined_df['deltaRT'] = (combined_df['predRT'] - combined_df['retentionTime']).abs()

    rt_df = pd.DataFrame({
        'coefficents': coefficents,
        'intercepts': intercepts,
    })
    if scan_file is not None:
        rt_df.to_csv(f'{config.output_folder}/rt_fit_{scan_file}.csv', index=False)

    return combined_df
