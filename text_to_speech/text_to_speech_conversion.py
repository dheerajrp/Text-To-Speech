"""
Conversion of the text to audio.
"""
from gtts import gTTS
import base64

from text_to_speech.constants_config.constants import \
    (language_selection_english, slow_format_audio, audio_file_name,
     open_audio_format, language_top_level_domain, decoding_format)


class TextConversion:
    @staticmethod
    def text_to_bytes(data: str) -> bytes:
        """
        Converts the text to base64 format.

        Args:
            data (str):
                The input data.

        Returns:
             bytes:
                Base64 format of the data.
        """
        tts = gTTS(text=data,
                   lang=language_selection_english,
                   tld=language_top_level_domain,
                   slow=slow_format_audio)
        tts.save(savefile=audio_file_name)
        with open(audio_file_name, open_audio_format) as file:
            base64_string = base64.b64encode(file.read())
        return base64_string

    @staticmethod
    def bytes_to_audio(byte_data: bytes) -> str:
        """
        Converts the byte data to the audio format.

        Args:
            byte_data (bytes):
                The base64 format of the data.

        Returns:
             str:
                The string format of the data.
        """
        return byte_data.decode(decoding_format)
