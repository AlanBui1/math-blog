from datetime import date

PAGETITLE = "Fermat 1998 Q22"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["number theory"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/1998/1998FermatContest.pdf"

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

There are four unequal, positive integers $a$, $b$, $c$, and $N$ such that $N = 5a + 3b + 5c$. It is also true that $N = 4a + 5b + 4c$ and $N is between 131 and 150. What is the value of $a+b+c$ ?

## Solution



''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)