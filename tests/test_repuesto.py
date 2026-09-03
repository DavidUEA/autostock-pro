import pytest
from src.repuesto import Repuesto, InventarioService

def test_no_permite_precio_invalido():
    """CP-01: Rechaza repuestos con precio negativo o cero"""
    with pytest.raises(ValueError, match="El precio debe ser mayor a cero."):
        Repuesto("REP-01", "Pastilla de Freno", "Bosch", -10.0, 5)

def test_registro_y_consulta_exitosa():
    """CP-04: Caso Crítico - Registro y recuperación de repuesto"""
    servicio = InventarioService()
    item = Repuesto("REP-100", "Bomba de Agua", "Gates", 45.50, 10)
    servicio.registrar_repuesto(item)
    
    recuperado = servicio.buscar_por_codigo("REP-100")
    assert recuperado is not None
    assert recuperado.nombre == "Bomba de Agua"
    assert recuperado.stock == 10