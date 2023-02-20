from datetime import date

PAGETITLE = "AIME II 2006 P7"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["combo", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/2006_AIME_II_Problems/Problem_7"

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

Find the number of ordered pairs of positive integers $(a,b)$ such that $a+b=1000$ and neither $a$ nor $b$ has a zero digit.

## Solution



''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)