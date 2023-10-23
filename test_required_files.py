import os

def test_required_files_exist():
    assert os.path.exists('noteBG/A.png')
    assert os.path.exists('noteBG/B.png')