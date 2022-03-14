#!/usr/bin/env python3
f = open("/proc/cpuinfo", "r")
r = f.readlines()
print(f"\033[32m# General Information\033[0m\n\n\033[97mModel Name: {r[4][13:].replace('     ', '')}Model: {r[3][9:]}CPU Arch: {r[19].find('lm') != -1 and 'x64' or 'x86'}\nCPU Cores: {r[12][12:]}Vendor ID: {r[1][12:]}CPU Family: {r[2][13:]}Stepping: {r[5][11:]}Microcode: {r[6][12:]}CPU MHz: {r[7][11:]}Cache Size: {r[8][13:]}Siblings: {r[9][14:]}FPU Support: {r[15][7:]}FPU Exception: {r[16][16:]}CPUID Level: {r[17][14:]}Have WP: {r[18][6:]}\033[0m\n\033[32m# Other Information\n\n\033[0m\033[97mFlags: {r[19][9:]}VMX Flags: {r[20][13:]}\033[0m\033[1;31mBugs: {r[21][8:]}\033[0m\033[97mAddress Sizes: {r[25][16:]}\033[0m", end = "")

