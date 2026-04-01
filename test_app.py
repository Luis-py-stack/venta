import os

def test_app_imports():
    """Test para validar que la aplicación se pueda importar correctamente."""
    try:
        import app
        imported = True
    except ImportError:
        imported = False

    assert imported == True, "El módulo app.py falló al importarse."

def test_files_exist():
    """Test básico para verificar la existencia de archivos importantes."""
    assert os.path.exists("app.py"), "Falta app.py"
    assert os.path.exists("requirements.txt"), "Falta requirements.txt"
    assert os.path.exists("README.md"), "Falta README.md"