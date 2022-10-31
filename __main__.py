from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

from text_to_speech.constants_config.constants import (index_html,
                                                       key_of_data, port, host)
from text_to_speech.text_to_speech_conversion import TextConversion

app = Flask(__name__)
CORS(app)

text_conversion = TextConversion()


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template(index_html)


@app.route("/predict", methods=['POST'])
@cross_origin()
def convert():
    data = request.json[key_of_data]
    if len(data) != 0:
        result = text_conversion.text_to_bytes(data)
        return {key_of_data: text_conversion.bytes_to_audio(byte_data=result)}
    else:
        return dict(error="in text")


if __name__ == "__main__":
    app.run(host=host, port=port)
