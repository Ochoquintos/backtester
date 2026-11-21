import numpy as np
import pandas as pd


def test_pandas_works():
    assert pd.Series(np.arange(3)).sum() == 3
