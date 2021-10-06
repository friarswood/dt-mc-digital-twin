import os
from dotenv import load_dotenv
from mcpi.minecraft import Minecraft
from mcpi import block
import disruptive as dt

DOOR_BOTTOM = 0
DOOR_TOP = 8
DOOR_CLOSED = 0
DOOR_OPEN = 4

# /setworldspawn 0 0 0

def main(dt_project_id, mc):

  door_loc = eval(os.getenv("FRONT_DOOR_COORDS", "(0,0,0)"))

  front_door = mc.getBlockWithData(door_loc)
  # check its a door
  if front_door.id != block.DOOR_WOOD.id:
    raise RuntimeError(f"Door not found at location {door_loc}")

  # Initialize a stream generator for all temperature events in a project.
  for e in dt.Stream.event_stream(dt_project_id, event_types=[dt.events.TOUCH, dt.events.OBJECT_PRESENT]):
    if e.event_type == dt.events.TOUCH:
      print(f'touch from {e.device_id} at {e.data.timestamp}')
      # TODO ring bell or note block
    elif e.event_type == dt.events.OBJECT_PRESENT:
      print(f'{e.data.state} from {e.device_id} at {e.data.timestamp}')
      if e.device_id == "bchopvl7rihkdo9k5img":
        front_door.data = DOOR_OPEN if e.data.state == "NOT_PRESENT" else DOOR_CLOSED
        mc.setBlock(door_loc, front_door)


if __name__ == "__main__":

  load_dotenv()

  # Connection to MC server
  mc_server = os.getenv("MC_SERVER")
  mc_port = int(os.getenv("MC_PORT"))
  mc = Minecraft.create(address=mc_server, port=mc_port)
  print(mc)

  # Connection to DT cloud
  dt_project = os.getenv("DT_PROJECT")
  dt_svc_key = os.getenv("DT_SVC_KEY")
  dt_svc_secret = os.getenv("DT_SVC_SECRET")
  dt_svc_email = os.getenv("DT_SVC_EMAIL")
  dt.log_level = 'debug'
  dt.default_auth = dt.Auth.service_account(dt_svc_key, dt_svc_secret, dt_svc_email)

  try:
    main(dt_project, mc)
  except Exception as e:
    print(e)



