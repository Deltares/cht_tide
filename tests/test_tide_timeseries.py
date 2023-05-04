import pandas as pd

from cht_tide.tide_predict import predict


def test_timeseries_from_components():
    # Create dataframe with values
    data = {
        "amplitude": [
            0.39452,
            0.06667,
            0.08968,
            0.01860,
            0.05285,
            0.04300,
            0.01846,
            0.00857,
            0.01022,
            0.00451,
            0.00200,
            0.00101,
            0.00129,
            0.05300,
            0.07800,
        ],
        "phase": [
            14.38,
            40.10,
            352.95,
            36.25,
            217.27,
            234.41,
            220.42,
            233.82,
            348.71,
            347.03,
            180.00,
            89.38,
            202.68,
            50.50,
            176.30,
        ],
    }
    df = pd.DataFrame(
        data,
        index=[
            "M2",
            "S2",
            "N2",
            "K2",
            "K1",
            "O1",
            "P1",
            "Q1",
            "MF",
            "MM",
            "M4",
            "MS4",
            "MN4",
            "SSA",
            "SA",
        ],
    )
    df.index.name = "constituent"

    # Create timeseries
    times = pd.date_range(start="2023-01-01", end="2023-01-02", freq="10T")

    # Predict the tide
    v = predict(df, times)

    assert v.dtype == "float64"
    assert len(times) == len(v)
