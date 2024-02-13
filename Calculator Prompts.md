MODEL: Codellama 7B Q4_K_M by TheBloke

1:Write me a simple calculator program in Python that can add, subtract, multiply, and divide.

NOTES:

Honestly I am very satisfied with the first results. I would try to push for more but TBH I don't really see what I could do different.

2: Reject the input if the user attempts to divide by zero. Call them a "Naughty Pookie"

NOTES: Decided to add handling for dividing by zero. Also seeing if it can do *any* normal text handling. Appears not though.

3: Add error handling for all possible invalid inputs.

NOTES: Casting a very wide net. Seeing if it can recognize that it will error if you multiply by zero (It doesn't) [IT DIDN'T CHANGE THE CODE]

4: Multiplying by zero produces an error. Fix it. ValueError: invalid literal for int() with base 10: 'multiply'

NOTES: Being direct with it seems to work.
