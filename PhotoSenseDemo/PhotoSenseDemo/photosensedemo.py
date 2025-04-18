import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from streamlit_extras.buy_me_a_coffee import button as buymeacoffee_button

st.set_page_config(page_title="Prototype for a Standalone Image Clustering App", layout="wide")
st.title("🧠 Prototype for a Simple Standalone Image Clustering App")

# Upload images
uploaded_files = st.file_uploader(
    "Upload image files to cluster (JPG, PNG, JPEG)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

def extract_features(img, bins=(8, 8, 8)):
    """Extract color histogram as features."""
    img = img.resize((128, 128)).convert("RGB")
    arr = np.array(img)
    hist = np.histogramdd(
        arr.reshape(-1, 3), bins=bins, range=[(0, 256)] * 3, density=True
    )[0]
    return hist.flatten()

if uploaded_files:
    with st.expander('### 📷 Image Previews'):
        cols = st.columns(8)
        images = []
        features = []

        for idx, file in enumerate(uploaded_files):
            image = Image.open(file)
            images.append((file.name, image))
            features.append(extract_features(image))
            with cols[idx % 8]:
                st.image(image, caption=file.name, use_container_width=True)

    if st.button("🔍 Cluster Images"):
        with st.expander('Cluster Images'):
            with st.spinner("Extracting features and clustering..."):

                X = np.array(features)

                # Choose number of clusters (or make it a slider later)
                n_clusters = min(5, len(images))  # up to 5 clusters
                model = KMeans(n_clusters=n_clusters, random_state=42)
                labels = model.fit_predict(X)

                # Combine with image info
                clustered = list(zip(images, labels))
                clustered.sort(key=lambda x: x[1])  # sort by cluster

                st.markdown("### 🔢 Clustered Images")
                cluster_cols = st.columns(8)
                previous_label = None
                counter = 0

                for idx, ((fname, img), label) in enumerate(clustered):
                    if previous_label is not None and label != previous_label:
                        cluster_cols = st.columns(8)
                        counter = 0
                        st.divider()
                    with cluster_cols[counter % 8]:
                        st.image(img, caption=f"{fname}", use_container_width=True)
                    previous_label = label
                    counter = counter + 1

    buymeacoffee_button(username="erdogant", floating=True)
