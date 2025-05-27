import streamlit as st
import google.generativeai as genai

# Your FREE Google Gemini API key
API_KEY = "AIzaSyBHYeUO1ctNG-zK-YY3SMOlP1-eTEZ18gw"  # Replace this with your real key from makersuite

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize model (gemini-pro for text only)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="SAP GenAI Assistant", layout="centered")
st.title("🧠 SAP GenAI Assistant")
st.markdown("Ask about SAP processes, documentation, or how-tos.")

question = st.text_area("💬 Ask your SAP question:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(question)
            st.markdown("### 💡 Answer:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

      # Footer
st.markdown("---")
st.markdown("Developed by Luiz Lopes – GenAI for SAP Users | v0.2")
