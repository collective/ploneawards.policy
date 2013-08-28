# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '0.2.dev0'
long_description = (
    open('README.rst').read() + '\n' +
#    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='ploneawards.policy',
      version=version,
      description="ploneawards Policy",
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Maarten Kling',
      author_email='maarten@fourdigits.nl',
      url='https://github.com/collective/ploneawards.policy',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneawards'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ploneawards.theme',
          'ploneawards.contenttypes',
          'fourdigits.portlet.twitter',
          'collective.carousel',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.testing',
              'zope.component',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
