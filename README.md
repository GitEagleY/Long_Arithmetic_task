# Long Long Arithmetic

## Prerequisites

Before you begin, ensure you have the following installed:

- Python: [Download Python](https://www.python.org/downloads/)

## Installation

1.  Clone the repository:

2.  Navigate to the project directory:

3.  Install the dependencies:

        pip install -r requirements.txt

## Example Usage

To run the program, navigate to the project directory and execute:

        python main.py

You should follow the program's instructions after running it and get something like this:

```
Enter the first number: 4567

Enter the second number: 1234

Result of FFT multiplication: 5635678

Result of Karatsuba multiplication: 5635678

```

## Running Tests

To run the tests, navigate to the project directory and execute:

    python test_main.py

## Test coverage

If you want to run test coverage, run following commands:

    coverage run -m unittest test_main.py
    coverage report -m

For html version:

    coverage run -m unittest test_main.py
    coverage html

## How i tried to implement this using Go

While building this project, I spent a day and a half trying to reinvent everything in Go from scratch, and I was having some trouble with the multiplication algorithms.
So I decided to use Go's built-in 'math/big' lib to continue doing this in Go, but after a few more hours of trying to implement Karatsuba algorithm, things again became very complex and difficult to understand.
So in the end I decided to move to Python where there is a simpler implementation of Karatsuba algorithm and numpy to implement FFT, IFFT.

## Big O for Basic Multiplication

The Basic Multiplication algorithm of O(N^2):

2N for individual multiplication + 2N for carry overs + N-1~N(additions)+ Normally each addition would need 2N steps, But theres Numbers as twice as large and overall addition gives us 4N^2 steps.

So in total we get:
O(N^2)

## Big O for Karatsuba Algorithm

The Karatsuba algorithm used in this project has a time complexity of O(N^log2(3)), which is approximately O(N^1.585).

## Big O for FFT Algorithm

The Fast Fourier Transform algorithm used in this project has a time complexity of O(N\*log(N)).

## Time spent

During this project i have spent the most time during research and when i was trying to figure out what was different multiplication algorithms about. So project took around 10h of writing different implementations and around the same time of research. Project was done in 4 days with breaks.

Summary:
10+ hours writing code
12+ hours research
