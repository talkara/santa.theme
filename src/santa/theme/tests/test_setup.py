from Products.CMFCore.utils import getToolByName
from abita.utils.utils import get_css_resource
from santa.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.theme'))

    def test_browserlayer(self):
        from santa.theme.browser.interfaces import ISantaThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ISantaThemeLayer, utils.registered_layers())

    def test_cssregistry__santa_theme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__santa_theme_main__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__santa_theme_main__compression(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__santa_theme_main__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__santa_theme_main__cookable(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__santa_theme_main__enabled(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__santa_theme_main__expression(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__santa_theme_main__media(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__santa_theme_main__rel(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__santa_theme_main__rendering(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__santa_theme_main__title(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__santa_theme_extra__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__santa_theme_extra__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__santa_theme_extra__compression(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__santa_theme_extra__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__santa_theme_extra__cookable(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__santa_theme_extra__enabled(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__santa_theme_extra__expression(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__santa_theme_extra__media(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__santa_theme_extra__rel(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__santa_theme_extra__rendering(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__santa_theme_extra__title(self):
        resource = get_css_resource(self.portal, '++resource++santa.theme/css/extra.css')
        self.assertIsNone(resource.getTitle())

    def test_metadata__dependency__abita_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('abita.basetheme'))

    def test_metadata__dependency__PloneFormGen(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('PloneFormGen'))

    def test_metadata__dependency__collective_prettyphoto(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.prettyphoto'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-santa.theme:default'), u'2')

    def test_viewlets__hidden__plone_portalheader(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalheader"
        skinname = "*"
        self.assertIn(u'plone.searchbox', storage.getHidden(manager, skinname))

    def test_viewlets__hidden__plone_portalfooter(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"
        skinname = "*"
        for viewlet in (
            u'plone.colophon',
            u'plone.site_actions'):
            self.assertIn(viewlet, storage.getHidden(manager, skinname))

    def test_uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.failIf(installer.isProductInstalled('santa.theme'))

    def test_uninstall_browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        from santa.theme.browser.interfaces import ISantaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISantaThemeLayer, utils.registered_layers())

    def test_uninstall_cssregistry__santa_theme_main(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.assertIsNone(get_css_resource(self.portal, '++resource++santa.theme/css/main.css'))

    def test_uninstall_cssregistry__santa_theme_extra(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.assertIsNone(get_css_resource(self.portal, '++resource++santa.theme/css/extra.css'))
