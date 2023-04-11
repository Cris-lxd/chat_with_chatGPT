from flask import Flask, request, Response
from flask_cors import CORS
import openai
import markdown
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/getText', methods=['GET'])
def getText():
    text = request.args.get('text')

    result = chat(text)
    print(result)
    save_record(text,result)
    return Response(markdown.markdown(escape_markdown(result)), content_type='text/markdown', )


def chat(text):
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content


def save_record(text,result):
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M")
    with open('record.txt', 'a', encoding='utf-8') as file:
        file.write('\n\n\n\n' +
                   'time:' + str(now) +
                   'question:' + text + '\n' +
                   'answer:' + '\n' + result )


def escape_markdown(text):
    return text.replace('\\', '\\\\').replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace(']', '\\]').replace('(', '\\(').replace(')', '\\)').replace('~', '\\~').replace('`', '\\`').replace('>', '\\>').replace('#', '\\#').replace('+', '\\+').replace('-', '\\-').replace('=', '\\=').replace('|', '\\|').replace('{', '\\{').replace('}', '\\}').replace('.', '\\.')


if __name__ == '__main__':
    app.run(port=8081)
