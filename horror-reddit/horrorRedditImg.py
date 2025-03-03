from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from PIL import Image, ImageOps
from gtts import gTTS
from moviepy import *

import random

import requests
import pandas as pd

import os
import time

from pprint import pprint

def create_text_list(response):

        text_list = []
        for post in response.json()['data']['children']:
            title = post['data']['title']
            
            text = post['data']['selftext']        

            tup = (title, text)
            text_list.append(tup)
        return text_list


def make_url_list(params=[]):
    
    REDDIT_URL = 'https://www.reddit.com/r/TwoSentenceHorror/top/.json'
    HEADERS = {'User-Agent': 'MyRedditApp/0.1'}

    resp = requests.get(REDDIT_URL, headers=HEADERS)

    full_url_list = []

    if resp.status_code != 200:
            print(f'Response status code is {resp.status_code} instead of 200')
            print(resp.json())
            
            return []
        
    else:

        json_list = resp.json()['data']['children']
        
        # text_list = create_text_list(resp) # dw lowkey fake code
        
        for post in json_list:
            url = post['data']['url']
            not_pinned_community_bool = 'announcement' not in str(url) and 'permabans' not in str(url)
            not_over18 = not post['data']['over_18']
            not_spoiler = not post['data']['spoiler']
            
            if not_pinned_community_bool and (not_over18 and not_spoiler):
                full_url_list.append(url)                                
                            
    return full_url_list

def get_image_list(url_list, num):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    past_urls = pd.read_csv("past_urls.csv")
    
    is_unique_url = []
    for item in url_list[0:num]:
        URL = item

        boolean_item = False
        if URL not in past_urls['URLS'].values:
            driver.get(URL)
            title_text = driver.find_element(By.XPATH, '/html/body/shreddit-app/div[2]/div[1]/div/main/shreddit-post')
            
            name = f'images/post-{url_list.index(item)+1}.png'
            title_text.screenshot(name)
            
            image = Image.open(name)
            inverted_image = ImageOps.invert(image)

            final_name = f'final/invert-{url_list.index(item)+1}.png'
            inverted_image.save(final_name)
            
            row = pd.DataFrame({'URLS': [URL],})
            past_urls = pd.concat([past_urls, row], ignore_index=True) 
            boolean_item = boolean_item or True
            
        is_unique_url.append(boolean_item)
        
    past_urls.to_csv("past_urls.csv", index=False)
    driver.close()
    
    return is_unique_url

    
def make_individual_reel(number, check_bool):

    for num in range(1, number+1):
        check_bool_item = check_bool[num-1]
        if check_bool_item:
            
            bgVid_n = random.randint(0,1) + 1
            
            clip = VideoFileClip(f"bgmFiles/backgroundVid{bgVid_n}.mp4").subclipped(20, 35) # Load file example.mp4 and extract only the subclip from 00:00:10 to 00:00:20
            clip = clip.with_volume_scaled(0.01) # Reduce the audio volume to 1% of his original volume


            post = ImageClip(f'final/invert-{num}.png').with_position(("center","center")).with_start(0).with_duration(15)
            
            (w, h) = clip.size
            crop_width = h * 9/16 # x1,y1 is the top left corner, and x2, y2 is the lower right corner of the cropped area.
            x1, x2 = (w - crop_width)//2, (w+crop_width)//2
            y1, y2 = 0, h
            cropped_clip = clip.cropped(x1=x1, y1=y1, x2=x2, y2=y2)

            audio_num = random.randint(1, 3)

            audio = []
            match audio_num:
                case 1:
                    tim = random.randint(0, 3000)
                    audio = AudioFileClip('bgmFiles/bgAudio1.mp3').subclipped(tim, tim + 15)
                    cropped_clip = cropped_clip.with_audio(audio)
                    cropped_clip = cropped_clip.with_volume_scaled(1.10)
            
                case 2:
                    audio = AudioFileClip('bgmFiles/daisybell_bgm.mp3').subclipped(4, 19)
                    cropped_clip = cropped_clip.with_audio(audio)
                    cropped_clip = cropped_clip.with_volume_scaled(0.65)
                
                case 3:
                    audio = AudioFileClip('bgmFiles/runrabbit_bgm.mp3').subclipped(40, 55)
                    cropped_clip = cropped_clip.with_audio(audio)
                    cropped_clip = cropped_clip.with_volume_scaled(0.65)
                
     
            video = CompositeVideoClip([cropped_clip, post]) # Overlay the text clip on the first video clip

            video.write_videofile(f'reels/result-{num}.mp4')  # Write the result to a file (many options available!)
            print(f'************** made video {num} **************')
        else:
            print(f'************** skipped video {num}, was not unique *****************')


def check_exists(num):

    file_path = f'reels/result-{num}.mp4'
    if os.path.exists(file_path) and file_path.endswith('.mp4'):
        return True

def post_individual_reel(num):
    num = 1
    YOUTUBE_URL = 'https://studio.youtube.com/channel/'
    TIKTOK_URL = 'https://www.tiktok.com/login/'
    TIKTOK_URL_E = 'https://www.tiktok.com/login/phone-or-email/email'
    
    title = 'r/twosentenceHorror #horror #scary #creepy'
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get(TIKTOK_URL_E)
    driver.maximize_window()
    
    time.sleep(2)
    
    # google_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[2]')
    # google_button.click()
    # driver.switch_to.window(driver.window_handles[-1])

    login_input = driver.find_element(By.TAG_NAME, 'input')
    login_input.send_keys('priya.yadav42805@gmail.com')
    time.sleep(2.54)
    
    password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[2]/div/input')
    password_input.send_keys('temporary1243$')
    time.sleep(2.54)
    
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    time.sleep(2.54)
    
        
    time.sleep(15)
    
    driver.close()
    
   
