from urllib.request import urlopen
from LinkFinder import LinkFinder
from Utils import *
import time


class Crawler:

    def __init__(self, project_name, base_url, max_depth):
        self.project_name = project_name
        self.base_url = base_url
        self.max_depth = max_depth
        self.current_depth = 0
        self.depth_links = []
        self.crawled = set()
        self.crawled_file = self.project_name + '/URLsCrawled.txt'
        self.stats_file = self.project_name + '/stats.txt'
        self.max_bytes = 0
        self.min_bytes = float('Inf')
        self.total_bytes = 0
        self.crawl_counter = 0
        self.boot()

    def boot(self):
        create_project_dir(self.project_name)
        create_files(self.project_name)
        initial_set = set()
        initial_set.add(self.base_url)
        self.depth_links.append(initial_set)
        self.crawled = file_to_set(self.crawled_file)

    def crawl(self, page_numbers):
        while self.current_depth < self.max_depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                print('Now crawling : ' + link + '| Current Depth :' + str(self.current_depth + 1))
                current_links.extend(self.filter_links(self.get_page_content(link)))
                self.crawled.add(link)
                time.sleep(1)
                if len(self.crawled) >= page_numbers:
                    break
            self.current_depth += 1
            self.depth_links.append(current_links)
            self.update_files()

    def get_page_content(self, page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(self.base_url)
            finder.feed(html_string)
            self.update_stats(html_bytes)
            self.save_content(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def filter_links(self, links):
        filtered_links = set()
        for link in links:
            if link in self.crawled:
                continue
            if link in self.depth_links[self.current_depth]:
                continue
            if '://en.wikipedia.org/wiki/' not in link:
                continue
            result = link.split('.org/wiki/')
            if 'Main_Page' in result[-1]:
                continue
            if ':' in result[-1]:
                continue
            filtered_links.add(link)
        return filtered_links

    def update_files(self):
        set_to_file(self.crawled, self.crawled_file)
        avg_byte_size = self.total_bytes / self.crawl_counter
        save_stats(self.stats_file, self.max_bytes, self.min_bytes, avg_byte_size, self.current_depth)

    def update_stats(self, html_bytes):
        byte_size = len(html_bytes)
        if byte_size > self.max_bytes:
            self.max_bytes = byte_size
        if byte_size < self.min_bytes:
            self.min_bytes = byte_size
        self.total_bytes += byte_size
        self.crawl_counter += 1

    def save_content(self, html_string):
        create_page_file(self.project_name, self.crawl_counter, html_string)


c1 = Crawler('wiki', 'https://en.wikipedia.org/wiki/Stephen_Robertson_%28computer_scientist%29', 2)
c1.crawl(10)




