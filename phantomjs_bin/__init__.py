import os
import platform


def _get_executable_path():
    os_type_mapping = {
        "Windows": {
            "dir": "windows",
        },
        "Darwin": {
            "dir": "macosx",
        },
        "Linux": {
            "dir": "linux",
        },
    }

    os_type = platform.system()

    if os_type not in os_type_mapping:
        raise EnvironmentError("Unsupported system type: %s" % os_type)

    os_info = os_type_mapping[os_type]

    if os_type == 'Windows':
        bin_filename = "phantomjs.exe"
    else:
        bin_filename = "phantomjs"

    setup_path = os.path.dirname(os.path.abspath(__file__))
    bin_path = os.path.join(setup_path, 'bin', os_info["dir"], bin_filename)

    return bin_path


executable_path = _get_executable_path()

