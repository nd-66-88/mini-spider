# mini-spider
Web crawler

HTMLParser.py: 
It parses html page and extracts href from tags.

log.py: 
It records console output and errors

mini_spider.py: 
main program. It reads from console input and passes parameters to threads

spiderx.py: 
inherits from threading.thread. It is mainly used for web crawls and saving webpages which match the given pattern

read_configs.py: 
read configuration from spider.conf

save_file.py: 
save files to local directory

request_URL.py: 
send requests

please install python3.8 before executing this program

how to execute this program: python mini_spider.py -c conf/spider.conf 
