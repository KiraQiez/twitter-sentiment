# 🐦 Twitter Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![NLP](https://img.shields.io/badge/NLP-Text%20Classification-orange)](#)

A Natural Language Processing (NLP) project that **scrapes tweets**, **preprocesses text**, and **trains a sentiment classifier** (Logistic Regression / Naive Bayes) to predict whether a tweet expresses **Positive**, **Negative**, or **Neutral** sentiment.

---

## 📌 Features
- Scrape tweets using:
  - `snscrape` (no API keys, but may need SSL fix)
  - **or** `Tweepy` (requires Twitter API keys)
- Clean and preprocess text (remove mentions, hashtags, punctuation, stopwords)
- Train sentiment classification model:
  - Logistic Regression (LR)
  - Naive Bayes (NB)
- Evaluate model performance with accuracy, precision, recall, F1-score
- Predict sentiment for new text

---
