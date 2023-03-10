from datetime import date

PAGETITLE = "CSMC 2011 B2"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["CSMC"]
TAGS = ["number theory", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://cemc.uwaterloo.ca/contests/past_contests/2011/2011CSMC.pdf"

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

<details>
<summary> Solution </summary>

</details>

''')

#![Problem Diagram](/assets/diagrams/fermat2006q23.png)