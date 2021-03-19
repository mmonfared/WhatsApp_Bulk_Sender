from Keywords import Keywords
from Variables.configs import *

# Send Bulk Message using search
keys = Keywords()
keys.open_whatsapp()
keys.send_bulk_message(message=bulk_message)
keys.teardown()
