
import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def hex_to_float(h):
    return struct.unpack('!f', bytes.fromhex(h))[0]

var0 = 123
var1 = 12
var2 = "1"

hex_var0 = '%#06x' % var0
hex_var1 = '{:#06x}'.format(var0)
hex_var2 = float_to_hex(float(var2))

print("hex_var0 = ", hex_var0[4:6])
print("hex_var1 = ", hex_var1)
print("hex_var2 = ", hex_var2)

input = "3f800000"

print("input[0:2] = %s" % input[0:2])
print("input[2:4] = %s" % input[2:4])
print("input[4:6] = %s" % input[4:6])
print("input[6:8] = %s" % input[6:8])
print("float(input) = ", round(hex_to_float(input), 1))


_hex = 'FF'
_int = int(_hex, 16)
print("_int = ", _int)
_int = _int + 10
print("_int = ", _int)

__hex = 0xFF
_hmask = 0b11110000
_lmask = 0b00001111

print("high bits = ", (int(_hex, 16) & _hmask) >> 4)
print("low bits = ", int(_hex, 16) & _lmask)