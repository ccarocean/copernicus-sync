from invoke import Collection, task

PACKAGE = "copsync"


@task
def check(c):
    """check code style"""
    c.run(f"flake8 setup.py tasks.py {PACKAGE}")


@task
def develop(c):
    """install development dependencies"""
    c.run(f"pip install --upgrade flake8 flake8-bugbear pydocstyle black isort")


@task
def format_isort(c):
    """sort imports"""
    c.run(f"isort -rc {PACKAGE} .")


@task
def format_black(c):
    """format the codebase with black"""
    c.run(f"black {PACKAGE} .")


@task(format_isort, format_black)
def format_all(c):
    """isort + black."""


format = Collection("format")
format.add_task(format_all, "all", default=True)
format.add_task(format_isort, "isort")
format.add_task(format_black, "black")

ns = Collection()
ns.add_task(check)
ns.add_task(develop)
ns.add_collection(format)
