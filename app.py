import streamlit as st
from streamlit_drawable_canvas import st_canvas
from inference import pipeline  

from PIL import Image
import numpy as np

st.set_page_config(layout="wide")
# Define two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Draw your doodle here 👇")

    canvas_result = st_canvas(
        fill_color="white",  # Default fill color
        stroke_width=3,
        stroke_color="black",
        background_color="white",
        update_streamlit=True,
        height=400,
        width=400,
        drawing_mode="freedraw",
        key="canvas"
    )

    submit = st.button("🧠 Classify Doodle")

with col2:
    st.header("🔍 Classification Result")
    
    if submit and canvas_result.image_data is not None:
        # Convert image to 128x128 
        img = Image.fromarray((canvas_result.image_data).astype(np.uint8)).convert("RGB").resize((128, 128))
        
        # Call the pipeline function
        prediction = pipeline(img)
        
        st.success(f"## {prediction}")

    elif not submit:
        st.write("Draw something and hit the button!")

