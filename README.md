# KMP-Algorithm-Implementation
Implementation of the KMP algorithm for token recognition, based on Section 3.4.5 of Aho's Compilers book.

# Assignment 2: KMP Algorithm Implementation

## Environment and Tools
* **Operating System:** Windows 11 / Linux Ubuntu
* **Programming Language:** Python 3.10
* **Tools Used:** Visual Studio Code, Terminal

## How to Run the Program
1. Ensure Python 3 is installed on your system.
2. Open a terminal.
3. Navigate to the directory containing `kmp_algorithm.py`.
4. Execute the script:
   ```bash
   python kmp_algorithm.py
5. The console will display the results ("yes" or "no") for the strings tested in Exercise 3.4.6.

## Algorithm Explanation
This script implements the Knuth-Morris-Pratt (KMP) string-searching algorithm. The KMP algorithm efficiently searches for occurrences of a "keyword" within a main "text string".The core of the KMP algorithm relies on the failure function computed in Assignment 1. When the algorithm scans the text and encounters a character that doesn't match the current position in the keyword, it doesn't just start over from the beginning of the keyword. Instead, it uses the failure function to look up the longest proper prefix of the keyword that is also a suffix of the part of the keyword we've already matched.This allows the algorithm to "slide" the keyword forward intelligently, bypassing redundant comparisons and achieving an $O(m + n)$ time complexity, where $m$ is the length of the text and $n$ is the length of the keyword.

Sincerely,

Juan Esteban Torres Peña

Mateo Duque Restrepo
