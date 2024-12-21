# __init__.py in the commands directory

# Import each module's execute function and assign an alias for clarity
from .ping import execute as ping
from .wiki import execute as wiki
from .info import execute as info
from .help import mehelp_command as help_command
from .copyright import execute as execute_copyright
from .experiment import execute as experiment
from .status import execute as status
from .image import execute as image
