# DSA Scraping Project

This project is a PyQt5 desktop application built for Data Structures and Algorithms course. It combines three practical tasks around eBook data:

- Scraping Springer eBooks data into a table
- Sorting CSV data with classic DSA algorithms
- Searching and Filtering CSV data with simple boolean logic

The app opens with a main menu and lets you move into the scraping, sorting, and searching windows.

## Features

### Scraping

- Scrapes eBook data from `single-ebooks.springernature.com`
- Collects fields such as ISBN, title, subtitle, authors, publish year, link, and price
- Shows scraping progress in a progress bar
- Supports pause, resume, and stop controls
- Displays scraped results in a table and lets you save them as CSV

### Sorting

- Loads a CSV file and displays it in a table
- Sorts a selected column using one of these algorithms:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Counting Sort
  - Radix Sort
  - Bucket Sort
  - Shell Sort
  - Gnome Sort
- Supports multi-level sorting with two selected columns and ascending/descending order per column
- Displays the execution time for the selected sorting run
- Lets you save the sorted data back to CSV

### Searching

- Loads a CSV file and displays it in a table
- Searches across one or two columns
- Supports text matching for string columns and exact matching for numeric columns
- Lets you combine two conditions with `None`, `AND`, `OR`, or `NOT`

## Project Structure

- `main.py` - thin launcher that starts the app
- `src/` - application package containing the windows and sorting algorithms
- `src/main_window.py` - main launcher window UI and navigation
- `src/scrap_window.py` - scraping interface, Selenium thread, and ChromeDriver settings
- `src/sort_window.py` - CSV sorting interface and sorting thread
- `src/search_window.py` - CSV search and filtering interface
- `src/algorithms.py` - sorting algorithm implementations
- `src/config.py` - ChromeDriver path helper
- `data/25k-books.csv` - already scraped dataset of 25,000 ebooks
- `data/500-books.csv` - already scraped dataset of 500 ebooks
- `requirements.txt` - Python dependencies for the project
- `.gitignore` - ignores local cache files and virtual environments
- `UI Files/` - original Qt Designer `.ui` files used to generate the windows

## Requirements

- Python 3
- PyQt5
- pandas
- selenium
- beautifulsoup4
- Google Chrome
- ChromeDriver

## Setup

Install the Python dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you do not already have ChromeDriver installed, download the version that matches your Chrome browser and either:

- use the app menu in the Scraping window: `Options -> Set ChromeDriver Path`
- or set the `CHROMEDRIVER_PATH` environment variable

The selected path is saved to `chromedriver_path.txt` in the project root and reused automatically. That file is local to your machine and is ignored by Git.

If you still want to set a fallback path in code, update the default value in `src/config.py`:

```python
DEFAULT_CHROMEDRIVER_PATH = r'C:\\Program Files\\Chromedriver\\chromedriver.exe'
```

## Run

Start the application from the project root:

```bash
python main.py
```

## How To Use

1. Open the app from `main.py`.
2. Choose one of the three modes: Scrape EBooks, Sort Data, or Search Data.
3. In the sorting and searching windows, load a CSV file before running actions.
4. In the scraping window, choose how many ebooks to collect, start scraping, and save the output when finished.

## Notes

- The scraping feature depends on live access to the Springer ebook site.
- The sorting algorithms operate on the selected column from the loaded CSV.
- Some algorithms are best suited to numeric or simple string data, especially counting, radix, and bucket sort.
- The generated Python files were created from Qt Designer `.ui` files, so manual UI edits should be made carefully.
