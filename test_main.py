 from main import *   

def test_word_count_map():
    assert word_count_map('i am sam i am') == \
           [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1)]
