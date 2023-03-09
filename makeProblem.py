from datetime import date

PAGETITLE = "AIME II 2005 P3"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["sequences", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/2005_AIME_II_Problems/Problem_3"

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