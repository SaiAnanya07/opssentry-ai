"""
SHAP Explainability Engine for OpsSentry
Explains why the ML model predicted pipeline failure
"""

import shap
import pandas as pd


class SHAPExplainer:

    def __init__(self, model):
        self.model = model
        self.explainer = shap.Explainer(model)

    def explain_prediction(self, input_data: dict):
        """
        Return feature importance for a single prediction
        """

        df = pd.DataFrame([input_data])

        shap_values = self.explainer(df)

        explanation = {}

        for feature, value in zip(df.columns, shap_values.values[0]):
            explanation[feature] = float(value)

        return explanation
