#include "sequenceList.h"
#include <stdio.h>
#include <stdlib.h>
//顺序表，使用连续的存储单元顺序存储数据元素 138
//静态分配
//以位序来定位元素而非下标





//向SeqList中插入元素e，下标为i
//在 1 <= i <= L.lenth+1的位置插入
// 从1开始插入
int ListInsert(SeqList *L,int i,int e){
    if (i < 1 || i > L->lenth){
        return 0;
    }else if (IsFull(L)){
        return 0;
    }
    int j;
    for (j = L->lenth;j >= i;j--) {
        L->data[j] = L->data[j-1];  
    }
    L->data[i-1]= e;
    L->lenth++;
    return 1;
}


//return 0 代表表中没有该元素
int LocateElement(SeqList *L,int e){
    int j;
    for ( j = L->lenth-1; j>=0; j--) {
        if (L->data[j] == e){
            break;
        } 
    }
    return j+1;
}
// 位序  1<= i <= L.lenth+1
// 返回值  
// 返回值为非0 表示成功并 将删除元素存放到给定的指针中，否则删除失败        
int ListDelete(SeqList *L,int i,int *e){
    if (i < 1 || i > L->lenth) {
        return 0;
    }else if(IsEmpty(L)){
        return 0;
    }
    *e = L->data[i-1]; 
    int j;
    for ( j = L->lenth; j>i ;j--){
        L->data[j-1] = L->data[j];  
    }
    L->lenth--;
    return 1;

}
int IsEmpty(SeqList *L){
    return L->lenth==0;
}

//先加在增
int IsFull(SeqList *L){
    return L->lenth >= MAXSIZE;
}



