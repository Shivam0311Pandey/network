from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.

class WebpageTests(LiveServerTestCase):

    def test(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        assert "Social Network" in driver.title
        user = "el"
        user1 = "el"
        register = driver.find_element_by_link_text("Register")
        register.send_keys(Keys.RETURN)
        time.sleep(1)
        heading = driver.find_element_by_tag_name("h2")
        assert heading.text == "Register"
        username = driver.find_element_by_name("username")
        email = driver.find_element_by_name("email")
        password = driver.find_element_by_name("password")
        confirmation = driver.find_element_by_name("confirmation")
        submit = driver.find_element_by_class_name("btn")
        username.send_keys(user)
        email.send_keys(f"{user}@example.com")
        password.send_keys("password")
        confirmation.send_keys("password")
        submit.click()
        time.sleep(1)
        userName = driver.find_element_by_id("name")
        assert userName.text == user
        assert "Following" in driver.page_source
        for i in range(15):
            postContent = driver.find_element_by_id("post-content")
            postSubmit = driver.find_element_by_class_name("btn")
            postContent.send_keys("Post content...")
            postSubmit.click()
        allPosts = driver.find_elements_by_class_name("post")
        assert len(allPosts) == 10
        userProfile = driver.find_element_by_link_text(user)
        userProfile.click()
        time.sleep(1)
        followers = driver.find_element_by_class_name("followers")
        follow = driver.find_element_by_xpath("//span[@class='text-muted']")
        assert followers.text == '0'
        assert follow.text == '0'
        userAllPosts = driver.find_elements_by_class_name("post")
        assert len(userAllPosts) == 10
        logOut = driver.find_element_by_link_text("Log Out")
        logOut.click()
        user = "elina"
        time.sleep(1)
        register = driver.find_element_by_link_text("Register")
        register.send_keys(Keys.RETURN)
        time.sleep(1)
        heading = driver.find_element_by_tag_name("h2")
        assert heading.text == "Register"
        username = driver.find_element_by_name("username")
        email = driver.find_element_by_name("email")
        password = driver.find_element_by_name("password")
        confirmation = driver.find_element_by_name("confirmation")
        submit = driver.find_element_by_class_name("btn")
        username.send_keys(user)
        email.send_keys(f"{user}@example.com")
        password.send_keys("password")
        confirmation.send_keys("password")
        submit.click()
        userName = driver.find_element_by_id("name")
        assert userName.text == user
        assert "Following" in driver.page_source
        postContent = driver.find_element_by_id("post-content")
        postSubmit = driver.find_element_by_class_name("btn")
        postContent.send_keys("Post content...")
        postSubmit.click()
        time.sleep(1)
        like = driver.find_element_by_class_name("heart")
        like.click()
        likeCount = driver.find_element_by_class_name("count")
        assert likeCount.text == "1"
        time.sleep(1)
        like.click()
        time.sleep(1)
        assert likeCount.text == "0"
        otherProfile = driver.find_element_by_link_text(user1)
        otherProfile.click()
        followBtn = driver.find_element_by_class_name("follow")
        followBtn.click()
        time.sleep(1)
        followers = driver.find_element_by_class_name("followers")
        assert followers.text == '1'
        allPosts = driver.find_elements_by_class_name("post")
        assert len(allPosts) == 10
        following = driver.find_element_by_link_text("Following")
        following.click()
        time.sleep(1)
        allPosts = driver.find_elements_by_class_name("post")
        assert len(allPosts) == 10
        userProfile = driver.find_element_by_link_text(user)
        userProfile.click()
        followers = driver.find_element_by_class_name("followers")
        follow = driver.find_element_by_xpath("//span[@class='text-muted']")
        assert followers.text == '0'
        assert follow.text == '1'
        userAllPosts = driver.find_elements_by_class_name("post")
        assert len(userAllPosts) == 1
        logOut = driver.find_element_by_link_text("Log Out")
        logOut.click()
        time.sleep(1)
        logIn = driver.find_element_by_link_text("Log In")
        logIn.click()
        time.sleep(1)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_class_name("btn")
        username.send_keys(user1)
        password.send_keys("password")
        submit.click()
        userName = driver.find_element_by_id("name")
        time.sleep(1)
        assert userName.text == user1
        assert "Following" in driver.page_source


