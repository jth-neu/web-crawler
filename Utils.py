import os


# Create a directory to store all the output
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.mkdir(directory)


# Create crawl jobs and stats files if not exists
def create_files(directory, base_url):
    queue = os.path.join(directory, 'queue.txt')
    crawled = os.path.join(directory, 'URLsCrawled.txt')
    stats = os.path.join(directory, 'stats.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url + '\n')
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(stats):
        write_file(stats, '')


# Write data to files
def write_file(filepath,data):
    with open(filepath, 'w') as file:
        file.write(data)


# Update file
def update_file(filepath, data):
    with open(filepath, 'a') as file:
        file.write(data + '\n')


# Update stats
def update_stats(filepath, max_size, min_size, average_size, max_depth_reached):
    with open(filepath, 'w') as file:
        file.write('Maximum size: ' + str(max_size) + ' bytes \n')
        file.write('Minimum size: ' + str(min_size) + ' bytes \n')
        file.write('Average size: ' + str(average_size) + ' bytes \n')
        file.write('Maximum depth reach: ' + str(max_depth_reached))

create_project_dir('wiki')
create_files('wiki', 'http://wiki.com')
update_file('wiki/queue.txt', 'sadasd')
update_stats('wiki/stats.txt', 12,12,12,12)