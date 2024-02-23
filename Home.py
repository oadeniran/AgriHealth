import streamlit as st
import tensorflow as tf

if __name__ == "__main__":
    if "corn_model" not in st.session_state:
        corn_model = tf.keras.models.load_model('corn_model.hdf5')
        poultry_model = model = tf.keras.models.load_model('poultry_model.hdf5')
        st.session_state["corn_model"] = corn_model
        st.session_state["poultry_model"] = poultry_model

    st.title("AgriHealth Watch")

    st.write('''Welcome to Agri Health Watch!
             At Agri Health Watch, we are dedicated to revolutionizing the way we approach disease management in agriculture. Our mission is to empower farmers and agricultural stakeholders with cutting-edge predictive analytics to safeguard the health of livestock and crops.
With our innovative platform, users can access real-time insights and forecasts to anticipate and mitigate the impact of diseases on their agricultural produce. By harnessing the power of data science and machine learning, we provide actionable recommendations that enable proactive decision-making and promote sustainable farming practices.

Whether you're a small-scale farmer or a large agricultural enterprise, Agri Health Watch is your trusted partner in promoting the health and resilience of your agricultural ecosystem. Join us in our mission to cultivate healthier crops, protect livestock, and build a more sustainable future for agriculture.

Explore our platform to discover how Agri Health Watch can empower you to take control of disease management in agriculture and optimize your farming operations. Together, let's build a healthier, more resilient agricultural landscape for generations to come.''')

st.title("How to Test Demo")
st.subheader("1. Select what you want to classify (Livestock or Crop)")
st.subheader("2. Select classification method: ")
st.subheader("3. Visit the website that contains the images used for the training and select any image from any class (Kaggle acct needed)")
st.subheader("4. Download the selected image to device then go back to app")
st.subheader("5. Upload the just downloaded image and the model predicts")

st.title("How to Use")
st.subheader("1. Select what you want to classify (Livestock or Crop)")
st.subheader("2. Select classification method: ")
st.markdown("Classify image option: For pre-existing image already on device")
st.markdown("Realtime-classification option: For pre-existing image already on device")
st.subheader("3. Upload file if classify-image option was selected or take picture with camera if realtime-classification option was selected")