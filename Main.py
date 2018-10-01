import argparse
from Crawler import Crawler

parser = argparse.ArgumentParser()
parser.add_argument("SeedUrl", help="The starting page of the crawling")
parser.add_argument("Numpages", help='The number of pages for the crawling', type=int)
args = parser.parse_args()
print('The Starting page is :' + args.SeedUrl)
print('The number of pages is :' + str(args.Numpages))


def start(url, numpages):
    if url != '' and numpages > 0:
        crawler = Crawler('Output', url, 5)
        crawler.crawl(numpages)
    else:
        raise ValueError('The input is invalid')

start(args.SeedUrl, args.Numpages)