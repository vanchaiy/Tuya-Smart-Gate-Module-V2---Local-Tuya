import tinytuya

DEVICE_ID = "your_device_id"
DEVICE_IP = "192.168.1.xx"
LOCAL_KEY = "your_local_key"

d = tinytuya.Device(DEVICE_ID, DEVICE_IP, LOCAL_KEY)
d.set_version(3.5)              # อุปกรณ์นี้เป็น 3.5
d.set_socketPersistent(True)

print("status:", d.status())   # อ่านสถานะ (DP 101-103 จะไม่โผล่ เพราะ Send-Only)
print("open:",   d.set_value(101, True))   # สั่งเปิด
# print("close:", d.set_value(102, True))  # สั่งปิด
# print("stop:",  d.set_value(103, True))  # สั่งหยุด