
import streamlit as st
from gtts import gTTS
import io
from datetime import datetime

st.set_page_config(page_title="SpeechStreamlit App", page_icon=":microphone:")

st.title("SpeechStreamlit App — Text to Speech")
st.write("Convert text to speech using the gTTS library. Requires internet access.")

text = st.text_area("Enter text to convert to speech", value="Welcome to data science AI", height=160)

lang_display = {"en": "English", "hi": "Hindi", "es": "Spanish", "fr": "French"}
lang = st.selectbox("Language", options=list(lang_display.keys()), format_func=lambda k: lang_display[k])

tld = st.selectbox("TLD (affects voice accent)", options=["com", "co.uk", "ca", "com.au"], index=0)

filename = f"speech_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"

col1, col2 = st.columns([3, 1])
with col1:
	generate = st.button("Generate Speech")
with col2:
	st.write("")

if generate:
	if not text.strip():
		st.error("Please enter some text to convert.")
	else:
		try:
			with st.spinner("Generating speech..."):
				tts = gTTS(text=text, lang=lang, tld=tld)
				mp3_fp = io.BytesIO()
				tts.write_to_fp(mp3_fp)
				mp3_fp.seek(0)
			st.success("Speech generated")
			# Play the generated audio
			st.audio(mp3_fp.read(), format="audio/mp3")
			# Reset pointer for download
			mp3_fp.seek(0)
			st.download_button("Download MP3", data=mp3_fp, file_name=filename, mime="audio/mpeg")
		except Exception as e:
			st.error(f"An error occurred while generating speech: {e}")

st.markdown("---")
st.write("Notes: gTTS uses Google Translate's TTS and requires an internet connection. Language options are a subset — use language codes supported by gTTS.")
