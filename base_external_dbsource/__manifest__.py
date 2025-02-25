# Copyright <2011> <Daniel Reis, Maxime Chambreuil, Savoir-faire Linux>
# Copyright <2016> <Henry Zhou MAXodoo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "External Database Sources",
    "version": "16.0.1.0.1",
    "category": "Tools",
    "author": "Daniel Reis, " "LasLabs, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-backend",
    "license": "LGPL-3",
    "images": ["images/screenshot01.png"],
    "depends": ["base"],
    "data": [
        "views/base_external_dbsource.xml",
        "security/ir.model.access.csv",
        "security/base_external_dbsource_security.xml",
    ],
    "demo": ["demo/base_external_dbsource.xml"],
    "installable": True,
}
