from setuptools import setup

setup(
    name="django-infranil",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
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
    test_suite='nose.collector',
    include_package_data=True,
)
