from sklearn.datasets import load_iris

dataset = load_iris()
x = dataset.data
y = dataset.target
print(dataset.DESCR)