from datetime import date

PAGETITLE = "AIME 1985 P7"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["number theory", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/1985_AIME_Problems/Problem_7"

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

Assume that $a$, $b$, $c$, and $d$ are positive integers such that $a^5 = b^4$, $c^3 = d^2$, and $c - a = 19$. Determine $d - b$.

[Problem Link]('''+PROBLEMLINK+''')

<details>
<summary> Solution </summary>

</details>

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)