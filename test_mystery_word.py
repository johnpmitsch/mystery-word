import mystery_word as myst


def test_open_file():
    assert myst.open_file('sample_words.txt') == ["dog", "cat",
                                                          "bear", "owl"]

def test_random_word():
    assert myst.get_random_word() in myst.open_file('/usr/share/dict/words')

def test_word_length():
    assert myst.word_length("cattle") == 6

def test_valid_user_input():
    assert myst.valid_user_input('a') == True
    assert myst.valid_user_input('ab') == False
    assert myst.valid_user_input('A') == True
    assert myst.valid_user_input('/') == False
    assert myst.valid_user_input(',') == False
    assert myst.valid_user_input('long string') == False

def test_guess_in_word():
    assert myst.guess_in_word('a', 'pear') == True
    assert myst.guess_in_word('X', 'axe') == True

def test_hide_letters():
    assert myst.hide_letters(['q','i'], 'quick') == ['q', '_', 'i', '_', '_']

def test_check_guesses_remaining():
    assert myst.check_guesses_remaining(8) == True
    assert myst.check_guesses_remaining(1) == True
    assert myst.check_guesses_remaining(0) == False
    assert myst.check_guesses_remaining(-1) == False

def test_win_game():
    assert myst.win_game(['a', 'p', 'l', 'e', 'r'], 'apple') == True
    assert myst.win_game(['z', 'p', 'l', 'e', 'r'], 'pear') == False

def test_not_guessed_before():
    assert myst.not_guessed_before('a', ['a', 'b', 'f']) == False
    assert myst.not_guessed_before('b', ['a', 'c', 'd']) == True

def test_validate_guess():
    assert myst.validate_guess('a', ['b', 'c', 'd']) == True
    assert myst.validate_guess('c', ['b', 'c', 'd']) == False
    assert myst.validate_guess('ba', ['a', 'v', 'x']) == False

def test_display_word():
    assert myst.display_word(['a', 'e', 'i'], "bait") == ["_", "a", "i", "_"]

def test_choose_difficulty():
    easy_word = myst.word_difficulty('easy')
    normal_word = myst.word_difficulty('normal')
    hard_word = myst.word_difficulty('hard')

    assert len(easy_word) >= 4 and len(easy_word) <= 6
    assert len(normal_word) >= 6 and len(normal_word) <= 10
    assert len(hard_word) >= 10

def test_play_again():
    assert myst.play_again('y') == True
    assert myst.play_again('n') == False

def test_initialize_game():
    myst.initialize_game()
    assert myst.guesses_remaining == 8
    assert myst.user_guesses == []
    assert myst.new_game == True
