OBJECTS = loader.o kmain.o
CC = gcc
CFLAGS = -m32 -nostdlib -nostdinc -fno-builtin -fno-stack-protector \
         -nostartfiles -nodefaultlibs -c
LDFLAGS = -T link.ld -melf_i386
AS = nasm.exe
ASFLAGS = -felf32
QEMU = /mnt/d/qemu/qemu-system-x86_64.exe
ISO = /mnt/d/workspace/OperatingSystem/os.iso
QEMUFLAGS = -drive file=$(ISO),media=cdrom,if=ide,format=raw \
            -bios /mnt/qemu/share/bios.bin  \
            -boot d \
            -display sdl \
            -m 32

all: kernel.elf
os.iso: kernel.elf
	cp kernel.elf iso/boot/kernel.elf
	genisoimage -R \
                    -b boot/grub/stage2_eltorito \
                    -no-emul-boot \
                    -boot-load-size 4 \
                    -A os \
                    -input-charset utf8 \
                    -quiet \
                    -boot-info-table \
                    -o os.iso \
                    iso
kernel.elf: $(OBJECTS)
	ld $(LDFLAGS) $(OBJECTS) -o kernel.elf



run: os.iso
	$(QEMU) $(QEMUFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) $< -o $@

%.o: %.s
	$(AS) $(ASFLAGS) $< -o $@

clean:
	rm -rf *.o os.iso kernel.elf
