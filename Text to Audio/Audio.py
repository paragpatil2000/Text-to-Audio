from gtts import gTTS
import os

# Define the text to be converted to speech
text = "Hi I am Parag Patil. I am a software developer and I am working on Python and machine learning projects..."

# Create a gTTS object
tts = gTTS(text=text, lang='en', slow=False)

# Save the audio file
output_path = "static/output.mp3"  # Save in the 'static' directory
tts.save(output_path)

print(f"Audio file saved at {output_path}")
