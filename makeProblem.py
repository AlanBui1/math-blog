from datetime import date

PAGETITLE = "Fermat 2007 Q23"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["geometry"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2007/2007FermatContest.pdf"

cats = str(CATEGORIES).replace("'", '')
tags = str(TAGS).replace("'", '')

with open(FILENAME, "w") as outFile:
    outFile.write('''---
title: '''+PAGETITLE+'''    
author: '''+AUTHOR+'''    
date: '''+DATE+'''
categories: '''+cats+'''
tags: '''+tags+'''
math: true    
mermaid: true  
---

---
## Problem Statement

[Problem Link]('''+PROBLEMLINK+''')

![Problem Diagram](/assets/diagrams/fermat2007q23.png)

## Solution

![Problem Diagram](/assets/diagrams/fermat2007q23-1.png)


''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)