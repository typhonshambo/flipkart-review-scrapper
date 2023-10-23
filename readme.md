# Flipkart Review Scrapper
<img align="right" alt="GIF" src="https://seeklogo.com/images/F/flipkart-logo-3F33927DAA-seeklogo.com.png" width="150"/>
Welcome to the 🌟 **Flipkart Review Scrapper** 🌟 project! This simple Python script helps you 🕵️‍♂️ scrape product reviews from Flipkart for a given keyword. With this tool, you can quickly gather product review data for analysis or other purposes.





## How to Use

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/flipkart-review-scrapper.git
    cd flipkart-review-scrapper
    ```

2. **Install Dependencies**

    Make sure you have the required libraries installed. You can install them using 📦 pip:

    ```bash
    pip install requests beautifulsoup4
    ```

3. **Run the Scrapper**

    Use the 🚀 `main.py` 🚀 script to run the scrapper. You will be prompted to enter the keyword for the product you want to search for.

    ```bash
    python main.py
    ```

    The scrapper will load and collect review data from Flipkart for the specified keyword.

4. **Check the Data**

    Once the scrapper has finished its work, you can find the collected data in a file called 📁 `data.json`. This JSON file contains the product titles and their corresponding reviews.

5. **Enjoy the Data!**

    You can now use the scraped data for your analysis, research, or any other purpose you have in mind.

## Code Structure

Here's a brief overview of the project structure:

- 📂 **`main.py`**: The main script that takes user input for the keyword and calls the scraper function.

- 📂 **`scrapper.py`**: Contains the code for web scraping Flipkart product reviews. It fetches product titles, review links, and reviews.



This project is a useful tool for collecting data from Flipkart and can be extended for various applications. If you have any questions or need further assistance, feel free to reach out. Happy scrapping! 🚀📦🌟
