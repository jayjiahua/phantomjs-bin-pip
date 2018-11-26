import os
import platform

BINARY_VERSION = '2.1.1'


def _get_executable_path():

    os_type_mapping = {
        "Windows": {
            "dir": "windows",
            "files": {
                "32bit": "phantomjs.exe",
                "64bit": "phantomjs.exe",
            }
        },
        "Darwin": {
            "dir": "macosx",
            "files": {
                "32bit": "phantomjs",
                "64bit": "phantomjs",
            }
        },
        "Linux": {
            "dir": "linux",
            "files": {
                "32bit": "phantomjs-i686",
                "64bit": "phantomjs-x86_64",
            }
        },
    }

    bin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", BINARY_VERSION)

    os_type = platform.system()
    os_bits = platform.architecture()[0]

    if os_type in os_type_mapping:
        os_info = os_type_mapping[os_type]
        return os.path.join(bin_dir, os_info["dir"], os_info["files"].get(os_bits, os_info["files"]["64bit"]))

    raise EnvironmentError("Unsupported system type: %s" % os_type)


executable_path = _get_executable_path()

