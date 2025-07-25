# Breast Cancer Classification Using PCA 

This project demonstrates how **Principal Component Analysis (PCA)** can be applied to the breast cancer dataset (from `sklearn.datasets`) to reduce dimensionality. The goal is to help the Anderson Cancer Center identify essential variables for donor funding and manage the growing number of referrals with data-driven insight.

---

## 📁 Project Structure

```

project/
│
├── pca.py      # Main script with PCA 
├── pca2.py      # This script reduced the dataset to 2 PCA component 
├── README.md   # Project documentation

````

---

## 📊 Dataset

- **Source:** `sklearn.datasets.load_breast_cancer`
- **Features:** 30 numerical attributes about tumor cells
- **Target:** Binary classification — Malignant (0) or Benign (1)

---

## 🧪 What the Project Does

1. Loads and Standardises the dataset
2. **Uses PCA** to show the most essential variables driving variance in cancer patient data
2. **Applies PCA** to reduce features to **2 principal components**
3. **Visualizes results** for interpretable insights

---

## 🚀 How to Run

1. Clone the repository or copy the script.
2. Ensure Python and required libraries are installed:

   ```bash
   pip install pandas scikit-learn matplotlib numpy

3. Run the script:

   ```bash
   python3 pca.py
   ```
4. Run the script:

   ```bash
   python3 pca2.py
   ```
---

## 📈 Results

* Dimensionality reduced from 30 → 2 using PCA
* The first script shows the most essential variables driving variance in cancer patient data and should be prioritised in reports to donors. 
It also outputs a variance plot that shows how many components are needed to retain ~90% of the information.
<img width="500" alt="fig1" src="fig1.png" />
<img width="500" alt="fig1b" src="fig1b.png" />
* The second script outputs a 2D scatter plot, clearly separating malignant and benign cases using the top 2 PCA components
  <img width="500" alt="fig2 - 2 PCA components" src="fig2.png" />
* Identified the top contributing variables for donor insights

---



## 📄 License

This project is open source and free to use for educational or internal business purposes.

---

## 💬 Contact

For improvements, feel free to open a pull request on my GitHub account or contact me directly - josephdokhare@gmail.com

