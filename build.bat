set BUILD=c:\temp\build
set PACKAGE=cogwheel-0.1-py3-none-any.whl
set SRC=c:\Dropbox\SYS\Cogwheel
rmdir /s /q %BUILD%

mkdir %BUILD%
robocopy %SRC% %BUILD% /MIR
pushd %BUILD%
python -m build
popd
copy /y %BUILD%\dist\%PACKAGE% releases
pip uninstall -y cogwheel
pip install releases\%PACKAGE%
