# simple-search
A simple search tool for searching a directory of text files for keywords

To run:

Install Python (I'm using v3.12.3)

On the command prompt: python simplesearch.py <path to directory with text files in>

You will be given a search prompt.  You can either enter ':quit' to quit, or enter multiple words.

The words will be reported in rank order (top ten) of percentage content in the files.

I have provided an example set of files in the files subdirectory for you to search on a subject matter that interests me.

# Tests

There are also test cases.

To run the test cases, first create a virtual environment and activate it from a command prompt or terminal.

Then run:

pip install pytest.

Then run:

pytest -s tests.py
