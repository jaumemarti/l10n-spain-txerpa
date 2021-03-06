# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) All rights reserved:
#        2013-2014 Servicios Tecnológicos Avanzados (http://serviciosbaeza.com)
#                  Pedro Manuel Baeza <pedro.baeza@serviciosbaeza.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Extractos bancarios españoles (Norma 43)",
    "version": "3.0",
    "author": "Spanish localization team",
    "website": "https://launchpad.net/openerp-spain",
    "category": "Localisation/Accounting",
    "description": """
Extractos bancarios españoles (Norma 43)
========================================

Importación y tratamiento de los extractos bancarios españoles que siguen la
norma/cuaderno 43 de la 'Asociación Española de la Banca'. Puede consultarse la
especificación del formato aquí_.

.. _aquí: http://goo.gl/2zzlmu

**AVISO:** Este módulo requiere de varios módulos del repositorio de código:

https://github.com/OCA/bank-statement-reconcile
    """,
    "license": "AGPL-3",
    "depends": [
        "l10n_es",
        'account_statement_base_import',
        'account_statement_base_completion',
    ],
    "data": [
        "views/account_bank_statement_view.xml",
        "data/account_statement_completion_rule_data.xml",
    ],
    "installable": True,
}
