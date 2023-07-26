import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca','thal', 'heartdisease']
heartDisease = pd.read_csv('heart2.csv', names = names)
heartDisease = heartDisease.replace('?', np.nan)
model = BayesianNetwork([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'), ('heartdisease','chol')])
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
from pgmpy.inference import VariableElimination
HeartDisease_infer = VariableElimination(model)
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': int(input("enter age")), 'sex' :int(input("enter num(0 or 1)"))})
print(q['heartdisease'])