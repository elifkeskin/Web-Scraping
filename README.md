# Book Category Web Scraping & Competitor Analysis

## 📝 Business Problem

An online book retailer has observed low sales in the **"Non-Fiction"** and **"Travel"** categories. To address this, the company aims to analyze competitor offerings and pricing by scraping book data from a rival website: [books.toscrape.com](https://books.toscrape.com/).

## 🎯 Project Goal

The main objective of this project is to:

- Identify and extract information for each book listed under the "Travel" and "Non-Fiction" categories on the target website.
- Visit each book's detail page to collect additional content and data.
- Analyze the collected data to gain insights into competitors’ product offerings and pricing strategies.

## 📚 Data to be Collected

For each book in the specified categories, the following information will be scraped:

- Book Title
- Price
- Stock Availability
- Book Rating
- Product Description (from the detail page)
- UPC, Product Type, Tax, and other metadata (from the detail page)
- Category

## 🛠️ Technologies & Libraries

- **Python:** Main programming language for scripting and data analysis.
- **requests:** For sending HTTP requests to the website.
- **BeautifulSoup:** For parsing and extracting data from HTML pages.
- **pandas:** For organizing and analyzing the scraped data.
- **csv:** For exporting the results to CSV files.

## 🚦 Project Steps

1. **Category Page Scraping:**  
   - Navigate to the "Travel" and "Non-Fiction" categories on the website.
   - Extract the list of books and their links to detail pages.

2. **Detail Page Scraping:**  
   - For each book, visit its detail page.
   - Extract additional information such as product description, UPC, and other metadata.

3. **Data Storage:**  
   - Store the collected data in a structured format (e.g., CSV or DataFrame).

4. **Data Analysis:**  
   - Analyze competitor pricing, stock levels, and product descriptions.
   - Generate summary statistics and visualizations as needed.

## 🚀 Getting Started

1. **Clone the Repository**
    ```bash
    git clone https://github.com/elifkeskin/Web-Scraping.git
    cd Web-Scraping
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Scraper**
    ```bash
    python scraper.py
    ```

4. **Analyze the Data**
    - Open the generated CSV file or Jupyter notebook for further analysis.

## 📄 Example Output

| Title                | Price | Availability | Rating | Category    | Description         |
|----------------------|-------|--------------|--------|-------------|---------------------|
| Book Title Example   | £23.88| In stock     | 4      | Travel      | ...                 |

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

**For questions or suggestions, feel free to open an issue or contact the maintainer.**

