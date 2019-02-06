'''
This program will pull the most recent dominos codes from boards.ie and save 
in a file for alexa skill.
'''

import urllib.request
import bs4
import re

base_link = "https://www.boards.ie/vbulletin/showthread.php?"
base_thread = "p=108065387?"

#------------------------------------------------------------------------------
def get_html_on_page(link):
    response = urllib.request.urlopen(link)
    html = response.read().decode('utf-8','ignore')
    return html

# Not currently used -- gets the post messages on pages
def find_posts(html):
    result = re.findall(r'post_message_(\d{9})', html)
    return result

# Finds the codes on each page
def find_codes(html):
    result = re.findall('[A-Z]{5,10}[0-9]{1,4}', html)
    return result

# Findes the last page number
def get_last_page_number(mysoup):   
    for match in mysoup.find_all('a', attrs={'title':re.compile(r'^Last Page')}):
        last_page_link = match.get('href')
        last_page = last_page_link[-3:]
    return int(last_page)

#------------------------------------------------------------------------------

link = base_link+base_thread
base_html = get_html_on_page(link)
base_soup = bs4.BeautifulSoup(base_html, "html.parser")
last_page_number = get_last_page_number(base_soup)

end_thread = "t=2056744169"
codes = []    
for p in range(0, 10):
    curr_page_number = last_page_number-p
    curr_link = base_link+end_thread+"&page="+str(curr_page_number)
    curr_html = get_html_on_page(curr_link)
    page_codes = find_codes(curr_html)
    codes.append(page_codes)
 
code_list = []        
flat_code_list = [code for sublist in codes for code in sublist]
print(flat_code_list)







    
    