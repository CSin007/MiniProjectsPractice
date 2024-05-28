from bs4 import BeautifulSoup
import requests
import time
""" with open('home.html','r') as html_file:
    content = html_file.read(); 
    print(content); 
    -> found only 1 h5 tag, finds first one
    to change that, then do findall

    with open('home.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)

        -> this is code for scraping a html
        with open('home.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div',class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name}  costs {course_price}')

        below is some code to scrape recent jobs from asite
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span',class_='srp-skills').text.replace(' ','')
  
    
   
    print(published_date)
    print(f''''
          Company Name:{company_name}
          Required skills: {skills}
          ''')
    """
print("Put some skill u r not familiar with")
unfamiliar_skill = input(">")
print(f'Filtering out {unfamiliar_skill}')
def findJobs(): 
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs): 
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                   f.write(f" Company Name: {company_name.strip()} \n")
                   f.write(f"Required skills: {skills.strip()} \n")
                   f.write(f'More Info: {more_info} \n')
                print(f'File saved: {index} \n')
if __name__ =='__main__':
    while True:
        findJobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait*60)        
    
  
   

