import os
import tempfile

import streamlit as st
from PIL import Image
from inference_sdk import InferenceHTTPClient, InferenceConfiguration

# Page configuration
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱",
    layout="wide"
)

# Roboflow connection
@st.cache_resource
def get_client():
    return InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key=os.environ["ROBOFLOW_API_KEY"]
    ).configure(
        InferenceConfiguration(api_key_transport="header")
    )

# Website heading
st.title("🌱 Plant Disease Detection")
st.write(
    "Upload a plant leaf image to detect possible diseases "
    "using an AI-powered detection model."
)

st.divider()

# Image upload
uploaded_file = st.file_uploader(
    "Upload a plant image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Plant Image",
        use_container_width=True
    )

    if st.button("🔍 Detect Disease", type="primary"):

        try:
            with st.spinner("Analyzing your plant image..."):

                client = get_client()

                # Save image temporarily for Roboflow
                with tempfile.NamedTemporaryFile(
                    suffix=".jpg", delete=False
                ) as temp_file:
                    image.save(temp_file, format="JPEG")
                    image_path = temp_file.name

                try:
                    result = client.run_workflow(
                        workspace_name="plantdiseasedetection1216",
                        workflow_id="plant-disease-detection-3-v3-logic",
                        images={"image": image_path},
                        use_cache=True
                    )
                finally:
                    os.remove(image_path)

            st.success("Analysis completed!")

            st.subheader("Detection Results")

            predictions = result[0].get(
                "predictions", {}
            ).get("predictions", [])

            if predictions:
                for prediction in predictions:
                    disease = prediction.get("class", "Unknown")
                    confidence = prediction.get("confidence", 0)

                    st.write(f"**Detected:** {disease}")
                    st.write(
                        f"**Confidence:** {confidence * 100:.2f}%"
                    )
                    st.progress(float(confidence))
                    st.divider()
            else:
                st.info("No disease detections were returned.")

            with st.expander("View raw model response"):
                st.json(result)

        except Exception as error:
            st.error(f"Something went wrong: {error}")

st.caption(
    "AI predictions are model outputs and should be verified "
    "before making plant-health decisions."
)
