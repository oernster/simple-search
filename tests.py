import os
import tempfile
from io import StringIO
import pytest
from simplesearch import SimpleSearch, QuitSearch
from unittest.mock import patch

@pytest.fixture
def mock_files():
    # Create temporary directory and files for testing
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create temporary files
        file1 = os.path.join(tmp_dir, 'file1.txt')
        with open(file1, 'w') as f:
            f.write("test1 test2 test3\n")
            f.write("test2 test3 test4\n")

        file2 = os.path.join(tmp_dir, 'file2.txt')
        with open(file2, 'w') as f:
            f.write("test1 test2 test3\n")
            f.write("test2 test3 test4\n")
            f.write("test4 test5 test6\n")

        yield tmp_dir

def test_search_with_input(mock_files):
    # Mock user input
    user_input = 'test2\n:quit\n'

    # Redirect stdout for checking output
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('builtins.input', side_effect=user_input.split('\n')) as mock_input:
            try:
                search = SimpleSearch(mock_files)
                search.run()
            except SystemExit:
                pass  # Prevent the exit call from causing test failure

            # Check if the expected output is printed
            assert mock_stdout.getvalue() == "file1.txt: 100%\nfile2.txt: 100%\n"

def test_display_results_with_matches_with_input(mock_files):
    # Mock user input
    user_input = 'test2 test3 test4\n:quit\n'

    # Redirect stdout for checking output
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('builtins.input', side_effect=user_input.split('\n')) as mock_input:
            try:
                search = SimpleSearch(mock_files)
                search.run()
            except SystemExit:
                pass  # Prevent the exit call from causing test failure

            # Check if the expected output is printed
            assert mock_stdout.getvalue() == "file1.txt: 100%\nfile2.txt: 100%\n"


def test_display_results_no_matches_with_input(mock_files):
    # Mock user input
    user_input = 'xyz\n:quit\n'
    
    # Redirect stdout for checking output
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with patch('builtins.input', side_effect=user_input.split('\n')) as mock_input:
            try:
                search = SimpleSearch(mock_files)
                search.run()
            except SystemExit:
                pass  # Prevent the exit call from causing test failure

            # Check if the expected output is printed
            assert mock_stdout.getvalue() == "No matches found.\n"
