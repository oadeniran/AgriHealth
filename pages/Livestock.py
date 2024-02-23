import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import numpy as np

labels = ['Healthy', 'Unhealthy']


def home():
    st.header("A demo of using AI to predict if a fowl is diseased based on poop")

    st.subheader("The data used was gotten from - https://www.kaggle.com/datasets/warcoder/poultry-birds-poo-imagery-dataset")

    st.subheader("This serves as a proof of concept and will require additional training and data for a more efficient model")

    st.subheader("To test the model, visit the website for the images above and pick from any category. Then download and upload")

def clf():
    img_f = st.file_uploader("Poultry poop Image", type=["png", "jpg"])
    if img_f is not None:
        with open(img_f.name, mode='wb') as f:
            f.write(img_f.getbuffer()) # save pdf to disk
        st.success("Image Uploaded.....")
        st.image(img_f.name, caption="Uploaded image", width=200)
        st.info("Predicting if poultry is diseased or not")
        im = Image.open(img_f.name)
        im = im.resize((64, 64))
        im = np.expand_dims(np.array(im), 0)
        res = round(model.predict(im)[0][0])
        st.success("Prediction complete")
        st.header(f"The prediction by the model is {labels[int(res)]}")

def real_time():
    cam_input = st.camera_input(label="Camera")
    if cam_input:
        st.image(cam_input)
        with open("cam_img.jpeg", mode='wb') as f:
            f.write(cam_input.getbuffer())
        st.info("Predicting if poultry is diseased or not")
        im = Image.open("cam_img.jpeg")
        im = im.resize((64, 64))
        im = np.expand_dims(np.array(im), 0)
        res = round(model.predict(im)[0][0])
        st.success("Prediction complete")
        st.header(f"The prediction by the model is {labels[int(res)]}")



model = tf.keras.models.load_model('poultry_model.hdf5')
st.title("Livestock Diseases classifier")

st.sidebar.title("Selecet livestock")
selection = st.sidebar.radio("Go to", ["Poultry", "More-coming-soon"])
if selection == "Poultry":
    home()
    sub_sel = st.sidebar.radio("Select Option", ["---", "Classify Image", "Realtime Classification"])
    if sub_sel == "Classify Image":
        home()
    elif sub_sel == "Classify Image":
        clf()
    elif sub_sel == "Realtime Classification":
        real_time()

else:
    st.info("MORE LIVESTOCKS COMING SOON ......")
