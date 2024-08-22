from gradio_client import Client
client = Client("https://lpinnova-whisper-model-speech-to-text2.hf.space/")
result = client.predict(
				"./mp3/CO_gratuit1_Q39.mp3",	# str (filepath or URL to file) in 'audio_path' Audio component
				api_name="/predict"
)

with open('output.txt', 'w') as file:
    file.write(result)
print(result)