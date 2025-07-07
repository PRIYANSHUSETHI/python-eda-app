
# 📊 Data Analysis Web App using Python & Streamlit

A lightweight and interactive **data analysis web application** built using **Streamlit**. Upload your CSV files and perform essential **EDA (Exploratory Data Analysis)** tasks like viewing data, checking datatypes, inspecting for nulls and duplicates, and visualizing dataset statistics—**without writing a single line of code**.

---

## 🚀 Demo

> Want to see it in action?  
> Check out a live demo (if deployed) or run it locally using the instructions below.

---

## 📂 Features

This Streamlit app provides the following functionalities:

### 🔍 Dataset Upload & Preview
- Upload your `.csv` file.
- View the **head** or **tail** of the dataset.

### 📐 Dataset Dimensions
- Inspect the number of **rows** and **columns**.

### 🔤 Data Types
- View the datatype of each column.

### ⚠️ Null Value Detection
- Heatmap visualization of missing values using `seaborn`.
- Friendly success message if there are no nulls.

### 🔁 Duplicate Detection & Removal
- Identify duplicate rows in your dataset.
- Optionally remove them with a single click.

### 📈 Descriptive Statistics
- Get a comprehensive statistical summary of your data using `pandas.describe()`.

### 💬 Additional Info
- Info section about the app and author.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `seaborn` for null value heatmap
  - `matplotlib.pyplot` (via Streamlit for plotting)

---

## 🧑‍💻 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/data-analysis-streamlit-app.git
   cd data-analysis-streamlit-app
   ```

2. **Install dependencies**:
   Make sure you have Python 3.x installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit pandas seaborn matplotlib
   ```

3. **Run the application**:
   ```bash
   streamlit run app_python.py
   ```

4. **Upload your CSV file** and start exploring!

---

## 📁 File Structure

```
📦 data-analysis-streamlit-app/
 ┣ 📄 app_python.py        # Main Streamlit application
 ┗ 📄 README.md            # Project overview and documentation
```

---

## 📌 To-Do / Future Enhancements

- Add basic visualizations (histograms, bar charts, etc.)
- Correlation matrix
- File format support beyond `.csv`
- Deploy on Streamlit Cloud or Heroku

---

## 🙋‍♂️ Author

**Priyanshu Sethi**  
Connect with me on [LinkedIn](https://www.linkedin.com/in/priyanshu-sethi-bitsh/)  
Built with ❤️ using Streamlit

