# 📖 Wikipedia Web Crawler & Word Frequency Analyzer

A multi-step web crawling and text analysis pipeline that **crawls Wikipedia pages**, extracts and processes paragraph content, builds a **word frequency index**, and identifies which pages mention each word most. Results are displayed in a clean **browser-based CSV viewer** with real-time search.

---

## ✨ Features

### 🤖 Crawler & Analyzer (Python)
- Crawls Wikipedia starting from any article and follows all its links
- Extracts full paragraph content from each linked page using **headless Chrome**
- Multi-step data processing pipeline:
  - Raw crawl → grouped by URL → word index → frequency analysis
- Built-in **time limit** to control crawl duration
- Exports results at each stage to structured **CSV files**

### 🌐 CSV Viewer (Browser UI)
- Upload any output CSV directly in the browser
- Displays data in a formatted **HTML table**
- **Real-time search** — filters rows instantly as you type
- **Keyword highlighting** — matched text is visually highlighted
- Zero dependencies — pure HTML, CSS, Vanilla JavaScript

---

## 🔁 Pipeline — 4 Steps

```
STEP 1: Crawl
─────────────
Start URL (e.g. /wiki/Car)
    ↓
Extract all links from the page
    ↓
Visit each link with headless Selenium
    ↓
Extract paragraphs with BeautifulSoup
    ↓
Save → wikipedia1.csv  (ID, URL, Paragraphs)


STEP 2: Clean & Group
──────────────────────
wikipedia1.csv
    ↓
Group all paragraphs by URL
    ↓
Merge into one row per page
    ↓
Save → wikipedia1-1.csv  (ID, URL, Combined Paragraphs)


STEP 3: Build Word Index
─────────────────────────
wikipedia1-1.csv
    ↓
For each word → find all row IDs that contain it
    ↓
Count occurrences & sort by frequency
    ↓
Save → word_row_ids_with_count.csv  (Word, Row Count, Row IDs)


STEP 4: Find Dominant Page per Word
─────────────────────────────────────
word_row_ids_with_count.csv
    ↓
For each word → find which page ID mentions it most
    ↓
Save → Word_count.csv  (Word, Most Repeated Number, Count)
```

---

## 🛠️ Tech Stack

| Category        | Technology                               |
|-----------------|------------------------------------------|
| Crawling        | Python, Selenium (headless), Requests    |
| Parsing         | BeautifulSoup4                           |
| Data Processing | Python CSV, collections (Counter, defaultdict) |
| UI              | HTML5, CSS3, Vanilla JavaScript          |
| Browser Parser  | FileReader API, DOM Manipulation         |

---

## 📁 Project Structure

```
Web_Scraper_Wikipedia/
│
├── wikipedia.py   # Full 4-step crawl & analysis pipeline
├── index.html     # CSV Viewer UI — upload, display, search
├── script.js      # FileReader, table rendering & search/highlight logic
└── style.css      # Styling for the viewer interface
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Google Chrome + ChromeDriver (matching your Chrome version)

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Hirad1380/Web_Scraper_Wikipedia.git
cd Web_Scraper_Wikipedia

# 2. Install dependencies
pip install selenium beautifulsoup4 requests
```

### Run the Pipeline

**Step 1 — Crawl Wikipedia:**
```python
# In wikipedia.py, change the base URL to any Wikipedia article:
base_url = 'https://en.wikipedia.org/wiki/Car'
```
Uncomment Step 1 code block, then:
```bash
python wikipedia.py
```

**Steps 2, 3, 4 — Process the data:**

Uncomment each step one at a time and run:
```bash
python wikipedia.py
```

### View Results
1. Open `index.html` in your browser
2. Upload any generated CSV file
3. Search and explore the data

---

## 📊 CSV Output Files

| File | Columns | Description |
|------|---------|-------------|
| `wikipedia1.csv` | ID, URL, Paragraphs | Raw crawl — one row per paragraph |
| `wikipedia1-1.csv` | ID, URL, Paragraphs | Cleaned — one row per page |
| `word_row_ids_with_count.csv` | Word, Row Count, Row IDs | Inverted word index |
| `Word_count.csv` | Word, Most Repeated Number, Count | Dominant page per word |

---

## ⚠️ Notes

> - The crawler runs for a **limited time** (configurable in the code) to avoid infinite crawling
> - Headless Chrome is used to handle JavaScript-rendered content
> - Wikipedia's structure is stable, but very large crawls may take significant time

---

## 👨‍💻 Author

**Hirad Bayat**  
M.Sc. Applied Computer Science — University of Duisburg-Essen  
📧 Bayathirad7@gmail.com  
