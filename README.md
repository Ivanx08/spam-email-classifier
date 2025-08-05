# 📧 Spam Email Classifier

A machine learning web app that classifies SMS messages as **Spam** or **Ham** (Not Spam) using a **Multinomial Naive Bayes** model trained on the [Kaggle SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). Built using scikit-learn, deployed using Streamlit, and designed for real-time classification through a simple and intuitive interface.

---

## 🚀 Live Demo

> 🌐 **Coming Soon**: Hosted on [Streamlit Community Cloud](https://streamlit.io/cloud)

> 🧠 Accuracy: ~96% (on test dataset)

---

## 📌 Project Highlights

- 📧 Classifies SMS messages into **Spam** or **Ham**
- 🧼 Text preprocessing using **TF-IDF vectorization**
- 🤖 Trained using **Multinomial Naive Bayes** (sklearn)
- 💾 Model and vectorizer exported as `.pkl` files
- 🖥️ Deployed using [Streamlit Community Cloud](https://streamlit.io/cloud)
- 📓 [View Model Training Notebook (Google Colab)](https://colab.research.google.com/drive/1FpBBntvnKTPLnt6s-tIYhk_ii8hAQ_TI?usp=sharing)
- 📊 Dataset sourced from [Kaggle: SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## 🧠 Model Details

- **Model Type**: Multinomial Naive Bayes (scikit-learn)  
- **Vectorization**: TF-IDF using `TfidfVectorizer`  
- **Evaluation Metric**: Accuracy  
- **Accuracy**: ~96.2% on test data  
- **Data Preprocessing**: Lowercasing, punctuation removal, stopword filtering

---

## 🛠️ Tech Stack

| Tool            | Purpose                            |
|-----------------|------------------------------------|
| Python          | Core programming language          |
| scikit-learn    | Model training and evaluation      |
| Streamlit       | Web app development                |
| Pandas          | Data loading and preprocessing     |
| NumPy           | Numerical operations               |
| joblib          | Model persistence (`.pkl` files)   |
| Google Colab    | Model training and experimentation |
| Git & GitHub    | Version control and hosting        |

---

## 📂 Project Structure

```bash
📁 spam-email-classifier
├── app.py                   # Streamlit application
├── spam_model.pkl           # Trained Naive Bayes model
├── vectorizer.pkl           # TF-IDF vectorizer
├── spam.csv                 # Raw dataset
├── requirements.txt         # Python dependencies
├── setup.sh                 # Optional auto setup script
├── README.md                # Project documentation
├── spam_training.ipynb      # 📓 Google Colab notebook (also linked above)


---

## 🧪 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/Ivanx08/spam-email-classifier.git

# 2. Move into the project directory
cd spam-email-classifier

# 3. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate  # On Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

---

## 🧠 What I Learned

- ✉️ Natural language preprocessing for text classification

- 🤖 Training and evaluating models using scikit-learn

- 🧠 TF-IDF and Naive Bayes for spam detection

- 🌐 Deploying ML models with Streamlit

- 🔁 Saving and loading models with joblib

- 🗂️ Structuring projects for production-readiness


---

## 📄 License

This project is released under the **MIT License** – free to use, modify, and distribute.


---

## 🙋‍♂️ About the Author

I'm **Shivam Bhati**, an aspiring AI developer passionate about building real-world applications through hands-on projects. I enjoy translating complex deep learning ideas into accessible web apps.

> 🔗 [Connect on LinkedIn](https://www.linkedin.com/in/shivam-bhati-dev/)
