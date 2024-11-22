import requests
from bs4 import BeautifulSoup
import csv

# Получаем HTML-код страницы
url = 'https://www.lrytas.lt/it'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Извлекаем заголовки статей из тегов <h2>
articles = [article.get_text(strip=True) for article in soup.find_all('h2')]

# Извлекаем изображения
images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]

# Извлекаем ссылки из тегов <a>
links = [(link.get_text(strip=True), link['href']) for link in soup.find_all('a') if 'href' in link.attrs]

# Сохраняем данные в CSV файл
with open('sorted_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'Image URL', 'Link Text', 'URL'])  # Заголовки столбцов

    max_length = max(len(articles), len(images), len(links))

    for i in range(max_length):
        article_text = articles[i] if i < len(articles) else ''
        image_url = images[i] if i < len(images) else ''
        link_text, link_url = links[i] if i < len(links) else ('', '')
        writer.writerow([article_text, image_url, link_text, link_url])

print("Данные успешно сохранены в файл sorted_data.csv")

def crawl(time_limit=60, source='lrytas', return_format='csv'):
    return None