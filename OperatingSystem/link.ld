ENTRY(loader)

SECTIONS {
    . = 0x100000;
    /*将该节的起始位置对齐到 4KB的整数倍*/
    .text ALIGN (0x1000):{   
        *(.text)
    }
    .data ALIGN (0x1000):{
       *(.data) 
    }
     .rodata ALIGN (0x1000) : /* align at 4 KB */
    {
        *(.rodata*)          /* all read-only data sections from all files */
    }
    .bss ALIGN (0x1000) :    /* align at 4 KB */
    {
        *(COMMON)            /* all COMMON sections from all files */
        *(.bss)              /* all bss sections from all files */
    }
}