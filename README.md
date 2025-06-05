# 🌸 Iris Flower Classification Web App

This project presents a machine learning application that classifies Iris flower species based on their morphological features. Utilizing a **Random Forest Classifier**, the model is trained on the classic Iris dataset and deployed through a **Streamlit** web interface, allowing users to input flower measurements and receive real-time predictions.

## 📌 Features

* **Interactive Web Interface**: User-friendly Streamlit app for inputting flower measurements.
* **Machine Learning Model**: Trained using Random Forest algorithm for accurate classification.
* **Real-time Predictions**: Immediate feedback on the predicted Iris species.
* **Modular Codebase**: Organized structure with separate modules for model training, prediction, and app interface.

## 📁 Repository Structure

```
Iris-ML-Model/
├── .devcontainer/         # Development container configuration
├── app.py                 # Streamlit application script
├── iris.csv               # Dataset containing Iris flower measurements
├── model.py               # Script for training and saving the ML model
├── prediction.py          # Script for loading the model and making predictions
├── rf_model.sav           # Serialized trained Random Forest model
├── requeriments.txt       # List of required Python packages
└── README.md              # Project documentation
```

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system
* Recommended: Create and activate a virtual environment

### Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/TaniaKhatun18/Iris-ML-Model.git
   cd Iris-ML-Model
   ```

2. **Install the required packages**:

   ```
   pip install -r requeriments.txt
   ```

3. **Run the Streamlit application**:
     ```
   streamlit run app.py
     ```
   The application will open in your default web browser. If it doesn't, navigate to `http://localhost:8501` manually.

## 🧠 How It Works

1. **Data Loading**: The application uses the `iris.csv` dataset, which contains measurements of Iris flowers.

2. **Model Training**: The `model.py` script trains a Random Forest Classifier on the dataset and saves the trained model as `rf_model.sav`.

3. **Prediction**: The `prediction.py` script loads the saved model and defines a function to make predictions based on user input.

4. **Web Interface**: The `app.py` script creates a Streamlit web application that collects user input, invokes the prediction function, and displays the predicted Iris species.

## 📊 Dataset

The Iris dataset consists of 150 records under five attributes:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)
* Species (Setosa, Versicolor, Virginica)

This dataset is a classic in the field of machine learning and is widely used for testing classification algorithms.

## 🛠️ Dependencies

The project relies on the following Python packages:

* pandas
* numpy
* scikit-learn
* streamlit
* pickle

All dependencies are listed in the `requeriments.txt` file.

## 📈 Future Enhancements

* **Model Evaluation**: Incorporate evaluation metrics and visualizations to assess model performance.
* **User Input Validation**: Add checks to ensure valid input ranges for flower measurements.
* **Enhanced UI**: Improve the aesthetics and responsiveness of the web interface.
* **Deployment**: Host the application on a cloud platform for broader accessibility.

## 👩‍💻 Author

**Tania Khatun**

Aspiring AI Developer | Python Enthusiast

📄 License
This project is for educational purposes and personal learning.

## 📬 Contact
Feel free to connect or give feedback!
📧 Email: sania.khatun18022006@gmail.com
🌐 LinkedIn: : www.linkedin.com/in/tania-khatun-024a30324




