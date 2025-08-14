# 🛡️ PhishGuardian

PhishGuardian is a simple Streamlit web app that detects phishing messages and helps users report suspicious emails. It scans for red flags like suspicious phrases, risky URLs, urgency triggers, and fake alerts.

---

## ⚡ Quick Try (Live Version)
1. Open the [Live App link](https://phishguardian-6z94cyj7yavmezselurvjn.streamlit.app/#phishing-detector-and-reporter) in your browser.  
2. If prompted, click **“Wake up”** or similar to start the app.  
3. Start detecting and reporting phishing emails immediately—no installation needed.  

---

## 🚀 Features
- Detects common phishing patterns in email text  
- Highlights risky URLs (e.g. `.ru`, `.xyz`, known suspicious domains)  
- Provides a confidence score for how likely the email is phishing  
- Reporting system that appends suspicious emails to a local log  
- Downloadable phishing report  

---

## 📦 Requirements
- Python **3.8+** (tested on 3.10)  
- Streamlit (included in `requirements.txt`)  

---

## 🛠 Installation & Run

1. **Open your terminal / command prompt**  
   - **Windows:** Press `Win + R`, type `cmd` or `powershell`, and hit Enter  
   - **macOS:** Open **Terminal** from Applications → Utilities  
   - **Linux:** Open your preferred terminal  

2. **Check Python is installed**  
   ```bash
   python --version
1. **Clone the repository**  
```bash
  git clone https://github.com/Rahmahk02/PhishGuardian.git
```
```bash
  cd PhishGuardian
```
2. **Install dependencies**
```bash
  pip install -r requirements.txt
```
3. **Run the app**
```bash
  streamlit run phishing_checker.py
```
