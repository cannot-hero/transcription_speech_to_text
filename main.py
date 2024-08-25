import os
import shutil
from gradio_client import Client

def clear_output_folder(output_folder):
    if os.path.exists(output_folder):
        # Remove all files in the output folder
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        os.makedirs(output_folder)  # Create the folder if it doesn't exist

def convert_audio_to_text(mp3_folder, output_folder, api_url):
    # Clear the output folder before processing
    clear_output_folder(output_folder)

    # Initialize the Gradio API client
    client = Client(api_url)

    # Supported file extensions
    supported_extensions = ['.mp3', '.wav', '.WAV']

    # Iterate through all files in the MP3 folder
    for filename in os.listdir(mp3_folder):
        if any(filename.endswith(ext) for ext in supported_extensions):
            # Construct the file path
            file_path = os.path.join(mp3_folder, filename)

            # Convert the audio to text using the Gradio API
            result = client.predict(file_path, api_name="/predict")

            # Construct the output TXT file path (same name as the audio file but in the output folder)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            # Write the result to the corresponding TXT file in the output folder with utf-8 encoding
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(result)

            print(f"Processed {filename}, result saved to {output_file_path}")

if __name__ == '__main__':
    mp3_folder = "./mp3/"
    output_folder = "./output/"
    api_url = "https://lpinnova-whisper-model-speech-to-text2.hf.space/"

    convert_audio_to_text(mp3_folder, output_folder, api_url)
