#define FB_GREEN     2
#define FB_DARK_GREY 8
char *fb = (char *) 0x000B80000;

int sum_of_three(int a,int b,int c){
    return a + b + c;
}

void pchar(unsigned int i,unsigned char c,unsigned char fg,unsigned char bg){
    fb[i] = c;
    fb[i+1] = ((fg & 0x0F) << 4) | (bg & 0x0F);
}
void fb_write_cell(unsigned int i, char c, unsigned char fg, unsigned char bg)
    {
        fb[i] = c;
        fb[i + 1] = ((fg & 0x0F) << 4) | (bg & 0x0F);
    }


