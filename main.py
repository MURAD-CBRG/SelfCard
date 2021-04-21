from flask import Flask, render_template
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/member')
def personal_data_page():
    data = json.load(open('templates/data_base.json'))
    name = random.choice(list(data.keys()))

    params = {
        'title': 'Персональный данные участника экспедиции',
        'data': [name, [data[name][0], list(sorted(data[name][1]))]]
    }

    return render_template('personal_data_page.html', params=params)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
