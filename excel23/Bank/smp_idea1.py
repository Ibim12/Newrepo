from selenium import webdriver

PATH= "C:\chromedriver.exe"

driver=webdriver.Chrome(PATH)
social_media_posts={driver.get("https://techwithtim.net"),driver.get("https://www.youtube.com/watch?v=5ud9Y2uB4PY"),driver.get("https://www.youtube.com/watch?v=LojAlo8AGl4"),driver.get("https://www.w3schools.com/python/"),driver.get("https://www.instagram.com/")}
# f'post1:{"https://techwithtim.net"}, post2:{"https://www.youtube.com/watch?v=5ud9Y2uB4PY"},post3:{"https://www.youtube.com/watch?v=LojAlo8AGl4"}, post4{"https://www.w3schools.com/python/"}post5{"https://www.instagram.com/"}'
    # for i in range(1,3):
        # social_media_posts.add{}














        