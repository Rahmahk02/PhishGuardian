import streamlit as st
import re
from pathlib import Path
import datetime

# ──────────────────────────────
# Red-flag phishing patterns
# ──────────────────────────────
red_flags = [
    r"(verify|update|review|confirm).{0,15}(account|information|details)",
    r"your account (has been|is) (locked|suspended|limited)",
    r"(click|tap|follow).{0,10}(link|here|below)",
    r"(urgent|immediate) action required",
    r"(you have)?\s?(won|reward|prize|gift card)",
    r"(login|sign in).{0,15}(resolve|avoid|prevent)",
    r"(security|tax|billing) (notice|alert|update)",
    r"within\s?\d{1,2}\s?(hours|days)",
    r"(https?:\/\/)?[^\s]+(\.ru|\.xyz|\.tk|mysecureportal\.com)",
]

suspicious_domains = [".ru", ".xyz", ".tk", "mysecureportal.com"]

# ──────────────────────────────
# Detection Logic
# ──────────────────────────────
def extract_urls(text):
    return re.findall(r"https?://[^\s)>\]]+", text, re.IGNORECASE)

def is_phishing(email_text):
    lowered = email_text.lower()
    matches = [pattern for pattern in red_flags if re.search(pattern, lowered)]
    confidence = int((len(matches) / len(red_flags)) * 100)

    url_list = extract_urls(email_text)
    risky_urls = [u for u in url_list if any(dom in u.lower() for dom in suspicious_domains)]

    if len(matches) >= 2:
        msg = "⚠️ **Possible phishing detected!**"
    elif len(matches) == 1:
        msg = "🟡 **Slightly suspicious. Review with caution.**"
    else:
        msg = "✅ **This message looks safe.**"

    return msg, len(matches) >= 2, matches, confidence, url_list, risky_urls

def report_phishing(email_text):
    report_file = Path("reported_phishing.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp}\n{email_text}\n---\n"
    report_file.write_text(report_file.read_text() + entry if report_file.exists() else entry)
    return "🚨 Report submitted. Thank you!"

# ──────────────────────────────
# Streamlit UI
# ──────────────────────────────
st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
st.title("🛡️ Phishing Detector & Reporter")

with st.expander("📋 What Does This Tool Look For?"):
    st.markdown("""
    This tool scans for phishing signs like:
    - 🔐 Requests to **verify/update account info**
    - 🚫 Warnings like **“account suspended”**
    - 🧨 **Urgent action** prompts
    - 🏆 Claims of **prizes or rewards**
    - 🔗 Links with **risky domains** (e.g. `.ru`, `.xyz`, etc.)
    - 🕒 **Time pressure** ("within 24 hours")
    - 💳 Fake **security/tax/billing alerts**
    """)

email_input = st.text_area("📨 Paste the email or message here:", height=300)

if "last_scan" not in st.session_state:
    st.session_state.last_scan = "No scans yet"

col1, col2 = st.columns(2)
check = col1.button("🔍 Scan for Phishing")
clear = col2.button("🧹 Reset")

if clear:
    st.experimental_rerun()

if check:
    if email_input.strip() == "":
        st.warning("⚠️ Please paste some content first.")
    else:
        msg, is_flagged, patterns, score, urls, risky_urls = is_phishing(email_input)

        st.markdown(msg)
        st.progress(score)

        st.markdown(f"**Confidence Score:** {score}%")
        st.markdown("**Matched Patterns:**")
        if patterns:
            st.markdown("\n".join([f"• `{p}`" for p in patterns]))
        else:
            st.markdown("None")

        st.markdown("**Detected URLs:**")
        if urls:
            for u in urls:
                label = "🚩" if u in risky_urls else "🔗"
                st.markdown(f"{label} {u}")
        else:
            st.markdown("None")

        st.markdown(f"🕒 **Last Scan:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        if is_flagged:
            if st.button("🚨 Report This Message"):
                msg = report_phishing(email_input)
                st.success(msg)

            # Downloadable report
            report_text = f"""Phishing Report
====================
Time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Confidence: {score}%

Matched Patterns:
{chr(10).join(["- " + p for p in patterns]) or 'None'}

Links:
{chr(10).join([f"- {u} {'(RISKY)' if u in risky_urls else ''}" for u in urls]) or 'None'}

Message:
---------
{email_input}
"""
            st.download_button("⬇️ Download Report", report_text, file_name="phishing_report.txt")
