
#ifndef SEQUENCE_H
#define SEQUENCE_H
#define MAXSIZE 100
typedef struct 
{
    int data[MAXSIZE];
    int lenth;
    /* data */
}SeqList;

int IsFull(SeqList *);
int IsEmpty(SeqList *);
int LocateElement(SeqList *,int);
int ListDelete(SeqList *,int,int *);
int ListInsert(SeqList *,int,int);
#endif
