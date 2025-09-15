import pytest
import subprocess


@pytest.mark.parametrize("input_team, expected_output", [
    ("Ливерпуль", "Ливерпуль - чемпион!"),
    ("Барселона", "Барселона - чемпион!"),
    ("Наполи", "Наполи - чемпион!"),
    ("", "- чемпион!")
])
def test_task_3(input_team, expected_output):
    result = subprocess.run(
        ["python", 'Module_1/Lesson_1/task_3.py'],
        input=input_team + "\n",
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == expected_output
