import streamlit as st
import google.generativeai as genai

# Your Google Gemini API key
API_KEY = "AIzaSyBHYeUO1ctNG-zK-YY3SMOlP1-eTEZ18gw"  # Replace with your actual API key

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-pro")

# App UI
st.set_page_config(page_title="SAP GenAI Assistant", layout="centered")
st.title("🧠 SAP GenAI Assistant")
st.markdown("Ask your SAP-related question below:")

# Use st.text_input for mobile-friendly input
question = st.text_input("💬 Your SAP question:")

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
