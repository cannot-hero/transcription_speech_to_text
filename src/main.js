import { Client } from '@gradio/client';
const test1 = Bun.file('./mp3/CO_gratuit1_Q01.mp3');
const audioBlob = new Blob([test1], { type: 'audio/mpeg' });
const app = await Client.connect(
    'https://lpinnova-whisper-model-speech-to-text2.hf.space/'
);
const result = await app.predict('/predict', [
    audioBlob, // blob in 'audio_path' Audio component
]);

console.log(result.data);
