from datetime import date

PAGETITLE = "AIME 1988 P5"
AUTHOR = "Alan_Bui"
DATE = str(date.today())
CATEGORIES = ["AIME"]
TAGS = ["probability", "TO DO"]

FILENAME = "_posts/"+DATE+"-"+PAGETITLE.replace(" ", "-")+".md"
PROBLEMLINK = "https://artofproblemsolving.com/wiki/index.php/1988_AIME_Problems/Problem_5"

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