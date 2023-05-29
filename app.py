from scrape import scrape
from dataPrep import prep
import sql

def main():
    print('Requesting data from API...')
    data = scrape()
    print('Done scraping!', 'Let\'s prep the data', sep='\n')
    data = prep(data)
    print('Done prepping!', 'Let\'s send the data to the database', sep='\n')
    for report in data:
        sql.createDailyReport(report)
    print(data)

if __name__ == '__main__':
    main()