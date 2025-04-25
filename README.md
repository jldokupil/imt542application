# Wikipedia Reference Extractor

This is a simple Python CLI application that accepts a Wikipedia article URL and displays all the sources listed in the References section in a clean, readable format.

---

## Features

- Accepts any valid Wikipedia article URL
- Extracts and displays all citation references
- Prints results in a nicely formatted list
- Handles invalid URLs and connection errors gracefully

---

## Getting Started

### 1. Clone or Download the Script

You can download the file directly or clone this repo if you're storing it in Git.

```bash
git clone <your-repo-url>
cd wikipedia-reference-extractor
```

Or just move the `wiki_sources.py` script to your working directory.

---

### 2. Install Dependencies

Make sure you have Python 3 and the required libraries:

```bash
pip install requests beautifulsoup4
```

---

### 3. Run the Application

```bash
python3 wiki_sources.py "https://en.wikipedia.org/wiki/Artificial_intelligence"
```

Replace the URL with any Wikipedia article you want to scrape.

---

## Example Output

```
References:
------------------------------------------------------------
1. Artificial Intelligence: A Modern Approach. Russell & Norvig. Pearson Education.
2. "Turing Test". Stanford Encyclopedia of Philosophy.
...
```

---

## Notes

- This script only works with English Wikipedia URLs (e.g., `en.wikipedia.org/wiki/...`).
- Make sure the article has a References section, or the script may return "No references found."

---

## License

This project is free to use and modify. No attribution required, but always appreciated!

---

## Contributing

Feel free to open issues or submit pull requests to improve parsing, error handling, or formatting.
