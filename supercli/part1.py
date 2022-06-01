import pandas as pd
import urllib3
from bs4 import BeautifulSoup
import requests
import json
import checkDyte


def CompVer(v1, v2):
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)

    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]
    if n > m:
        for i in range(m, n):
            arr2.append(0)
    elif m > n:
        for i in range(n, m):
            arr1.append(0)
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return 1
        elif arr2[i] > arr1[i]:
            return -1
    return 0


def wel(filepath, dependency):

    df = pd.read_csv(filepath)

    df['version'] = ""
    df['version_satisfied'] = ""

    check = []
    versions = []
    for i in range(len(df)):
        temp = df['repo'][i]
        fileName = df['name'][i]
        newLink = "https://raw.githubusercontent.com/"
        link = temp.split("/")
        d = link[3]
        newLink = newLink + d + "/"

        e = link[4]
        newLink = newLink + e + "/"
        newLink = newLink + "main/package.json"
        exist_vers = checkDyte.content(newLink)
        df.at[i, 'version'] = exist_vers

        ans = CompVer(exist_vers, dependency)
        if ans < 0:
            df.at[i, 'version_satisfied'] = 'false'
        else:
            df.at[i, 'version_satisfied'] = 'true'
    df.to_csv('part1.csv')

    print(df)
