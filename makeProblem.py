from datetime import date

PAGETITLE = "AIME 1983 P10"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["combo", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_10"

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

The numbers $1447$, $1005$ and $1231$ have something in common: each is a $4$-digit number beginning with $1$ that has exactly two identical digits. How many such numbers are there?

## Solution



''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)