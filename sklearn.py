# sklearn 
# import sklearn as skl
import sklearn as skl
# Importing necessary libraries for Scikit-Learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

# Creating sample data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training a linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Making predictions
y_pred = model.predict(X_test_scaled)

# Calculating the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Loading the Iris dataset
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# Splitting the dataset
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)

# Training a KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_iris, y_train_iris)

# Making predictions
y_pred_iris = knn.predict(X_test_iris)

# Applying PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_iris)
print("PCA Transformed Data:\n", X_pca[:5])

# Importing Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# Generating data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--')
plt.plot(x, y2, label='Cosine Wave', color='red', linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Waves')
plt.legend()
plt.grid()
plt.show()

# Generating a random image
random_image = np.random.rand(100, 100, 3)  # 100x100 RGB image with random pixels
plt.imshow(random_image)
plt.axis('off')
plt.title('Random Image')
plt.show()

# Loading and displaying an image
img = mpimg.imread('sample_image.png')  # Ensure image exists
plt.imshow(img)
plt.axis('off')
plt.title('Displayed Image')
plt.show()

# Creating a bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()

# Creating a scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.scatter(x_scatter, y_scatter, color='orange', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()
