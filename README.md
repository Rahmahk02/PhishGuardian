# 🛡️ Phishing Detector & Reporter

**Live App:** [Try it on Streamlit](https://phishguardian-6z94cyj7yavmezselurvjn.streamlit.app/#phishing-detector-and-reporter)

This is a simple Streamlit web app that detects phishing messages and helps users report suspicious emails. It scans for red flags like suspicious phrases, risky URLs, urgency triggers, and fake alerts.

## 🚀 Features

- Detects common phishing patterns in email text
- Highlights risky URLs (e.g. `.ru`, `.xyz`, known suspicious domains)
- Confidence score for how likely the email is phishing
- Reporting system that appends suspicious emails to a local log
- Downloadable phishing report

## 📦 Requirements

- Python 3.7+
- Streamlit

## 🛠 Installation

```bash
git clone https://github.com/Rahmahk02/PhishGuardian.git
cd PhishGuardian
pip install -r requirements.txt

streamlit run app.py

