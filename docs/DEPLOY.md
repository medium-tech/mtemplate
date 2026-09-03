
# deploying to pypi

## install build dependencies

    pip install -r requirements-dev.txt

## finalizing release
1. increment version in `pyproject.toml` file

1. run tests with `python -m unittest` from the root of the repo

## build and publish release

1. build distributions

        python3 -m build --sdist
        python3 -m build --wheel

1. check distributions for errors

        twine check dist/*

1. upload to pypi (will prompt for api key, no other config needed)

        twine upload dist/*