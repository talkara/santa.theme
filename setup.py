from setuptools import find_packages
from setuptools import setup


setup(
    name='santa.theme',
    version='0.3',
    description="Theme for Santa site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='ABITA',
    author_email='taito.horiuchi@abita.fi',
    url='http://santa.abita.fi/',
    license='Non-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['santa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone>=4.2',
        'five.pt',
        'hexagonit.testing',
        'plone.app.theming',
        'plone.app.themingplugins',
        'santa.templates',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
