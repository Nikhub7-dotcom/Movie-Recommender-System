# 🎬 Movie Recommender System

This is a content-based movie recommender system built using Python and Streamlit. It recommends similar movies based on the user's selected movie using cosine similarity on movie features like genres, keywords, and more.

---

## 🚀 Deployed App

Click the button below to try the app live:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://your-streamlit-app-link.streamlit.app](https://nikhub7-dotcom-movie-recommender-system-appapp-o97aha.streamlit.app/)

> Replace `https://your-streamlit-app-link.streamlit.app` with your actual deployed URL.

---

## 📁 Project Structure

Movie-Recommender-System/
│
├── app/
│ └── app.py # Streamlit frontend app
│
├── model/
│ ├── movies_dict.pkl # Movie metadata dictionary
│ └── similarity.pkl # Precomputed similarity matrix
│
├── .gitattributes # Git LFS tracked files
├── .gitignore # Files to ignore in Git
├── README.md # This file
└── requirements.txt # Python dependencies


---

## 🔧 Features

- Recommends top 5 similar movies based on a selected title
- Uses cosine similarity between TF-IDF or count vector features
- Beautiful, responsive UI with Streamlit
- Scalable deployment-ready structure

---

## 🧠 How It Works

- **Data**: Movies metadata scraped from TMDB or preprocessed from Kaggle datasets.
- **Similarity**: Uses cosine similarity on text features (like overview, genres, etc.).
- **Model Files**: `movies_dict.pkl` and `similarity.pkl` are loaded at runtime.

---

## 🛠 Installation (Local Development)

```bash
git clone https://github.com/Nikhub7-dotcom/Movie-Recommender-System.git
cd Movie-Recommender-System
pip install -r requirements.txt
streamlit run app/app.py

☁️ Deployment
The app is deployed using Streamlit Cloud. For large .pkl files (like similarity.pkl), Git LFS or external hosting is used.

🙋‍♂️ Author
Nikhil Kumar
GitHub: @Nikhub7-dotcom


