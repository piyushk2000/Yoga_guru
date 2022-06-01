import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import threading
from typing import Union
from PIL import Image
import pickle
import pandas as pd
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import av
from streamlit_webrtc import *
from PIL import ImageFile
import sqlite3
from datetime import date
from distutils.command.upload import upload
conn = sqlite3.connect('data.db',check_same_thread=False)

c = conn.cursor()
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(name TEXT,acuu TEXT,passFail TEXT,asan TEXT,date DATE,inputby)')

def add_data(name,acuu,passFail,asan,inputby):

	c.execute('INSERT INTO taskstable(name,acuu,passFail,asan,date,inputby) VALUES (?,?,?,?,?,?)',(name,acuu,passFail,asan,date.today(),inputby))
	conn.commit()



ImageFile.LOAD_TRUNCATED_IMAGES = True