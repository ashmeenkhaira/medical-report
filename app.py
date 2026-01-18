import streamlit as st
import tensorflow as tf
from utils.image_utils import preprocess_image
from utils.inference import generate_report, load_vocab

st.set_page_config(
    page_title="Chest X-ray Report Generator",
    layout="centered"
)
from huggingface_hub import hf_hub_download

@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="<your-username>/chest-xray-report-generator",
        filename="model.keras"
    )
    return tf.keras.models.load_model(model_path)

model = load_model()
vocab = load_vocab("model/vocab.txt")

st.title("🩻 Chest X-ray Automated Report Generator")
st.warning("For research and educational use only. Not for clinical diagnosis.")

frontal = st.file_uploader("Upload Frontal (PA) X-ray", type=["png", "jpg"])
lateral = st.file_uploader("Upload Lateral X-ray", type=["png", "jpg"])

if frontal and lateral:
    st.image([frontal, lateral], caption=["Frontal", "Lateral"], width=250)

    if st.button("Generate Report"):
        with st.spinner("Analyzing X-rays..."):
            img_f = preprocess_image(frontal)
            img_l = preprocess_image(lateral)
            report, diseases = generate_report(model, img_f, img_l, vocab)

        st.subheader("🩺 Predicted Conditions")
        for d, p in diseases.items():
            st.write(f"- **{d}**: {p:.2f}")

        st.subheader("📄 Generated Radiology Report")
        st.write(report)
