from flask import Flask, render_template, request
import openai
import requests
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# set up OpenAI API credentials
openai.api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        url = response["data"][0]["url"]
        image_data = requests.get(url).content
        img = Image.open(BytesIO(image_data))
        img_data = BytesIO()
        img.save(img_data, "JPEG")
        img_data.seek(0)
        return render_template('index.html', image_data=img_data.getvalue())
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
