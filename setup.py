from setuptools import setup, find_packages
import os

version = '0.2.dev0'

setup(name='ploneawards.policy',
      version=version,
      description="ploneawards Policy",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Maarten Kling',
      author_email='maarten@fourdigits.nl',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel", "fourdigits.skeleton"],
      )
