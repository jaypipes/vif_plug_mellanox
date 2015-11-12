#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from os_vif import plugin
from os_vif import objects

from vif_plug_mellanox import processutils

PLUGIN_NAME = 'mlnx_direct'

_DEV_PREFIX_ETH = 'eth'


class MellanoxDirectPlugin(plugin.PluginBase):
    """
    A VIF type that plugs the interface directly into the Mellanox physical
    network fabric.
    """

    def __init__(self, **config):
        processutils.configure(**config)

    def get_supported_vifs(self):
        return set([objects.PluginVIFSupport(PLUGIN_NAME, '1.0', '1.0')])

    def plug(self, instance, vif):
        vnic_mac = vif.address
        device_id = instance.uuid
        fabric = vif.physical_network
        if not fabric:
            raise exception.NetworkMissingPhysicalNetwork(
                network_uuid=vif.network.id)
        dev_name = vif.devname_with_prefix(_DEV_PREFIX_ETH)
        processutils.execute('ebrctl', 'add-port', vnic_mac,
                             device_id, fabric, PLUGIN_NAME, dev_name,
                             run_as_root=True)

    def unplug(self, vif):
        vnic_mac = vif.address
        fabric = vif.physical_network
        if not fabric:
            raise exception.NetworkMissingPhysicalNetwork(
                network_uuid=vif.network.id)
        processutils.execute('ebrctl', 'del-port', fabric, vnic_mac,
                             run_as_root=True)
