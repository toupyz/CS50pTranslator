import os
import pytest
import project

HIGHSCORE_FILE = project.HIGHSCORE_FILE

@pytest.fixture(autouse=True)
def cleanup_file(): # This fixture runs before and after each test to clean the file
    if os.path.exists(HIGHSCORE_FILE):
        os.remove(HIGHSCORE_FILE)
    yield
    if os.path.exists(HIGHSCORE_FILE):
        os.remove(HIGHSCORE_FILE)


def test_load_highscore_when_file_missing(): # When the highscore file doesn't exist, load_highscore should return 0
    assert project.load_highscore() == 0


def test_save_and_load_highscore(): # Save a highscore and then load it back
    project.save_highscore(77)
    assert project.load_highscore() == 77


def test_ask_question_correct_answer(): # Given specific numbers and correct answer, returns True
    assert project.ask_question(a=6, b=7, user_answer=42) is True


def test_ask_question_wrong_answer(): # Given specific numbers and wrong answer, returns False
    assert project.ask_question(a=6, b=7, user_answer=40) is False

