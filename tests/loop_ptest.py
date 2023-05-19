from exercises.loop import for_search_good

def test_for_search_good(capsys):
    numbers = [5, 9, 7, 13, 15, 1, 11]
    item = 3
    for_search_good(numbers, item)
    stdout, stderr = capsys.readouterr()
    assert stdout == 'Item Not Found!\n'

# note: to execute this test: pytest loop_ptest.py -v
