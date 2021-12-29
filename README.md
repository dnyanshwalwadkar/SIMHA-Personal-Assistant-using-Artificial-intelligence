# SIMHA-Personal-Assistant-using-Artificial-intelligence
Personal Assistant Using Artificial intelligence

The rise of automation, along with increased computational power, novel application of statistical algorithms, and improved accessibility to data, have resulted in the birth of the personal digital assistant market, popularly represented by Apple’s Siri, Microsoft’s Cortana, Google’s Google Assistant, and Amazon’s Alexa.

While each assistant may specialize in slightly different tasks, they all seek to make the user’s life easier through verbal interactions so you don’t have to search out a keyboard to find answers to questions like “What’s the weather today?” or “Where is Switzerland?”. Despite the inherent “cool” factor that comes with using a digital assistant, you may find that the aforementioned digital assistants don’t cater to your specific needs. Fortunately, it’s relatively easy to build your own

![alt text](https://github.com/dnyanshwalwadkar/SIMHA-Personal-Assistant-using-Artificial-intelligence/blob/master/how-to-build-a-digital-virtual-assistant-in-python.png)
## Speech Recognition Package – 
when you voice a question, we’ll need something that can capture it. The SpeechRecognition package allows Python to access audio from your machine’s microphone, transcribe audio, save audio to an audio file, and other similar tasks.

## Text to Speech Package – 
our assistant will need to convert your voiced question to a text one. And then, once the assistant looks up an answer online, it will need to convert the response into a voiceable phrase. For this purpose, we’ll use the gTTS package (Google Text-to-Speech). This package interfaces with Google Translate’s API. More information can be found here.

## Audio Playback Package –
All that’s left is to give voice to the answer. The mpyg321 package allows for Python to play MP3 files.
