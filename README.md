## Alexa-DominosCodes

https://www.amazon.co.uk/Darren-Coughlan-Pizza-Dough/dp/B07NWGMC2R/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1552876118&sr=1-1&keywords=pizza+dough

### What it does (Proposed design)
The program takes user speech input through the amazon alexa device requesting a dominos voucher code so they can get 30% off their next
Pizza. The program then replies with the most recent pizza code which has been pulled from the boards.ie dominos pizza code thread.

### Motivation
When ordering pizza it can sometimes bee difficult to go on to boards.ie and crawl through for a new code. This Amazon alexa app should 
make ordering a lot easier.

### Tools Used
The program is written in Python and hosted on AWS lambda. I used some of the following modules to retrieve the codes:
* BeautifulSoup - Used to parse html content in this project
* urllib.request to open urls


