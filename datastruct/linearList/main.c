#include "sequenceList.h"
int main(){
    SeqList *l = (SeqList *) malloc(sizeof(SeqList));
    printf("%d\n",ListInsert(l,1,1));
    printf("%d\n",ListInsert(l,2,1));
    printf("%d\n",LocateElement(l,1));
    return 0;
}