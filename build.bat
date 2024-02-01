set BUILD=c:\Tofu\Temp\Build
set PACKAGE=cogwheel-0.1-py3-none-any.whl
set SRC=X:\Projects\Cogwheel
rmdir /s /q %BUILD%

mkdir %BUILD%
robocopy %SRC% %BUILD% /MIR
pushd %BUILD%
python -m build
popd
copy /y %BUILD%\dist\%PACKAGE% releases
pip uninstall -y cogwheel
pip install releases\%PACKAGE%
