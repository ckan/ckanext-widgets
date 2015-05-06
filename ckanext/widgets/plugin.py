from ckan import plugins
from ckan.plugins import toolkit
from ckanext.widgets import helpers


class WidgetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'widgets_fetch_feed': helpers.fetch_feed,
            'widgets_get_featured_feed': helpers.get_featured_feed,
        }
