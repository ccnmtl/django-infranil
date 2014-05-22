from setuptools import setup, find_packages

setup(
    name="django-infranil",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="http://wiki.ccnmtl.columbia.edu/",
    description="almost flat pages",
    long_description="Almost Flat Pages",
    install_requires = [
        "Django",
    ],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    packages=['pagetree'],
    test_suite='nose.collector',
    include_package_data=True,
)
