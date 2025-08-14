import streamlit as st
from utils import generate_and_speak

st.set_page_config(
    page_title="EchoVerse LLM + TTS",
    page_icon="🗣️",
    layout="centered"
)

st.title("🗣️ EchoVerse LLM + TTS")
st.markdown("Enter a prompt and hear the AI speak it back!")

user_input = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Type something for the AI to say...",
    height=150
)

lang_input = st.selectbox("Language", ["en", "hi", "es", "fr"], index=0)

if st.button("🎤 Generate & Speak", use_container_width=True):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        try:
            with st.spinner("Generating response and audio..."):
                generated_text, audio_bytes = generate_and_speak(user_input, lang=lang_input)

            if generated_text.strip():
                st.subheader("📖 Generated Text")
                st.write(generated_text)
            else:
                st.error("❌ Failed to generate text.")

            if audio_bytes:
                st.subheader("🔊 Audio Output")
                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="Download MP3",
                    data=audio_bytes,
                    file_name="echoverse_tts.mp3",
                    mime="audio/mpeg"
                )
            else:
                st.error("❌ Failed to generate audio.")

        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

st.markdown("---")
st.caption("Powered by Granite LLM + Google TTS")
