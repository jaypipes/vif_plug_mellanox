=================
vif_plug_mellanox
=================

An `os-vif` VIF plugin for plugging and unplugging virtual interfaces that use
Mellanox NICs via a direct vNIC type.

Features
--------

* A `vif_plug_mellanox.mellanox.MellanoxDirectPlugin` VIF plugin that directly
  plugs into a Mellanox NIC.

Installation
------------

Install the OVS VIF plugins using `pip`::

    sudo pip install vif_plug_mellanox

After doing so, the `os-vif` library's `initialize()` method will automatically
load the Mellanox VIF plugin in this library and allow Nova and any other
system to plug VIFs that use Mellanox NICs in some capacity.

Configuration
-------------

The following configuration options are used by the
`vif_plug_mellanox.mellanox.MellanoxDirectPlugin` VIF plugin and are passed from the
`os_vif.initialize(**config)` function:

* `disable_rootwrap` -- Defaults to `False`. Override to entirely disable any
  use of rootwrap and instead rely solely on sudoers files.
* `use_rootwrap_daemon` -- Defaults to `False`. Override to enable the rootwrap
  daemon mode which can increase the performance of root-run commands.
* `rootwrap_config` -- Defaults to `'/etc/nova/rootwrap.conf'`. Path to the
  `oslo.rootwap` config file.
