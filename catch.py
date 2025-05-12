from playwright.sync_api import sync_playwright
import time

def scrape_text_from_webpage(url, output_file):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            while True:
                # 等待页面加载并且<div id="voteMessage">元素出现
                page.wait_for_selector('#voteMessage', timeout=10000)
                
                # 获取<div id="voteMessage">中的文字内容
                vote_message = page.query_selector('#voteMessage').inner_text().strip()
                
                if vote_message != "Loading...":
                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(vote_message + '\n')
                    print(f'Text has been successfully saved to {output_file}')
                    break
                else:
                    print('Content is still loading, waiting for 1 second...')
                    time.sleep(1)
            
            browser.close()
    except Exception as e:
        print(f'An error occurred: {e}')

# 使用示例
url = 'https://darkslategray-squirrel-310334.hostingersite.com/wen.html'  # 替换成你要爬取的网页URL
output_file = './vote.txt'  # 输出的本地txt文件名

while True:
    scrape_text_from_webpage(url, output_file)
    time.sleep(1)  # 每隔1秒执行一次
