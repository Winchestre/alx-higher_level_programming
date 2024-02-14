#!/usr/bin/python3
"""
Python script that fetches a URL with request packages
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    t = req.text
    print(f"Body response:\n\t- type: {type(t)}\n\t- content: {t}")
