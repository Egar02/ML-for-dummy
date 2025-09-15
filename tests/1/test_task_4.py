import pytest
import subprocess


@pytest.mark.parametrize("a, b, c, expected_output", [
    ("МИР!", "ТРУД!", "МАЙ!", "МАЙ!\nТРУД!\nМИР!"),
    ("Hello", "it's", "me", "me\nit's\nHello"),
    ("I love", "python", "so much", "so much\npython\nI love")

])
def test_task_4(a, b, c, expected_output):
    input_data = f"{a}\n{b}\n{c}\n"

    process = subprocess.Popen(
        ['python', 'Module_1/Lesson_1/task_4.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, _ = process.communicate(input=input_data)

    assert expected_output in stdout
