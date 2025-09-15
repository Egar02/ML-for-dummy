import subprocess


def test_task_2():
    result = subprocess.run(
        ["python", 'Module_1/Lesson_1/task_2.py'],
        capture_output=True,
        text=True
    )

    assert result.stdout.strip() == '*\n**\n***'
