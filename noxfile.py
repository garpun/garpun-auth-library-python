import nox

TEST_DEPENDENCIES = [
    "flask",
    "mock",
    "oauth2client",
    "pytest",
    "pytest-cov",
    "pytest-localserver",
    "requests",
    "urllib3",
    "cryptography",
]

lint_dependencies = ["black", "flake8"]

BLACK_VERSION = "black==19.3b0"
BLACK_PATHS = ["garpunauth", "tests", "setup.py"]


@nox.session(python="3.7")
def lint(session):
    session.install(*lint_dependencies)
    session.run("black", "--check", *BLACK_PATHS)
    session.run("flake8", *BLACK_PATHS)
    session.run("python", "setup.py", "check", "--metadata", "--strict")


@nox.session(python="3.7")
def blacken(session):
    """Run black.
    Format code to uniform standard.
    This currently uses Python 3.6 due to the automated Kokoro run of synthtool.
    That run uses an image that doesn't have 3.6 installed. Before updating this
    check the state of the `gcp_ubuntu_config` we use for that Kokoro run.
    """
    session.install(BLACK_VERSION)
    session.run("black", *BLACK_PATHS)


@nox.session(python=["3.6", "3.7", "3.8"])
def tests(session):
    session.install(*TEST_DEPENDENCIES)
    session.install(".")
    session.run("pytest", "--cov=garpunauth", "--cov=tests", "tests")


@nox.session(python="3.7")
def cover(session):
    session.install(*TEST_DEPENDENCIES)
    session.install(".")
    session.run(
        "pytest", "--cov=garpunauth", "--cov=tests", "--cov-report=", "tests",
    )
    session.run("coverage", "report", "--show-missing", "--fail-under=0")
    session.run("coverage", "erase")
