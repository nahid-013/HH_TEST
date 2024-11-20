import requests
from bs4 import BeautifulSoup
import csv
def fetch_animal_counts(url):
    url = url
    animal_counts = {}
    flag = True
    while flag:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        main = soup.find("div", id="mw-pages").find_all("div", "mw-category-group")
        for row in main:
            links = [link.find('a').get_text() for link in row.find_all('li')]
            for i2 in links:
                animal_counts[row.find('h3').get_text()] = animal_counts.get(row.find('h3').get_text(), 0)+1
            next_page = soup.find("a", text="Следующая страница").get("href")
            if not row.find('h3').get_text() == 'A':
                url = 'https://ru.wikipedia.org' + next_page
            else:
                return animal_counts

def save_to_csv(animal_counts, filename='beasts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(animal_counts.keys()):
            writer.writerow([letter, animal_counts[letter]])


if __name__ == "__main__":
    print("Ожидайте...")
    animal_counts = fetch_animal_counts('https://ru.wkipedia.org/wiki/Категория:Животные_по_алфавиту')
    print(animal_counts)
    save_to_csv(animal_counts)
    print("Данные сохранены в beasts.csv")