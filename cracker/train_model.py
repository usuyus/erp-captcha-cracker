from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from test_data import generate_dataset
from PIL import Image
import pickle

def train_new_model(n):
	clf = MLPClassifier(verbose=True)
	data, label = generate_dataset(n)
	clf.fit(data, label)
	with open("data/model.pkl", "wb") as f:
		pickle.dump(clf, f)

# train_new_model(10000)

def get_current_model():
	with open("data/model.pkl", "rb") as f:
		clf = pickle.load(f)
	return clf

def predict_captcha(digits):
	ds = get_current_model().predict(digits).tolist()
	return "".join([str(i) for i in ds])