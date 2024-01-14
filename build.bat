set BUILD=c:\temp\build
set PACKAGE=cogwheel-0.2-py3-none-any.whl
set SRC=c:\Dropbox\SYS\Cogwheel
::rmdir /s /q %BUILD%
mkdir %BUILD%
robocopy %SRC% %BUILD%
pushd %BUILD%
python -m build
copy %BUILD%\dist\%PACKAGE% releases
popd
pip uninstall -y cogwheel
pip install releases\%PACKAGE%
