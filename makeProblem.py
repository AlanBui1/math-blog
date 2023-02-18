from datetime import date

PAGETITLE = "Fermat 2009 Q23"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["number theory"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2009/2009FermatContest.pdf"

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

Suppose that $a$, $b$, $c$, and $d$ are positive integers that satisfy the equations

$$ab + cd = 38$$

$$ac + bd = 34$$

$$ad + bc = 43$$

What is the value of $a$ + $b$ + $c$ + $d$?

## Solution



''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)