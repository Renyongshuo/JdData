# ! /usr/bin/python3
# _*_ coding: utf-8 _*_

from __future__ import print_function
import requests
import sys

resp = requests.get("http://www.jd.com")
print(resp.status_code)
