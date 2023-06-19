import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import pandas as pd
from PIL import Image

# Load the IUCN Red List of Threatened Species dataset
red_list = pd.read_csv('red_list.csv')
# Load the ResNet50 model
model = ResNet50(weights='imagenet')

# Define function to get the dog breed and its endangered status
def get_breed_status(file_path):
    img = image.load_img(file_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded_preds = decode_predictions(preds, top=3)[0]
    breed_name = decoded_preds[0][1]
    endangered_status = red_list.loc[red_list['common name'] == breed_name]['red list status'].values
    if len(endangered_status) > 0:
        result = "Predicted dog breed: " + breed_name + "\nEndangered status: " + endangered_status[0]
    else:
        result = "Predicted dog breed: " + breed_name + "\nEndangered status: Not Endangered"
    return(result)

# Create a Streamlit app
def main():
    # Set page config
    st.set_page_config(
        page_title="Statistical Analysis Of Living Organisms",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Display title
    st.title("The Dog Breed Detector")
    st.subheader("Detect your favorite dogs with ease")

    # Select and display an image
    file_path = st.file_uploader("Select an image", type=["jpg", "jpeg", "png", "jfif"])
    if file_path is not None:
        result = get_breed_status(file_path)
        st.text(result)
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Resizes the image proportionally to fit in a 400x400 box
        st.image(img, caption="Selected Image")

    # Provide information about dogs
    st.markdown("""
        Dogs are a beloved pet all over the world, known for their loyalty and affection towards humans. 
        They are a domesticated species of the Canidae family, originally descended from wolves. While they 
        are commonly kept as house pets, dogs are also well-suited to living in a range of habitats, 
        including forests, grasslands, and deserts. Their natural habitat varies depending on the breed, 
        but most dogs prefer environments with moderate temperatures and access to water.
        
        Dogs are found all over the world and are popular in most cultures. They are highly adaptable and 
        can be found in almost any country or region, from the Arctic Circle to tropical islands. In terms 
        of lifespan, the average dog can live up to 12 years, but this varies greatly depending on factors 
        such as breed, size, and overall health. Some breeds can live up to 20 years or more, while others 
        may only survive for a few years. Overall, dogs are a highly varied and interesting species with a 
        long history of companionship with humans.
    """)


if __name__ == "__main__":
    main()
