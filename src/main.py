import os
from gradio_client import Client

# Initialize the Gradio API client
client = Client("https://lpinnova-whisper-model-speech-to-text2.hf.space/")

# Define the paths to the MP3 folder and the output folder
mp3_folder = "./mp3/"
output_folder = "./output/"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the MP3 folder
for filename in os.listdir(mp3_folder):
    if filename.endswith(".mp3"):
        # Construct the file path
        file_path = os.path.join(mp3_folder, filename)

        # Convert the audio to text using the Gradio API
        result = client.predict(file_path, api_name="/predict")
        print(result)
        # Construct the output TXT file path (same name as the MP3 file but in the output folder)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

        # Write the result to the corresponding TXT file in the output folder
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(result)

        print(f"Processed {filename}, result saved to {output_file_path}")
