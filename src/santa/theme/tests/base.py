from abita.basetheme.tests.base import IntegrationTestCase as BaseIntegrationTestCase
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import unittest


class SantaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import santa.theme
        self.loadZCML(package=santa.theme)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'santa.theme:default')

    def tearDownZope(self, app):
        """Tear down Zope."""


FIXTURE = SantaThemeLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="SantaThemeLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="SantaThemeLayer:Functional")


class IntegrationTestCase(BaseIntegrationTestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
