"""Linux Microkernel Tools"""
import struct,json,os

class BootSectorBuilder:
    """Minimal x86 boot sector builder"""
    def build_mbr(self,bootloader_msg="NullSec MicroLinux"):
        """Build a minimal MBR boot sector structure"""
        sector=bytearray(512)
        # JMP short to code
        sector[0]=0xEB; sector[1]=0x3C
        # Boot message placeholder
        msg_bytes=bootloader_msg.encode()[:32]
        for i,b in enumerate(msg_bytes): sector[0x3E+i]=b
        # Boot signature
        sector[510]=0x55; sector[511]=0xAA
        return {"size":512,"signature":"0x55AA","message":bootloader_msg,
                "valid":sector[510]==0x55 and sector[511]==0xAA}
    
    def analyze_partition_table(self,mbr_bytes=None):
        """Parse MBR partition table entries"""
        if mbr_bytes is None: return {"partitions":[],"note":"No MBR data provided"}
        entries=[]
        for i in range(4):
            offset=446+i*16
            if offset+16<=len(mbr_bytes):
                status=mbr_bytes[offset]
                ptype=mbr_bytes[offset+4]
                if ptype!=0:
                    entries.append({"partition":i+1,"status":"active" if status==0x80 else "inactive",
                                   "type":hex(ptype)})
        return {"partitions":entries,"count":len(entries)}

class InitSystem:
    SERVICES={"networking":{"priority":10,"type":"oneshot","description":"Configure network interfaces"},
              "syslog":{"priority":20,"type":"daemon","description":"System logging daemon"},
              "sshd":{"priority":30,"type":"daemon","description":"SSH server"},
              "cron":{"priority":40,"type":"daemon","description":"Task scheduler"}}
    
    def boot_sequence(self):
        return sorted(self.SERVICES.items(),key=lambda x:x[1]["priority"])
    
    def generate_init_script(self):
        lines=["#!/bin/sh","# NullSec MicroLinux init","","mount -t proc none /proc",
               "mount -t sysfs none /sys","mount -t devtmpfs none /dev","",
               "echo 'NullSec MicroLinux booted'","","exec /bin/sh"]
        return "\n".join(lines)
