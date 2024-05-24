import nox


@nox.session(python=['3.8', '3.9', '3.10', '3.11', '3.12'])
def tests(session):
    session.install('pytest')
    session.install('-e', '.')
    session.run('pytest')


@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8')
