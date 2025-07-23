import streamlit as st
import numpy as np
from PIL import Image
import numpy as np
from model import generate_prompt, get_model_resp

datasets_link = {
    'Corn': 'https://www.kaggle.com/datasets/responsibleailab/crop-disease-ghana',
    'Maize' : 'https://www.kaggle.com/datasets/gauravduttakiit/makerere-fall-armyworm-crop-challenge'
}

all_labels = {
    'Corn' : {0: 'Corn__Cercospora_Leaf_Spot',
 1: 'Corn__Common_Rust',
 2: 'Corn__Healthy',
 3: 'Corn__Northern_Leaf_Blight',
 4: 'Corn__Streak'}, 

 "Maize" : {
    0: "Not affected by Armyworm",
    1: "Affected by Armyworm"
}
}

def home(selection):
    st.header(f"A demo of using AI to predict if {selection} plant is diseased based on leave image")

    st.subheader(f"The data used was gotten from - {datasets_link[selection]}")

    st.subheader("This serves as a proof of concept and will require additional training and data for a more efficient model")

    st.subheader("To test the model, visit the website for the images above and pick from any category. Then download and upload")

def clf(selection, model, labels):
    img_f = st.file_uploader(f"{selection}-image", type=["png", "jpg"])

    if img_f is not None:
        with open(img_f.name, mode='wb') as f:
            f.write(img_f.getbuffer()) # save png to disk
        st.success("Image Uploaded.....")
        st.image(img_f.name, caption="Uploaded image", width=200)
        st.info(f"Predicting if {selection} is diseased or not")
        im = Image.open(img_f.name)
        im = im.resize((64, 64))
        im = np.expand_dims(np.array(im), 0)

        if selection == 'Corn':
            res = model.predict(im)
            print(res)
            pred = np.argmax(res)
        else:
            res = round(model.predict(im)[0][0])
            pred = res
        
        st.success("Prediction complete")
        st.header(f"The prediction by the model is {labels[int(pred)]}")
        return labels[int(pred)]
        

def real_time(selection, model, labels):
    cam_input = st.camera_input(label="Camera")
    if cam_input:
        st.image(cam_input)
        with open("cam_img.jpeg", mode='wb') as f:
            f.write(cam_input.getbuffer())
        st.info(f"Predicting if {selection} is diseased or not")
        im = Image.open("cam_img.jpeg")
        im = im.resize((64, 64))
        im = np.expand_dims(np.array(im), 0)
        res = model.predict(im)
        pred = np.argmax(res)
        st.success("Prediction complete")
        st.header(f"The prediction by the model is {labels[int(pred)]}")
        return labels[int(pred)]

def run_selection(selection):
    if selection == "More-coming-soon":
        st.info("MORE CROPS COMING SOON ......")
    elif selection not in ['Corn', "Maize"] and selection != "More-coming-soon":
        st.info("MODEL IN PROGRESS ......")
    else:
        home(selection)
        sub_sel = st.sidebar.radio("Select Option", ["---", "Classify Image", "Realtime Classification"])
        if sub_sel == "Classify Image":
            result = clf(selection, st.session_state[f"{selection}_model"], all_labels[selection])
            if result != None:
                with st.spinner("Generating Analysis...."):
                    prompt = generate_prompt(selection, result)
                    print(prompt)
                    response = get_model_resp(prompt)
                    st.write(response)
        elif sub_sel == "Realtime Classification":
            result = real_time(selection, st.session_state[f"{selection}_model"],  all_labels[selection])

st.title("Crop Diseases classifier")

st.sidebar.title("Selecet Crop")
selection = st.sidebar.radio("Go to", ["Corn", "Maize", "Pepper", "Tomato", "More-coming-soon"])
run_selection(selection)