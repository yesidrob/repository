odoo.define('mi_modulo_grafica.grafica', function (require) {
    "use strict";

    const rpc = require('web.rpc');

    document.addEventListener('DOMContentLoaded', function () {
        const canvas = document.getElementById('graficaBarras');
        if (canvas) {
            rpc.query({ route: '/grafica/datos' }).then(function (data) {
                new Chart(canvas.getContext('2d'), {
                    type: 'bar',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Valores',
                            data: data.valores,
                            backgroundColor: 'rgba(54, 162, 235, 0.6)',
                        }]
                    }
                });
            });
        }
    });
});
