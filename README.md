# AgriHealth
Test it out - https://agrihealth.streamlit.app
## Inspiration
As a Nigerian, I've witnessed a significant rise in prices and inflation across all sectors, particularly affecting food prices. Food, being one of life's essentials, is experiencing soaring prices, contributing to increased hunger and poverty among families. This is directly at odds with Sustainable Development Goals 1 and 2, which aim to eradicate poverty and hunger, respectively.

Our vision is to bolster local food production, encompassing both livestock and crops, to drive sustainable development in our country. By reducing dependency on foreign imports, which is a primary driver of escalating food prices amidst a deteriorating economy, we aim to create a more resilient food system.

## What it does
The AgriHealth project empowers farmers and other stakeholders in agriculture with a tool to combat crippling diseases in agricultural produce. Using computer vision technology, the tool predicts the health status of crops and livestock based on images sourced directly from the agricultural produce.

## How we built it
This project is built on Python and machine learning techniques, specifically leveraging convolutional neural networks (CNNs) implemented with TensorFlow. We trained deep learning models on specialized datasets tailored to each specific prediction task. These models were then deployed using Streamlit, providing a user-friendly frontend where stakeholders can upload images or capture real-time photos using their mobile devices. The images are processed through the respective model, and the predictions are returned to users, empowering them to make informed decisions about their livestock or crops.

## Challenges we ran into
One of the main challenges we encountered was sourcing appropriate datasets for training. While platforms like Kaggle offer valuable datasets, we found a scarcity of graphical datasets related to livestock diseases. Similarly, datasets for crop diseases were limited, with many relying on tabular data for predictions. Moving forward, expanding and refining our dataset collection will be crucial for enhancing the project's efficacy.

## Performance optimization was another challenge. Although we achieved accuracy levels of 80% and above, further improvements are needed, requiring additional training time and resources which were constrained by our timeframe.

## Accomplishments that we're proud of
We take pride in successfully deploying the model for public use in real-time. Deploying deep learning models can be resource-intensive, but overcoming this challenge signifies a significant achievement for our project.

# What's next for AgriHealth
Looking ahead, there are several avenues for improving the AgriHealth project. Two key areas of focus include:

Expansion of livestock and crop categories to broaden the tool's applicability.
Integration of chatbots, such as OpenAI, to provide real-time feedback based on model predictions, enhancing user interaction and usability.
