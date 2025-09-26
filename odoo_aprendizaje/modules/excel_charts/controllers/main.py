from odoo import http
from odoo.http import request, content_disposition
import json
import logging

_logger = logging.getLogger(__name__)

class ExcelChartsController(http.Controller):

    @http.route('/excel_charts/import', type='json', auth='user')
    def import_excel(self, file, filename):
        """Endpoint para importar archivo Excel"""
        try:
            ExcelData = request.env['excel.data']
            result = ExcelData.import_excel_data(file, filename)
            
            return {
                'success': True,
                'message': 'Archivo importado correctamente',
                'record_id': result['record_id'],
                'data': result['data']
            }
        except Exception as e:
            _logger.error("Error en importación: %s", str(e))
            return {
                'success': False,
                'error': str(e),
                'message': 'Error al importar el archivo'
            }

    @http.route('/excel_charts/get_data/<int:record_id>', type='json', auth='user')
    def get_excel_data(self, record_id):
        """Obtener datos de un registro existente"""
        record = request.env['excel.data'].browse(record_id)
        if not record.exists():
            return {'success': False, 'error': 'Registro no encontrado'}
        
        try:
            return {
                'success': True,
                'data': json.loads(record.data)
            }
        except json.JSONDecodeError as e:
            _logger.error("Error JSON: %s", str(e))
            return {'success': False, 'error': 'Error al leer los datos'}