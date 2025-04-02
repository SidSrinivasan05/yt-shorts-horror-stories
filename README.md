# yt-shorts-horror-stories

This repository automates the creation of YouTube horror shorts by generating eerie visuals, suspenseful audio, and chilling narratives.
This project was started to see if it was possible to autogenerate those AITA tiktok/shorts. Since that project proved to be a little difficult to implement,
instead this project started focusing on recreating tiktok/shorts that show Reddit's Two Sentence Horror Stories.

# Installation
```sh
        git clone https://github.com/SidSrinivasan05/yt-horror-shorts.git  
        cd yt-shorts-horror-stories/horror-reddit
```
        
Install required modules

# Usage
```sh
        python main.py
```
Manually go in and change how many shorts you want to be made using the parameter in the main function.


# Features:
Web Scraping: Goes through the sub reddit r/twosentencehorror to find the top stories.

Automated Video Editing: Combines stock footage, eerie effects, and sound design.

Background Music & SFX: Adds suspenseful soundtracks and jump scare effects.

# Process
1.) Uses Reddit's API and Selenium to find the top n stories of the week and screenshots the stories.

- Makes sures the screenshots aren't of videos already made (No Duplicate Videos)

- Makes sures the image isn't of a Above 18 post or has a spoiler (All screenshots are viewable)

- Saves all the posts urls to a csv file to ensure no duplicate videos are made
    
2.) Uses PIL to invert the colors of the screenshot to dark mode to fit the theme

3.) Then creates a 15 second video clip using MoviePy module 
- This clip is formatted to fit the tiktok/short format

- Randomly picks a stock background video to play underneath the screenshot of the story

- Randomly picks a creepy audio to play in the back ground

Saves this clip locally

# Side Note
Some background stock files were too large to add to the git repo so they were just omitted. If you plan on using this project, pay attention to the file names and 
whether those files exist in your personal project.


# Missing Features
  This project isn't perfect. There was an effort to add an AI voice in the background to read out the stories. 
  While this is possible and and easily implementable, the background voice might take away from the initial creepy mood.

  There was also an effort to auto upload these videos. Initially Selenium seemed like the route for this, but Youtube's and Tiktok's made this 
  difficult to work with.
  Youtube and Tiktok's API also were too difficult to work with and required an existing business or a reputable youtube channel.

# Modules Used
- Selenium

- Pandas

- PIL

- Requests

- MoviePy
