import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer


preprocess_pipeline = ColumnTransformer(
    transformers=[
    ],
    remainder="passthrough",
    verbose_feature_names_out=False,
)
preprocess_pipeline.set_output(transform="pandas")
