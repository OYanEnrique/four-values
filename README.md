# four-values
A Python script that analyzes four user-input numbers to count occurrences of 9, find the position of 3, and list all even numbers.

# 🔢 Four Values Analyzer

A command-line Python script that reads four integer values from the user, stores them in a tuple, and then performs a simple analysis on the data.

## Features

The script provides the following analysis:

* **Count Occurrences**: It counts and displays how many times the number `9` appears in the input.
* **Find Position**: It finds the first position where the number `3` was entered. If `3` is not found, it reports that as well.
* **Identify Even Numbers**: It iterates through all the entered numbers and prints out all the even ones.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `four_values.py`).
3.  Run the script from your terminal:
    ```sh
    python four_values.py
    ```
4.  The program will prompt you to enter four numbers, one after the other.
5.  After the fourth number is entered, the script will automatically print the analysis results.

### Example

```sh
> python four_values.py
Enter a number: 9
Enter a number: 3
Enter a number: 8
Enter a number: 9
The number 9 was entered 2 times
The number 3 was found in the 2° position
Even number found: 8
```
