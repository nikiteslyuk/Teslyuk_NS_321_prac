import sys

sys.stdout.write(
    sys.stdin.read()
    .encode("LATIN1", errors="replace")
    .decode("CP1251", errors="replace")
)
