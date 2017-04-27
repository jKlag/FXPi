-server.py receives a command (via TCP connection) to either turn on or turn off effects
-client.py sends a command to server to either turn on or turn off effects
-patch.pd is a Pure Data guitar effects patch that can receive a command via python script to turn effects on/off

Instructions for use:
  -Connect UCA222 to Pi via USB
  -Plug guitar into input jack and amp into output jack of UCA222
  -Plug in Pi to a power source
  -Wait about a minute to give the Pi time to boot up
  -Open client program with the terminal/CL command 'python client.py'
  -Enter commands of the form <effect> <on/off>
  -Type 'exit' to quit client program
