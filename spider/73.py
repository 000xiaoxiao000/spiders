from selenium import webdriver
from selenium.webdriver import ActionChains
#拖曳动作
browser=webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_css_selector('#draggable')
targer=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,targer)
actions.perform()