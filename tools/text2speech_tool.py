## Tool for text to speech
import replicate
#
def text2speech(text:str) -> str:
    """This tool is useful when we want to convert text to speech."""
    # Function logic here
    output = replicate.run(
    "cjwbw/seamless_communication:668a4fec05a887143e5fe8d45df25ec4c794dd43169b9a11562309b2d45873b0",
    input={
        "task_name": "T2ST (Text to Speech translation)",
        "input_text": text,
        "input_text_language": "English",
        "max_input_audio_length": 60,
        "target_language_text_only": "English",
        "target_language_with_speech": "English"
    }
    )
    return output["audio_output"]