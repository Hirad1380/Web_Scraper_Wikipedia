# --------------------------------- STEP 1 ---------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import requests
# import csv
# from collections import defaultdict, Counter

# id = 0

# def get_links(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', href=True)
#     return [link['href'] for link in links]

# def get_paragraphs(url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     paragraphs = soup.find_all('p')
#     driver.quit()
#     return [paragraph.text.strip().replace(',', ' ').replace('"', '') for paragraph in paragraphs]

# def main():
#     global id
#     base_url = 'https://en.wikipedia.org/wiki/Car' 
#     start_time = time.time()
#     end_time = start_time + 600
#     links = get_links(base_url)
#     with open('wikipedia222.csv', 'a', encoding='utf-8') as f:
#         f.seek(0, 2)
#         empty = f.tell() == 0
#         if empty:
#             f.write("ID,URL,Paragraphs\n")
#         for link in links:
#             if time.time() > end_time:
#                 break
#             full_url = base_url + link
#             print("-----------------------------------")
#             print("URL: ", full_url)
#             paragraphs = get_paragraphs(full_url)
#             for paragraph in paragraphs:
#                 id += 1
#                 f.write(f"{id},{full_url},{paragraph}\n")
#     print("Crawling completed.")
    
# if __name__ == "__main__":
#     main()



import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import csv
from collections import defaultdict, Counter

# id = 0

# def get_links(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', href=True)
#     return [link['href'] for link in links]

# def get_paragraphs(url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     paragraphs = soup.find_all('p')
#     driver.quit()
#     return [paragraph.text.strip().replace(',', ' ').replace('"', '') for paragraph in paragraphs]

# def main():
#     global id
#     base_url = 'https://en.wikipedia.org/wiki/Car'
#     start_time = time.time()
#     end_time = start_time + 60
#     links = get_links(base_url + '/wiki/Car') 
#     with open('wikipedia1.csv', 'a', encoding='utf-8') as f:
#         f.seek(0, 2)
#         empty = f.tell() == 0
#         if empty:
#             f.write("ID,URL,Paragraphs\n")
#         for link in links:
#             if time.time() > end_time:
#                 break
#             if link.startswith('https://'):
#                 full_url = link
#             else:
#                 full_url = base_url + link
#             print("-----------------------------------")
#             print("URL: ", full_url)
#             try:
#                 paragraphs = get_paragraphs(full_url)
#                 for paragraph in paragraphs:
#                     id += 1
#                     f.write(f"{id},{full_url},{paragraph}\n")
#             except Exception as e:
#                 print(f"Failed to process {full_url}: {e}")
#     print("Crawling completed.")

# if __name__ == "__main__":
#     main()





# --------------------------------- STEP 2 ---------------------------------


# with open('wikipedia1.csv', newline='', encoding='utf-8') as input_file, open('wikipedia1-1.csv', 'w', newline='', encoding='utf-8') as output_file:
#     reader = csv.DictReader(input_file)
#     fieldnames = ['ID', 'URL', 'Paragraphs']
#     writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
#     writer.writeheader()
    
#     grouped_rows = defaultdict(list)
    
#     for row in reader:
#         url = row['URL']
#         grouped_rows[url].append(row)
    
#     new_id = 1
    
#     for url, rows in grouped_rows.items():
#         combined_paragraphs = ' '.join(row['Paragraphs'] for row in rows)
#         writer.writerow({'ID': new_id, 'URL': url, 'Paragraphs': combined_paragraphs})
#         new_id += 1



# --------------------------------- STEP 3 ---------------------------------


# def find_word_rows(csv_file_path, column_index):
#     word_rows = defaultdict(list)
#     with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for row_index, row in enumerate(csv_reader, start=1):
#             if len(row) > column_index:  
#                 words = row[column_index].split()
#                 for word in words:
#                     word_rows[word].append(row_index)
#     return word_rows

# def save_word_rows_to_csv(word_rows, output_file_path):
#     with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(['Word', 'Row Count', 'Row IDs'])
#         for word, row_ids in word_rows.items():
#             row_count = len(row_ids)
#             csv_writer.writerow([word, row_count, '-'.join(map(str, row_ids))])

# file_path = 'wikipedia1-1.csv'
# column_index = 2  
# word_rows = find_word_rows(file_path, column_index)
# output_file_path = 'word_row_ids_with_count.csv'
# save_word_rows_to_csv(word_rows, output_file_path)
# print("CSV file with word row IDs and counts saved successfully.")

# def sort_csv(file_path, column_index):
#     with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         header = next(csv_reader)  
#         sorted_rows = sorted(csv_reader, key=lambda x: float(x[column_index]), reverse=True)

    
#     with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(header)
#         csv_writer.writerows(sorted_rows)

# file_path = 'word_row_ids_with_count.csv'  
# column_index = 1  
# sort_csv(file_path, column_index)
# print("CSV file sorted successfully.")



# --------------------------------- STEP 4 ---------------------------------

# number_counts = Counter()

# with open('word_row_ids_with_count.csv', newline='', encoding='utf-8') as input_file, open('Word_count.csv', 'w', newline='', encoding='utf-8') as output_file:
#     reader = csv.DictReader(input_file)
#     fieldnames = ['Word', 'Most Repeated Number', 'Count']
#     writer = csv.DictWriter(output_file, fieldnames=fieldnames)
#     writer.writeheader()

#     for row in reader:
#         word = row['Word']
#         row_ids = row['Row IDs'].split('-')

#         number_counts.clear() 
#         for row_id in row_ids:
#             number_counts[row_id] += 1

#         most_repeated_number = max(number_counts, key=number_counts.get)
#         highest_count = number_counts[most_repeated_number]

#         writer.writerow({'Word': word, 'Most Repeated Number': most_repeated_number, 'Count': highest_count})

# print("Output CSV file generated successfully.")