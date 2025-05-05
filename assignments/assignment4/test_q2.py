from hw4_q2 import *

import pandas as pd
import numpy as np


fname = "populations.txt"


def test_assert_largest_species_series():
    assert isinstance(largest_species(fname), pd.Series)


def test_largest_species_idx():
    data = pd.read_csv(
        "tests_data/q3_largest.csv", index_col=0, header=None, names=["year", "animal"]
    )
    assert np.all(data.index == largest_species(fname).index)


def test_largest_species_content():
    data = pd.read_csv(
        "tests_data/q3_largest.csv",
        index_col=0,
        header=None,
        names=["year", "animal"],
        squeeze=True,
    )
    assert np.all(data.values == largest_species(fname).values)


def test_assert_lynx_series():
    assert isinstance(lynxes_when_hares(fname), pd.Series)


def test_lynx_idx():
    data = pd.read_csv(
        "tests_data/q3_lynx.csv", index_col=0, header=None, names=["year", "lynx"]
    )
    assert np.all(data.index == lynxes_when_hares(fname).index)


def test_lynx_values():
    data = pd.read_csv(
        "tests_data/q3_lynx.csv",
        index_col=0,
        header=None,
        names=["year", "lynx"],
        squeeze=True,
    )
    assert np.allclose(data.values, lynxes_when_hares(fname).values)


def test_mean_columns():
    data = pd.read_csv("tests_data/q3_mean.csv", index_col=0, header=0)
    assert all(data.columns == mean_animals(fname).columns)


def test_mean_vals():
    data = pd.read_csv("tests_data/q3_mean.csv", index_col=0, header=0)
    assert np.allclose(
        data.mean_animals.values, mean_animals(fname).mean_animals.values
    )
