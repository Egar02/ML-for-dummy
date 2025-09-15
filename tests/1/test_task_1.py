import subprocess


def test_task_1():
    result = subprocess.run(
        ["python", 'module_1/1/task_1.py'],
        capture_output=True,
        text=True
    )

    assert result.stdout.strip() == '4 8 15 16 23 42'
