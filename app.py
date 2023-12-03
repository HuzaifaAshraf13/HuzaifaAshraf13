from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_news(api_key, country='us', category='general', num_articles=5):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'category': category,
        'apiKey': api_key,
        'pageSize': num_articles
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        news_data = response.json()

        if news_data['status'] == 'ok':
            return news_data['articles']
        else:
            return []

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return []
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return []
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return []
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news', methods=['GET'])
def fetch_news():
    api_key = 'WRITE YOUR API KEY HERE '
    country = request.args.get('country', 'us')
    category = request.args.get('category', 'general')
    num_articles = int(request.args.get('num_articles', 5))

    news_data = get_news(api_key, country, category, num_articles)

    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=True)
