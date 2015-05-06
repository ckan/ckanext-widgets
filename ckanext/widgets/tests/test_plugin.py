"""Tests for plugin.py."""
import os

from ckan.new_tests import helpers

from nose.tools import assert_true


class TestFrontPageFeed(helpers.FunctionalTestBase):
    @classmethod
    def _apply_config_changes(cls, cfg):
        atom10 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'atom10.xml')
        cfg['ckanext.widgets.featured_feed'] = open(atom10).read()

    def test_front_page_layout(self):
        response = TestFrontPageFeed._test_app.get(url='/')
        assert_true('Example Feed' in response.body)
        assert_true('A subtitle' in response.body)
        assert_true('Atom-Powered Robots Run Amok' in response.body)
        assert_true('Some text.' in response.body)

