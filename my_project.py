from my_module.scraper import crawl

if __name__ == '__main__':
    crawl(time_limit=60, source='lrytas', return_format='csv')