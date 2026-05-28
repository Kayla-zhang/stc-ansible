STC Ansible Documentation
=========================

STC Ansible is an experimental Ansible plugin to configure VIAVI TestCenter
data models and execute tests. It lets you describe BGP, OSPF, DHCP, IGMP/MLD,
VXLAN, and other test scenarios declaratively in Ansible playbooks and run
them against a VIAVI TestCenter LabServer.

.. note::
   **STC** is short for **VIAVI TestCenter**. The lowercase ``stc`` prefix is used
   throughout this module's Ansible action keywords (``stc:``), inventory groups,
   and configuration values.

The plugin source lives on `GitHub
<https://github.com/Viavi-TestCenter/stc-ansible>`_.

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   Getting_Started

.. toctree::
   :maxdepth: 2
   :caption: Sessions and ports

   Session
   Port
   EmulatedDevice

.. toctree::
   :maxdepth: 2
   :caption: Routing protocols

   BGP
   OSPF

.. toctree::
   :maxdepth: 2
   :caption: Address assignment and multicast

   DHCP
   IGMP
   MLD
   Multicast

.. toctree::
   :maxdepth: 2
   :caption: Overlays and traffic

   VXLAN
   StreamBlock

.. toctree::
   :maxdepth: 2
   :caption: Execution and results

   Start_Protocols
   Results
   System

.. toctree::
   :maxdepth: 2
   :caption: Maintenance

   Tags
   Delete_Objects


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
