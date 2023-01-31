# College Salary Report Scraper
This project scrapes data from the Payscale College Salary Report and saves it to a CSV.

# Requirements
> pandas
> requests
> beautifulsoup4

# Explanation of the code
The code uses 'requests' library to make HTTP requests to the URL of the College Salary Report. The 'beautifulsoup4' library is then used to parse the HTML response and extract the data of interest. The extracted data then stored in a list of dictionaries which is then converted to a pandas DataFrame and saved to a CSV file.


