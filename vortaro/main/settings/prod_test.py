from vortaro.main.settings.prod import *

INSTALLED_APPS += ('django_jenkins',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
    },
    'loggers': {
    },
}
JENKINS_TASKS = (
    # 'django_jenkins.tasks.run_pylint',
    # 'django_jenkins.tasks.run_pep8',
    # 'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.with_coverage',
)