
# 🚗 Car Selling Price Prediction Web App  

This is a **Streamlit-based web application** that predicts the selling price of a car based on user inputs like manufacturing year, kilometers driven, fuel type, seller type, transmission type, and ownership status.  
The application uses multiple regression models trained on car price data.

---

## ✅ Features:
- Select from various machine learning models:
  - Linear Regression  
  - Ridge Regression  
  - Lasso Regression  
  - Random Forest Regressor  
  - Bagging Regressor  
- Interactive UI with sliders and dropdowns  
- Real-time price prediction when you click **Predict Selling Price**  
- Professional and clean interface  

---

## 🛠️ Technologies Used:
- Python  
- Streamlit  
- Scikit-learn  
- Numpy  
- Pickle (for loading pre-trained models)  

---

## 🚀 How to Run Locally:

1️⃣ **Clone or Download this Repository**  
Or copy all project files into your folder.

2️⃣ Make sure these trained model files are present in your project folder:
```
Linear_reg model.pkl
Ridge_reg model.pkl
Lasso_reg model.pkl
RandomForest_reg model.pkl
Bagging_reg model.pkl
```

3️⃣ Install the required Python packages:
```bash
pip install -r requirements.txt
```

4️⃣ Start the Streamlit app:
```bash
streamlit run app.py
```

5️⃣ Open the URL provided in your terminal (usually `http://localhost:8501/`)  

---

## 📁 Project Structure:
```
├── app.py
├── Linear_reg model.pkl
├── Ridge_reg model.pkl
├── Lasso_reg model.pkl
├── RandomForest_reg model.pkl
├── Bagging_reg model.pkl
├── Car_price_prediction_jupyter_file.ipynb
├── README.md
├── requirements.txt
```

---

## 🏗️ Model Training:
The model training and export to `.pkl` files can be done using the Jupyter Notebook provided:
```
Car_price_prediction_jupyter_file.ipynb
```

## 🙋‍♂️ Support:
If you face any issues, feel free to reach out or open an issue in the repository.


