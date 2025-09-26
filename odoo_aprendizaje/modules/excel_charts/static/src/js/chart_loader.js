odoo.define('excel_charts.ChartLoader', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var _t = core._t;

    var ExcelChartAction = AbstractAction.extend({
        template: 'excel_charts.Template',
        events: {
            'click .o_import_excel': '_onImportExcel',
            'click .o_download_example': '_onDownloadExample'
        },

        init: function(parent, context) {
            this._super(parent, context);
            this.record_id = context.active_id;
            this.plotlyLoaded = false;
        },

        willStart: function() {
            var self = this;
            return this._super().then(function() {
                return self._loadPlotly().then(function() {
                    if (self.record_id) {
                        return self._loadChartData();
                    }
                    return Promise.resolve();
                });
            });
        },

        _loadPlotly: function() {
            var self = this;
            return new Promise(function(resolve) {
                if (window.Plotly) {
                    self.plotlyLoaded = true;
                    return resolve();
                }
                
                var script = document.createElement('script');
                script.type = 'text/javascript';
                script.src = 'https://cdn.plot.ly/plotly-2.24.1.min.js';
                script.onload = function() {
                    self.plotlyLoaded = true;
                    resolve();
                };
                script.onerror = function() {
                    console.error("Error al cargar Plotly.js");
                    resolve();
                };
                document.head.appendChild(script);
            });
        },

        _onImportExcel: function(ev) {
            ev.preventDefault();
            var self = this;
            
            var $input = $('<input>', {
                type: 'file',
                accept: '.xlsx,.xls,.csv'
            });
            
            $input.on('change', function(e) {
                var file = e.target.files[0];
                if (!file) return;
                
                var reader = new FileReader();
                reader.onload = function(e) {
                    var binary = '';
                    var bytes = new Uint8Array(e.target.result);
                    for (var i = 0; i < bytes.byteLength; i++) {
                        binary += String.fromCharCode(bytes[i]);
                    }
                    
                    rpc.query({
                        route: '/excel_charts/import',
                        params: {
                            file: window.btoa(binary),
                            filename: file.name
                        }
                    }).then(function(result) {
                        if (result.success) {
                            self.record_id = result.record_id;
                            self._renderCharts(result.data);
                            self.displayNotification({
                                title: _t("Éxito"),
                                message: result.message,
                                type: 'success'
                            });
                        } else {
                            self.displayNotification({
                                title: _t("Error"),
                                message: result.message || 'Error desconocido',
                                type: 'danger'
                            });
                        }
                    });
                };
                reader.readAsArrayBuffer(file);
            });
            
            $input.click();
        },

        _loadChartData: function() {
            var self = this;
            return rpc.query({
                route: '/excel_charts/get_data/' + this.record_id
            }).then(function(result) {
                if (result.success) {
                    self._renderCharts(result.data);
                }
            });
        },

        _renderCharts: function(data) {
            if (!this.plotlyLoaded) {
                console.error("Plotly.js no está cargado");
                return;
            }

            // Limpiar contenedores
            $('#pieChart').empty();
            $('#barChart').empty();

            // Validar datos
            if (!data || !data.rows || data.rows.length === 0) {
                console.warn("No hay datos para mostrar");
                return;
            }

            try {
                var xValues = data.rows.map(function(row) { 
                    return row[data.headers[0]] || ''; 
                });
                
                var yValues = data.rows.map(function(row) {
                    var val = row[data.headers[1]] || 0;
                    return typeof val === 'number' ? val : parseFloat(val) || 0;
                });

                // Gráfico de Torta
                Plotly.newPlot('pieChart', [{
                    values: yValues,
                    labels: xValues,
                    type: 'pie',
                    textinfo: 'percent+label',
                    hoverinfo: 'label+percent+value',
                    textposition: 'inside',
                    automargin: true,
                    marker: {
                        colors: ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
                    }
                }], {
                    title: data.headers[0] || 'Distribución',
                    margin: {t: 30, b: 30, l: 30, r: 30}
                });

                // Gráfico de Barras
                Plotly.newPlot('barChart', [{
                    x: xValues,
                    y: yValues,
                    type: 'bar',
                    marker: {
                        color: 'rgba(55, 128, 191, 0.7)',
                        line: {
                            color: 'rgba(55, 128, 191, 1.0)',
                            width: 1.5
                        }
                    }
                }], {
                    title: data.headers[1] || 'Valores',
                    xaxis: {title: data.headers[0] || 'Categorías'},
                    yaxis: {title: data.headers[1] || 'Valores'},
                    margin: {t: 30, b: 80, l: 60, r: 30}
                });

            } catch (error) {
                console.error("Error al renderizar gráficos:", error);
            }
        }
    });

    core.action_registry.add('excel_charts_action', ExcelChartAction);
    return ExcelChartAction;
});