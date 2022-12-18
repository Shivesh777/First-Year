import streamlit as st
from PIL import Image

SEEDLING_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/65/seedling_1f331" \
                     ".png "
page_title = "Weed Detector"

# Set page title and favicon.
st.set_page_config(
    page_title=page_title,
    page_icon=SEEDLING_EMOJI_URL
)


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://get.wallhere.com/photo/sunlight-trees-landscape-hill-nature-grass-sky-field-photography-green-morning-farm-atmosphere-steppe-grassland-pasture-agriculture-meadow-plantation-plain-1920x1080-px-lawn-highland-prairie-crop-rural-area-computer-wallpaper-atmosphere-of-earth-ecosystem-grass-family-ecoregion-789185.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

# Cache model and class indices loading
# @st.cache
# def load_model():
#     with open(class_indices_path) as json_file:
#         class_indices = json.load(json_file)

#     model = tf.keras.models.load_model(model_path)
#     return model, class_indices


# Display markdown content
"""
# Weed Detector
Text here
---
"""

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.markdown(
        "Here are [some images](https://drive.google.com/drive/folders/13gjzw--osiXXZdIrhtyzB6WvCtHY36Wj?usp=sharing) you could try using!")
else:
    pass
    # image = Image.open(file)
    # st.image(image, use_column_width=True)

    # image = image.resize((224, 224))
    # image = np.expand_dims(np.asarray(image), axis=0) / 255

    # model, class_indices = load_model()
    # predictions = model(image)

    # class_indices = {v: k for (k, v) in class_indices.items()}
    # predicted_label = str(class_indices[np.argmax(predictions)])
    # species, disease = predicted_label.split("__")

    # st.subheader(f"This leaf is of a {species} plant")
    # if disease == "healthy":
    #     st.subheader("This plant is healthy ✔")
    # else:
    #     disease_name = disease.replace("_", " ")
    #     st.subheader(f"This plant is suffering from {disease_name}")
