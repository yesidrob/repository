from odoo import models, fields, api
import base64
import xlrd
import json
from odoo.exceptions import UserError

class ExcelData(models.Model):
    _name = 'excel.data'
    _description = 'Datos importados desde Excel'

    name = fields.Char('Nombre del archivo', required=True)
    file = fields.Binary('Archivo Excel', required=True)
    date_import = fields.Datetime('Fecha de importación', default=fields.Datetime.now)
    data = fields.Text('Datos en JSON')

    def import_excel_data(self, file_data, file_name):
        """Método mejorado para importar datos desde Excel"""
        try:
            file_content = base64.b64decode(file_data)
            workbook = xlrd.open_workbook(file_contents=file_content)
            sheet = workbook.sheet_by_index(0)
            
            # Validación básica
            if sheet.ncols < 2 or sheet.nrows < 2:
                raise UserError("El archivo debe tener al menos 2 columnas y 1 fila de datos")
            
            # Procesar encabezados
            headers = [str(sheet.cell_value(0, col)).strip() or f"Columna {col+1}" 
                      for col in range(sheet.ncols)]
            
            # Procesar filas
            rows = []
            for row_idx in range(1, sheet.nrows):
                row_data = {}
                for col in range(sheet.ncols):
                    cell_value = sheet.cell_value(row_idx, col)
                    # Convertir fechas Excel
                    if sheet.cell_type(row_idx, col) == xlrd.XL_CELL_DATE:
                        cell_value = xlrd.xldate_as_datetime(cell_value, workbook.datemode)
                    row_data[headers[col]] = cell_value
                rows.append(row_data)
            
            # Validar datos numéricos
            numeric_col = 1 if len(headers) > 1 else 0
            numeric_values = [row.get(headers[numeric_col], 0) for row in rows]
            
            json_data = {
                'headers': headers,
                'rows': rows,
                'has_numeric_data': any(isinstance(v, (int, float)) for v in numeric_values)
            }
            
            # Buscar o crear registro
            record = self.search([('name', '=', file_name)], limit=1)
            if record:
                record.write({
                    'file': file_data,
                    'date_import': fields.Datetime.now(),
                    'data': json.dumps(json_data, default=str)
                })
            else:
                record = self.create({
                    'name': file_name,
                    'file': file_data,
                    'data': json.dumps(json_data, default=str)
                })
            
            return {
                'success': True,
                'record_id': record.id,
                'data': json_data
            }
            
        except Exception as e:
            raise UserError(f"Error al procesar el archivo: {str(e)}")