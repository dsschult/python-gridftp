import os
import sys
import platform
import glob
from distutils.core import setup, Extension

version="1.4.0"
GLOBUS_LOCATION = "/usr"

try:
    GLOBUS_LOCATION = os.environ["GLOBUS_LOCATION"]
except KeyError:
    print >> sys.stderr, "GLOBUS_LOCATION is not set; using default %s" %(GLOBUS_LOCATION)

linkFlags = [
"-Bstatic",
"-L%s/lib64" % GLOBUS_LOCATION,
"-lglobus_ftp_client",
"-lglobus_io",
"-lglobus_common",
"-Bdynamic"
]

my_include_dirs=["%s/include/globus"%GLOBUS_LOCATION]
for dir in glob.iglob("%s/include/globus/*"%GLOBUS_LOCATION):
    if os.path.isdir(dir):
        my_include_dirs.append(dir)
if os.path.exists("/usr/lib/globus/include"):
    my_include_dirs.append("/usr/lib/globus/include")
elif os.path.exists("/usr/lib64/globus/include"):
    my_include_dirs.append("/usr/lib64/globus/include")

e = Extension(
        "gridftpwrapper",
        ["gridftpwrapper.c"],
        include_dirs=my_include_dirs,
        extra_compile_args=["-O1", "-Wno-strict-prototypes", "-D_FORTIFY_SOURCE=2", "-fstack-protector"],
        extra_link_args=linkFlags
        )

extModList = [e]

setup(name="python-gridftp",
      version=version,
      description="Python GridFTP client bindings",
      author="Jeff Kline",
      author_email="kline@gravity.phys.uwm.edu",
      url="http://www.lsc-group.phys.uwm.edu/LDR",
      py_modules=["gridftpClient", "gridftpwrapper"],
      ext_modules=extModList
      )
