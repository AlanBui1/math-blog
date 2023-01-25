from datetime import date

PAGETITLE = "Fermat 2008 Q23"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["geometry"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2008/2008FermatContest.pdf"

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

Square $PQRS$ has side length 4 m. Point $U$ is on $PR$ with $PR = 4UR$. A circle centered at $U$ touches two sides of the square. $PW$ is a tangent to the circle, with $W$ on $QR$. The length of $PW$, to the nearest thousandth of a metre, is

[Problem Link]('''+PROBLEMLINK+''')

![Problem Diagram](/assets/diagrams/fermat2008q23.png)

## Solution

![Problem Diagram](/assets/diagrams/fermat2008q23-1.png)


''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)