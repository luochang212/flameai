import os
import shutil
import nox


@nox.session
def tests(session):
    # base env
    session.install('pytest')
    session.install('-e', '.')
    
    # copy files
    target_dir = './data'
    files = ['student.csv', 'course.csv']
    session.run('mkdir', '-p', target_dir, external=True)
    for f in files:
        source_dir = os.path.join(target_dir, f)
        shutil.copy(source_dir, target_dir)

    # test
    session.run('pytest')


@nox.session
def lint(session):
    session.install('flake8')
    session.install('flake8-import-order')
    session.run('flake8', '--import-order-style', 'google')
