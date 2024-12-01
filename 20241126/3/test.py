import sys
import struct

try:
    header = sys.stdin.buffer.read(44)
    if len(header) < 44:
        print("NO")
    else:
        try:
            (
                riff,
                file_size,
                wave,
                fmt,
                _,
                audio_format,
                channels,
                rate,
                _,
                _,
                bits,
                data,
                data_size,
            ) = struct.unpack("<4sI4s4sIHHIIHH4sI", header)
        except struct.error:
            print("NO")
        else:
            if riff != b"RIFF" or wave != b"WAVE" or fmt != b"fmt " or data != b"data":
                print("NO")
            else:
                print(
                    f"Size={file_size}, Type={audio_format}, Channels={channels}, Rate={rate}, Bits={bits}, Data size={data_size}"
                )
except Exception:
    print("NO")
