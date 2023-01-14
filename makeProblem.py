from datetime import date

PAGETITLE = "Fermat 2005 Q20"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["geometry", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2005/2005FermatContest.pdf"

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

In triangle $ABC$, if $AB = AC = x + 1$ and $BC = 2x - 2$, where $x > 1$, then the area of the triangle is always equal to

[Problem Link]('''+PROBLEMLINK+''')

## Solution

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)