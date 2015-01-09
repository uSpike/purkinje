# -*- coding: utf8 -*-

"""Static web assets (JS, CSS, etc.)
"""

from flask.ext.assets import Bundle, Environment


BC = 'bower_components'
JS = 'js'
THIRDPARTY = JS + '/thirdparty'
CONTROLLERS = JS + '/controllers'
DIRECTIVES = JS + '/directives'
SERVICES = JS + '/services'

# paths are relative to the 'static' directory
BUNDLES = {
    'css': Bundle(
        BC + '/bootstrap/dist/css/bootstrap.css',
        BC + '/bootstrap/dist/css/bootstrap-theme.css',
        BC + '/sass-bootstrap-glyphicons/css/bootstrap-glyphicons.css',
        BC + '/angular-ui-grid/ui-grid.css',

        BC + '/fontawesome/css/font-awesome.css',

        'css/thirdparty/dashboard.css',

        'css/purkinje.css',
        'css/default.css',

        filters='cssmin',
        output='gen/packed.css'
    ),
    'js': Bundle(
        BC + '/underscore/underscore.js',
        BC + '/angular/angular.js',
        BC + '/angular-bootstrap/ui-bootstrap.js',
        BC + '/angular-bootstrap/ui-bootstrap-tpls.js',
        BC + '/ui-router/release/angular-ui-router.js',
        BC + '/angular-ui-grid/ui-grid.js',
        BC + '/simple-statistics/src/simple_statistics.js',
        BC + '/ng-blink/ng-blink.js',

        BC + '/Chart.js/Chart.js',
        BC + '/tc-angular-chartjs/dist/tc-angular-chartjs.js',

        THIRDPARTY + '/histogramjs/histogram.js',

        JS + '/util.js',
        JS + '/defs.js',
        JS + '/app.js',
        JS + '/config.js',
        JS + '/routes.js',
        JS + '/runblocks.js',

        DIRECTIVES + '/test_activity_directive.js',

        CONTROLLERS + '/navbar_controller.js',
        CONTROLLERS + '/test_results_table_controller.js',
        CONTROLLERS + '/server_settings_controller.js',

        JS + '/filters.js',

        SERVICES + '/underscore.angular.js',
        SERVICES + '/websocket_service.js',
        SERVICES + '/avviso_service.js',

        filters='jsmin',
        output='gen/packed.js'
    )
}


def register_assets(app):
    """Make assets known to flask assets extension"""
    assets = Environment(app)
    assets.register(BUNDLES)
    return assets
