import subprocess


def test_task_2():
    result = subprocess.run(
        ["python", 'module_1/1/task_2.py'],
        capture_output=True,
        text=True
    )

    assert result.stdout.strip() == '*\n**\n***'
