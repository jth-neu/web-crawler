import os


# Create a directory to store all the output
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.mkdir(directory)
    output_folder = os.path.join(directory, 'crawled_pages')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)


# Create crawl jobs and stats files if not exists
def create_files(directory):
    crawled = os.path.join(directory, 'URLsCrawled.txt')
    stats = os.path.join(directory, 'stats.txt')
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(stats):
        write_file(stats, '')


# Create a text for web page
def create_page_file(directory, page_count, data):
    file = os.path.join(directory, 'crawled_pages/' + str(page_count) + '.txt')
    if not os.path.isfile(file):
        write_file(file, data)


# Write data to files
def write_file(filepath,data):
    with open(filepath, 'w') as file:
        file.write(data)


# Update file
def update_file(filepath, data):
    with open(filepath, 'a') as file:
        file.write(data + '\n')


# save stats
def save_stats(filepath, max_size, min_size, average_size, max_depth_reached):
    with open(filepath, 'w') as file:
        file.write('Maximum size: ' + str(max_size) + ' bytes \n')
        file.write('Minimum size: ' + str(min_size) + ' bytes \n')
        file.write('Average size: ' + str(average_size) + ' bytes \n')
        file.write('Maximum depth reach: ' + str(max_depth_reached))


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
