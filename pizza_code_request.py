'''
This program will pull the most recent dominos codes from boards.ie and save 
in a file for alexa skill.
'''

from urllib.request import Request, urlopen
import bs4
import re
from collections import OrderedDict

base_link = "https://www.boards.ie/vbulletin/showthread.php?"
base_thread = "p=108065387?"

#------------------------------------------------------------------------------
def get_html_on_page(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
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

def giz_codes():
    link = base_link+base_thread
    base_html = get_html_on_page(link)
    base_soup = bs4.BeautifulSoup(base_html, "html.parser")
    last_page_number = get_last_page_number(base_soup)
    
    end_thread = "t=2056744169"
    codes = []    
    for p in range(0, 3):
        curr_page_number = last_page_number-p
        curr_link = base_link+end_thread+"&page="+str(curr_page_number)
        curr_html = get_html_on_page(curr_link)
        page_codes = find_codes(curr_html)
        codes.append(page_codes)

    flat_code_list = [" ".join(code) for sublist in codes for code in sublist]
    flat_code_list = list(OrderedDict.fromkeys(flat_code_list))
    
    return flat_code_list


def get_codes_ordered_list():
    flat_code_list = giz_codes()
    return flat_code_list

def get_first_code():
    flat_code_list = giz_codes()
    return flat_code_list[0]
    
def get_code_indexed(index):
    flat_code_list = giz_codes()
    if(index > len(flat_code_list)-1):
        return "not available"
    else:
        return flat_code_list[index]




    
    