import streamlit as st
import pickle

# Load the model
model = pickle.load(open('new_gestational.pkl', 'rb'))

# Function to classify the input
def classify(input_data):
    # Perform classification using the loaded model
    prediction = model.predict(input_data)
    return prediction

def main():
    st.title("Gestational Diabetes Prediction")
    html_temp = """
    <div style="background-color: #F0F8FF; padding: 10px;">
        <h2 style="color: #800000; text-align: center;">Gestational Diabetes Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input sliders for features
    age = st.slider('Age', 10, 100)
    no_of_pregnancy = st.slider('Number of Pregnancies', 0, 20)
    # Add sliders for other features

    # Collect input data
    input_data = [[age, no_of_pregnancy]]  # Add other features here

    if st.button('Classify'):
        # Perform classification
        result = classify(input_data)
        # Display the result
        st.success('Prediction: {}'.format(result))

if __name__ == '__main__':
    main()
