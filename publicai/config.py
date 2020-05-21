"""
Copyright 2019, All rights reserved.
Author : SangJae Kang
Mail : rocketgrowthsj@gmail.com
"""
import os

HOME_DIR = os.path.expanduser("~")
DOWNLOAD_URL = "https://studyai.s3.ap-northeast-2.amazonaws.com"
SAVE_DIR = os.path.join(HOME_DIR, ".studyai", "datasets")

EVALUATION_URL = "http://quiz.publicai-edu.com"

if not os.path.exists(SAVE_DIR):
    # Create Cache Directory
    os.makedirs(SAVE_DIR, exist_ok=True)
