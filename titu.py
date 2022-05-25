import os, sys
try:
    __import__("titu").main_apv()
except Exception as e:
    exit(str(e))
