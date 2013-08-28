# -*- coding: utf-8 -*-

from ploneawards.policy.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

PROJECTNAME = 'ploneawards.policy'
DEPENDENCIES = [
    'ploneawards.theme',
    'ploneawards.contenttypes',
    'fourdigits.portlet.twitter',
    'collective.carousel',
]


class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)

        self.assertFalse(
            result,
            "These dependencies are not installed: " + ", ".join(result)
        )


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
