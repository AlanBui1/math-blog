from datetime import date

PAGETITLE = "Fermat 2017 Q25"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["number theory", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2017/2017FermatContest.pdf"

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

Let $r$ = $\sqrt{\dfrac{\sqrt{53}{2}} + \dfrac{3}{2}}. There is a unique triple of positive integers $(a, b, c)$ such that 

$$r^100 = 2r^98 + 14r^96 + 11r^94 - r^50 + ar^46 + br^44 + cr^40$$

What is the value of $a^2 + b^2 + c^2$?

[Problem Link]('''+PROBLEMLINK+''')


## Solution

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)