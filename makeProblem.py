from datetime import date

PAGETITLE = "Fermat 2000 Q17"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["Fermat"]
TAGS = ["geometry", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2000/2000FermatContest.pdf"

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

Three circles have centres A, B and C with radii 2, 4 and 6 respectively. The circles are tangent to each other as shown. $\\triangle ABC$ has

(A) $\\angle A$ obtuse (B) $\\angle B = 90^{\\circ}$ (C) $angle A = 90^{\circ}$ (D) all angles acute (E) $\\angle A = \\angleB$

[Problem Link]('''+PROBLEMLINK+''')

![Problem Diagram](/assets/diagrams/fermat2000q17.png)

## Solution

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)