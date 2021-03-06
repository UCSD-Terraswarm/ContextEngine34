#Wanlin Cui

import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel();

y[::5] += 1 * (0.5 - np.random.rand(8))

trainer = DecisionTreeAB(complexity=0, numInputs=1, discreteOutputs=0, discreteInputs=0)
trainer.addBatchObservations(X,y);
trainer.train();


y_predict = np.empty([0]);

for i in range(T.shape[0]):
	result = trainer.execute(T[i]);
	y_predict = np.concatenate((y_predict,result));

plt.subplot(1, 1, 1)
plt.scatter(X, y, c='k', label='data')
plt.plot(T, y_predict, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("Decision Tree With AdaBoostClassifier (k = %i, weights = '%s')" % (2,
	"uniform"))

plt.show()