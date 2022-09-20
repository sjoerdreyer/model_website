import json, requests
import streamlit as st

def load_lottiefile(filepath:str):
    with open(filepath, 'r') as f:
        return json.load(f)
