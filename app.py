import  os
import logging
import streamlit as st
from PIL import Image
from settings import RESOURCES_DIR, DURATION, WAVE_OUTPUT_FILE
from src.sound import sound
from src.transcript import get_text_from_audio
from src.semantic_search import get_most_similars

##setup_logging()
logger = logging.getLogger('app')

def main():
    title = "Tell us how do you feel"
    text_from_audio = ''
    st.set_page_config(page_title=title,page_icon=None, layout='centered')
    st.title(title)
    image = Image.open(os.path.join(RESOURCES_DIR, 'hope.jpeg'))
    st.image(image, use_column_width=True)

    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            sound.record()
        st.success("Recording completed")

    if st.button('Play'):
        # sound.play()
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except:
            st.write("Please record sound first")



    if st.button('Get Text from Recording'):
      text_from_audio = get_text_from_audio(WAVE_OUTPUT_FILE)
      print("$$$"+text_from_audio)
      #save_image_from_prompt(text_from_audio)
      st.subheader("Text: "+text_from_audio)
      #st.write("Output Image")
      #output_image=image = Image.open(IMAGE_OUPUT_FILE)

      #st.image(output_image, use_column_width=True)
      
      #TODO: This will be consumed and diaplayed by fronted

    if st.button('Get recommendations'):
      results = get_most_similars(text_from_audio)
      for verse in results:
        st.text(verse)


if __name__ == '__main__':
    main()
