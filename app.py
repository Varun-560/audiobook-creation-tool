import openai

# Set your API key (Replace with your own key or use environment variable)
openai.api_key = "YOUR_API_KEY"

def audio_to_text(file_path):
    """
    Convert audio file to text using OpenAI Whisper model.
    Supported formats: mp3, wav, m4a, webm
    """
    try:
        with open(file_path, "rb") as audio_file:
            transcript = openai.Audio.transcriptions.create(
                model="whisper-1",  # OpenAI Whisper model
                file=audio_file
            )
        return transcript["text"]
    except Exception as e:
        return f"Error: {e}"

if _name_ == "_main_":
    print("?? Audio to Text Converter")
    file_path = input("Enter the path of your audio file: ").strip()
    result = audio_to_text(file_path)
    print("\n--- Transcribed Text ---\n")
    print(result)