import os
import platform


def _get_executable_path():
    bin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")

    os_type = platform.system()

    if os_type == 'Windows':
        bin_filename = "phantomjs.exe"
    else:
        bin_filename = "phantomjs"

    return os.path.join(bin_dir, bin_filename)


executable_path = _get_executable_path()

