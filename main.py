import time
import requests

def get_http_metrics(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    metrics = {
        'status_code': response.status_code,
        'response_time': end_time  start_time,
        'headers': response.headers,
        'content_size': len(response.content)
    }

    return metrics

url = 'http://example.com'
metrics = get_http_metrics(url)

for key, value in metrics.items():
    print(f'{key}: {value}')
