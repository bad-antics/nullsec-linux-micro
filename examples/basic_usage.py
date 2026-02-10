from nullsec_linux_micro.core import BootSectorBuilder,InitSystem
b=BootSectorBuilder()
print(f"MBR: {b.build_mbr()}")
i=InitSystem()
print(f"\nBoot sequence:")
for name,svc in i.boot_sequence(): print(f"  [{svc['priority']}] {name}: {svc['description']}")
print(f"\nInit script:\n{i.generate_init_script()}")
