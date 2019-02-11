import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

class DemoPlugin(BasePlugin):
  def query(self, **kwargs):
    pgi = self.find_single_process_group(pgi_name('Apache Web Server httpd'))
    pgi_id = pgi.group_instance_id
    stats_url = "http://localhost"
    stats = json.loads(requests.get(stats_url).content.decode())
    self.results_builder.absolute(key='randomNumber', value=stats['randomNumber'], entity_id=pgi_id)
