import numpy as np
import pandas as pd

def media(reviews):
    return np.nanmean(reviews.Nota.unique())