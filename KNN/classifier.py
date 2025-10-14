import numpy as np
from collections import Counter

# Calculate Euclidean distance
def euclidean_distance(x1, x2):
  return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
  def __init__(self, k=3):
    self.k = k

  def fit(self, X, y):
    self.X_train = X
    self.y_train = y

  def predict(self, X):
    predictions = [self._predict(x) for x in X]
    return np.array(predictions)

  def _predict(self, x):
    # Compute distances to all training points
    distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
      
    # Get indices of the k nearest neighbors
    k_indices = np.argsort(distances)[:self.k]
      
    # Get the labels of the k nearest neighbors
    k_nearest_labels = [self.y_train[i] for i in k_indices]
      
    # Majority vote
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]

# Example usage
if __name__ == "__main__":
  from sklearn.datasets import load_iris
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score

  # Load dataset
  iris = load_iris()
  X, y = iris.data, iris.target

    # Train-test split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Initialize and train KNN
  knn = KNN(k=3)
  knn.fit(X_train, y_train)

  # Predict and evaluate
  predictions = knn.predict(X_test)
  print("Accuracy:", accuracy_score(y_test, predictions))
