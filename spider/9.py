html='''
<html>
 <body>
  <p class="story">
   Once upon a time there were three little sisters;and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    <!--Elsie-->
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
'''

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print('Next Sibling',soup.a.next_sibling)
print('Prev Sibling',soup.a.previous_sibling)
print('Next Sibling',list(enumerate(soup.a.next_siblins)))

