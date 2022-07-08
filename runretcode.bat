@echo off

echo.
echo   _^|_^|    _^|_^|_^|    _^|      _^|    _^|_^|_^|  _^|      _^|
echo _^|    _^|  _^|    _^|    _^|  _^|    _^|        _^|_^|  _^|_^|
echo _^|_^|_^|_^|  _^|_^|_^|        _^|        _^|_^|    _^|  _^|  _^|
echo _^|    _^|  _^|    _^|      _^|            _^|  _^|      _^|
echo _^|    _^|  _^|_^|_^|        _^|      _^|_^|_^|    _^|      _^|
echo.
echo.

python -m returncode ^
python -m returncode ^
python -c "import random; import sys; sys.exit(random.randrange(0, 1 + 1))"
