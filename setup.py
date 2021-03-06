from setuptools import setup

setup(
    name="django-infranil",
    version="1.1.0",
    author="Anders Pearson",
    author_email="ctl-dev@columbia.edu",
    url="https://github.com/ccnmtl/django-infranil",
    description="almost flat pages",
    long_description="Almost Flat Pages",
    install_requires=[
        "Django",
    ],
    scripts=[],
    license="BSD",
    platforms=["any"],
    zip_safe=False,
    packages=['infranil'],
    include_package_data=True,
)
