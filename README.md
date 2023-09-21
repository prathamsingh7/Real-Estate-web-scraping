# Real-Estate-web-scraping

Developing a web scraper to collect real estate data, store it in a Postgres database, and a flask endpoint to search the dataset by year or document number.

### Step 1 - Web scraping
- The website to scrape is [Maharashtra State Government Department of Registration and Stamps](https://pay2igr.igrmaharashtra.gov.in/eDisplay/propertydetails/)

- After entering the **year, district, taluka, village, and registration year** as given, the data is generated.

- The task is to scrape the first **50 entries** of the obtained table data. 

- The entire scraping process is automated using **Selenium** and can be found in [this file](https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/web_scraper.py)

- The initial scraped data looks like -
<p align="center">
  <img width="900" height="500" src="https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/Images/data_marathi.png">
</p>

### Step 2 - Cleaning and translating data
- As seen above, the scraped data is in **Marathi**and hence must be translated to **English** 

- First, the data is cleaned and the data format is changed in this [code file](https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/cleaning_translating.ipynb)

- Thereafter, all the columns containing text in Marathi are translated to English using the **googletrans** library.

- The translated data looks like -
<p align="center">
  <img width="900" height="500" src="https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/Images/data_english.png">
</p>

### Step 3 - Storing data in the PostgreSQL database table and building a Flask endpoint
- First, a connection to the **PostgreSQL** database is made using the **psycopg2** library.

- A table is created and the CSV file is iterated over the rows and all the rows are inserted in the PostgreSQL table.

- The code for the storing of data in the PostgreSQL table can be found in [this file](https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/postgres.py)

- The PostgreSQL table looks like -
<p align="center">
  <img width="900" height="500" src="https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/Images/database.png">
</p>

- Finally, a flask endpoint was built for extracting the data based on registration year and document number. The code for the same can be found [here](https://github.com/prathamsingh7/Real-Estate-web-scraping/blob/main/app.py)
