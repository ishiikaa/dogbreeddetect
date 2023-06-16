# dogbreeddetect
This code is a Python script that implements a web application using Streamlit. The application is called "The Dog Breed Detector" and allows users to upload an image of a dog and get information about the predicted breed of the dog and its endangered status.

Here's an explanation of the code

It imports the necessary libraries:

streamlit is a framework for building interactive web applications.
numpy is a library for numerical computations.
tensorflow.keras.preprocessing provides image preprocessing utilities.
tensorflow.keras.applications.resnet50 contains the ResNet50 model for image classification.
pandas is a library for data manipulation and analysis.
PIL (Python Imaging Library) provides image processing capabilities.
It loads the IUCN Red List of Threatened Species dataset from a CSV file called "red_list.csv" using pd.read_csv() function.

It loads the ResNet50 model with pre-trained weights from the ImageNet dataset using ResNet50(weights='imagenet').

It defines a function called get_breed_status(file_path) that takes a file path to an image as input. Inside the function:

It loads and preprocesses the image using image.load_img() and image.img_to_array() functions.
It makes predictions on the preprocessed image using the ResNet50 model.
It decodes the predictions to obtain the top 3 predicted labels using decode_predictions() function.
It extracts the breed name from the top predicted label.
It retrieves the endangered status of the breed from the loaded Red List dataset.
It constructs a result string that includes the predicted breed name and its endangered status.
It returns the result string.
It defines a function called main() that serves as the entry point of the Streamlit web application. Inside the function:

It sets the page configuration using st.set_page_config() to define the title, layout, and initial sidebar state.
It displays the title and a subheader of the web application.
It allows the user to select and upload an image file using st.file_uploader().
If an image file is uploaded, it calls the get_breed_status() function to get the predicted breed and endangered status.
It displays the result string and the selected image using st.text() and st.image() respectively.
It provides general information about dogs using the st.markdown() function.
It checks if the script is being executed directly (not imported as a module) and calls the main() function in that case.

This script combines machine learning (ResNet50 model) with web development (Streamlit) to create an application that can predict the breed of a dog based on an uploaded image and provide information about its endangered status.






