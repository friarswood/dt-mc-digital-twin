
from datetime import datetime, timedelta
import disruptive as dt

# https://minecraft.fandom.com/wiki/Daylight_cycle
# mc time cycle is [0,24000) -> [6:00, 6:00)

def mc_now():
  now = datetime.now()
  ref = now.replace(hour=6, minute=0, second=0, microsecond=0)
  # 86400 seconds in real day, 1 MC tick is 3.6 seconds (86400/24000)
  ticks = int(((now - ref).total_seconds() % 86400) / 3.6)
  return ticks


def weather(dt_project_id):

  device_id = "emuc3j2ko1m4b6dtmof5pm0"

  sensor = dt.Device.get_device(device_id, dt_project_id)

  p = sensor.reported.temperature.celsius

  # we use the following rule of thumb for reported pressure:
  # 970 to 984  = Stormy
  # 984 to 998   = Rain
  # 998 to 1012 = Change
  # 1012 to 1026 = Fair
  # 1026 to 1040 = Dry

  if p <= 984.0:
    return "thunder"
  if p <= 998.0:
    return "rain"
  return "clear"


