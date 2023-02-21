from datetime import date

PAGETITLE = "AIME 1996 P12"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["combo", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/1996_AIME_Problems/Problem_12"

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

For each permutation $a_1,a_2,a_3,\cdots,a_{10}$ of the integers $1,2,3,\cdots,10$, form the sum

\[|a_1-a_2|+|a_3-a_4|+|a_5-a_6|+|a_7-a_8|+|a_9-a_{10}|.\]

The average value of all such sums can be written in the form $\dfrac{p}{q}$, where $p$ and $q$ are relatively prime positive integers. Find $p+q$.

[Problem Link]('''+PROBLEMLINK+''')

## Solution



''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)