from datetime import date

PAGETITLE = "AIME 1990 P10"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["complex numbers", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/1990_AIME_Problems/Problem_10"

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

The sets $A = \{z : z^{18} = 1\}$ and $B = \{w : w^{48} = 1\}$ are both sets of complex roots of unity. The set $C = \{zw : z \in A ~ \mbox{and} ~ w \in B\}$ is also a set of complex roots of unity. How many distinct elements are in $C_{}^{}$?

[Problem Link]('''+PROBLEMLINK+''')

## Solution

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)