import commands

from plugin import PluginMaster, PluginInstance
import session
import ui
import log
import config
import tools

from mako.template import Template
from mako.lookup import TemplateLookup

class DashboardPluginMaster(PluginMaster):
	name = 'Dashboard'

	def make_instance(self):
		i = DashboardPluginInstance(self)
		self.instances.append(i)
		return i


class DashboardPluginInstance(PluginInstance):
	name = 'Dashboard'

	def _on_load(self, s):
		PluginInstance._on_load(self, s)

		c = ui.Category()
		c.text = 'Dashboard'
		c.description = 'Server status'
		c.icon = 'plug/dashboard;icon'
		self.category_item = c

		log.info('DashboardPlugin', 'Started instance')

	def update(self):
		pass
	
	def get_html(self):
		ajenti_version = '&nbsp;Ajenti ' + config.ajenti_version
		distro_name = '&nbsp;' + tools.actions['core/detect-distro'].run()

		mylookup = TemplateLookup(directories=['htdocs'])
		template = Template(filename='plugins/dashboard/dashboard.html', lookup=mylookup)
		return template.render(plugins=self.session.plugins,
                serverName=config.server_name,
                ajentiVersion=ajenti_version,
                distroName=distro_name)
		
