import streamlit as st
import joblib

# Load the trained spam classification model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Set the page configuration for Streamlit
st.set_page_config(page_title="Spam Email Classifier", page_icon="📧")

# App title and short description
st.title("📧 Spam Email Classifier")
st.markdown("### 🧠 Enter a message to let model predict if it's spam or not.")

# Sample messages for quick testing
samples = {
    "🎁 Free Prize Spam": "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward!",
    "🔐 Bank Account Spam": "PRIVATE! Your 2004 Account Statement for 07742676969 shows 786 unredeemed Bonus Points.",
    "🧾 Bill Payment Ham": "Your Airtel bill of ₹599 is due tomorrow. Pay on time to avoid charges.",
    "👨‍💼 Boss Email Ham": "Please prepare the report for Monday’s meeting and send it by 5 PM."
}

# Sample selection
selected_sample = st.selectbox("Choose a sample message (optional):", [""] + list(samples.keys()))
default_text = samples[selected_sample] if selected_sample else ""

# Input area (pre-fills if sample selected)
user_input = st.text_area("Or type your own message:", value=default_text)

# Prediction logic
if st.button("Predict"):
    if user_input:
        try:
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)[0]
            confidence = model.predict_proba(input_vector)[0].max()
            
        
            if prediction == 0:
                st.subheader("✅ Not Spam (Ham)")
                st.write(f"Confidence: {confidence * 100:.2f}%")
            else:
                st.subheader("🚫 Spam")
                st.write(f"Confidence: {confidence * 100:.2f}%")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("⚠️ Please enter a message.")

st.markdown("---")
st.markdown("Made with ❤️| Author: Shivam Bhati")
st.markdown("Codec Technologies Internship Projects")
