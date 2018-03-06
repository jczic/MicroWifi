
from microWifi import MicroWifi
from machine   import Timer
from time      import sleep

# ============================================================================
# ===( Functions )============================================================
# ============================================================================

def _timerProcess(timer) :
	print('-----------------------------')
	print('Access point opened   : %s' % wifi.IsAccessPointOpened())
	print('Connected to AP       : %s' % wifi.IsConnectedToAP())
	print('Internet access       : %s' % wifi.InternetAccessIsPresent())
	print('google.com IP address : %s' % wifi.ResolveIPFromHostname('google.com'))
	print('-----------------------------')

# ============================================================================
# ===( Main )=================================================================
# ============================================================================

print()
print("=======================================================================")
print()

print() # ----------------------------------------------

wifi = MicroWifi()

Timer.Alarm(_timerProcess, 3, periodic=True)

if not wifi.OpenAccessPointFromConf() :
	wifi.OpenAccessPoint('.-= AP TEST =-.', None, '192.168.0.254')

if not wifi.ConnectToAPFromConf() :
	wifi.ConnectToAP('JCzic', 'azerty123')

print()
print("=======================================================================")
print()

# ============================================================================
# ============================================================================
# ============================================================================


