# Technical notes:
#### URL
* URL: Atlanta GA URL: https://www.zillow.com/homes/Atlanta,-GA_rb/
#### Finding the headers:
* Chrome developer tools, network tab, searchQueryState line for zillow.com
* grab the request headers (accept - user agent)
* format them as a dictonary
#### Finding the paramaters
* in the dev tools there is a searchQueryState paramaters section - grab that
* format as a dictionary 

#### BS4
* response.text
* content.prettify()

.contents lets you see direct child elements


https://www.zillow.com/atlanta-ga/

https://www.zillow.com/atlanta-ga/

https://www.zillow.com/homes/for_sale/Atlanta,-GA_rb/

"currentPage": %s


python3 -m venv env
source env/bin/activate
deactivate
echo ‘env' > .gitignore


