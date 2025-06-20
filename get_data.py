import requests

url = 'https://download.microsoft.com/download/3/e/1/3e1c3f21-ecdb-4869-8368-6deba77b919f/kagglecatsanddogs_5340.zip'
output_path = 'kagglecatsanddogs_5340.zip'

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

print(f"Arquivo baixado em: {output_path}")