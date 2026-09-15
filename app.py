import streamlit as st
import pickle
import numpy as np

# Page settings
st.set_page_config(
    page_title="Student Admission System",
    page_icon="🎓",
    layout="centered"
)

# Load trained model
model = pickle.load(open("Admission_model.pkl", "rb"))

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}

.stButton > button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #007B83;
}
</style>
""", unsafe_allow_html=True)


# Title
st.title("🎓 Student Admission Prediction System")
st.write("Enter student information to predict admission eligibility.")


# Student Information
with st.container():

    Name = st.text_input("Enter Name")

    Age = st.number_input(
        "Enter Age",
        min_value=0,
        max_value=100,
        value=None,
        placeholder="Enter age"
    )

    Marks = st.number_input(
        "Enter Marks",
        min_value=0,
        max_value=1000,
        value=None,
        placeholder="Enter marks"
    )

    Subject = st.selectbox(
        "Select Subject",
        [
            "",
            "Pre-Engineering",
            "Computer Science",
            "Pre-Medical",
            "Arts"
        ]
    )


# Prediction button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button("Predict Admission"):

        # Validation
        if not Name:
            st.warning("Please enter Name.")

        elif Age is None:
            st.warning("Please enter Age.")

        elif Marks is None:
            st.warning("Please enter Marks.")

        elif Subject == "":
            st.warning("Please select Subject.")

        else:

            # Subject encoding
            Subject_Computer = 1 if Subject == "Computer Science" else 0
            Subject_Math = 1 if Subject == "Pre-Engineering" else 0
            Subject_Medical = 1 if Subject == "Pre-Medical" else 0

            # Prepare input data
            data = np.array([[
                Age,
                Marks,
                Subject_Computer,
                Subject_Math,
                Subject_Medical
            ]])

            # Prediction
            prediction = model.predict(data)

            # Display result
            if prediction[0] == 1:
                st.success("✅ Eligible for Admission")
            else:
                st.error("❌ Not Eligible")