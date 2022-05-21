#include <stdio.h>
#include <stdlib.h>
#include "disk.h"
#include "fs.h"
#include <string.h>

void FileSysInit() {
	// FileSys info, inode bytemap, block bytemap, inode list를 0으로 채워서 초기화
	// 블록 크기의 메모리를 할당 받은 후 0으로 채우고 디스크로 저장하면 끝
	// 1) Block 크기의 메모리 할당하고 0으로 채운다
	// 2) DevWriteBlock 함수를 통해 메모리를 Block 0부터 6까지 저장한다
	DevCreateDisk();
	DevOpenDisk();

	char* pBuf = (char*)malloc(BLOCK_SIZE);

	// DevWriteBlock 함수를 통해 메모리를 Block 0부터 6까지 저장
	for (int i = 0;i < 7;i++) {
		DevWriteBlock(i, pBuf);
	}
	// 동적할당 메모리 해제
	free(pBuf);
}

void SetInodeBytemap(int inodeno)
{
	// Inode bytemap에서 byte inodeNum을 1로 설정하고 다시 디스크로 저장
	// Inode bytemap은 block 1에 저장됨
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) Block 1을 DevReadBlock 함수를 통해 메모리로 읽는다.
	// 3) byte inodeNum을 1로 설정함
	// 4) DevWriteBlock 함수를 통해 Block 1에 저장함
	char *pBuf =(char *)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 2)
    pBuf[inodeno] = (char)1; // 3)
	DevWriteBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 4)
}


void ResetInodeBytemap(int inodeno)
{
	// Inode bytemap에서 byte inodeNum을 0으로 설정하고 다시 디스크로 저장
	// Inode bytemap은 block 1에 저장됨
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) Block 1을 DevReadBlock 함수를 통해 메모리로 읽는다.
	// 3) byte inodeNum을 0으로 설정함
	// 4) DevWriteBlock 함수를 통해 Block 1에 저장함

	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 2)
    pBuf[inodeno] = (char)0; // 3)
	DevWriteBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 4)
}


void SetBlockBytemap(int blkno)
{
	// Block bytemap에서 byte blkNum을 1로 설정하고 다시 디스크로 저장
	// Block bytemap은 block 2에 저장됨
	// SetInodeBytemap 함수와 block 번호만 다르고 동작 동일

	char* pBuf = (char*)malloc(BLOCK_SIZE); 

	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
    pBuf[blkno] = (char)1;
	DevWriteBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
    free(pBuf);
}


void ResetBlockBytemap(int blkno)
{
	// Block bytemap에서 byte blkNum을 0로 설정하고 다시 디스크로 저장
	// Block bytemap은 block 2에 저장됨
	// ResetInodeBytemap 함수와 block 번호만 다르고 동작 동일

	char* pBuf = (char*)malloc(BLOCK_SIZE);

	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);

    pBuf[blkno] = (char) 0;
	DevWriteBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
}


void PutInode(int inodeno, Inode* pInode)
{
	// pInode에 지정하는 메모리 공간에 저장된 Inode inodeNum의 내용을 디스크에 저장한다.
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) inodeNum이 저장된 block 번호를 구한다
	// 3) block을 DevReadBlock 함수를 통해 메모리로 읽는다
	// 4) pInode의 내용을 Inode inodeNum에 복사한다.
	// 5) DevWriteBlock 함수를 통해 block에 저장한다.
	
	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	int blkno = INODELIST_BLOCK_FIRST + inodeno / (BLOCK_SIZE / sizeof(Inode)); // 2)
	
	DevReadBlock(blkno, pBuf); // 3)

	// 4)
	memcpy(pBuf + (inodeno % (BLOCK_SIZE / sizeof(Inode))) * sizeof(Inode), pInode, sizeof(Inode));
	
	// 5)
	DevWriteBlock(blkno, pBuf);
	
	free(pBuf);
}


void GetInode(int inodeno, Inode* pInode)
{
	// Inode 0를 디스크에서 읽어서 pInode가 지정하는 메모리 공간으로 저장함
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) inodeNum이 저장된 block 번호를 구한다.
	// 3) block을 DevReadBlock 함수를 통해 메모리로 읽는다
	// 4) inodeNum의 내용을 pInode로 복사한다. Inode 배열로 접근할 때 Inode type 변환해서 접근할 수 있다.
	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)
	int blkno = INODELIST_BLOCK_FIRST + (inodeno / (BLOCK_SIZE / sizeof(Inode))); // 2)

	// 3)
	DevReadBlock(blkno, pBuf);

	// 4)
	memcpy(pInode, pBuf + (inodeno % (BLOCK_SIZE / sizeof(Inode))) * sizeof(Inode), sizeof(Inode));

	free(pBuf);
}


int GetFreeInodeNum(void)
{
	// 할당되지 않은 inode 번호를 획득한다.
	// Inode bytemap (block1)에서 first fit searching 방법 사용함
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) block 1을 DevReadBlock 함수를 통해 메모리로 읽는다.
	// 3) 시작 위치부터 0을 가지는 byte를 찾는다. 이 방법이 First fit searching이다.
	// 4) 찾은 index를 return 한다.

	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 2)
	// 3)
	for (int i = 0; i < BLOCK_SIZE; i++) {
        if (pBuf[i] == (char)0)
            //printf("Inode pBuf[i] = %d, i=%d\n", pBuf[i],i);
            //index=i;
            return i;

	}

	free(pBuf);
	return -1;
}


int GetFreeBlockNum(void)
{
	// 할당되지 않은 block 번호를 획득한다.
	// Inode bytemap (block 2)에서 first fit searching 방법 사용함
	// 1) malloc으로 block 크기의 메모리 할당
	// 2) block 2를 DevReadBlock 함수를 통해 메모리로 읽는다.
	// 3) 시작 위치부터 0을 가지는 byte를 찾는다. 이 방법이 First fit searching이다.
	// 4) 찾은 index를 return 한다.

	char* pBuf = (char*)malloc(BLOCK_SIZE);
	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);

	// FileSysInit() 함수에서 block 6까지 메모리 할당을 함으로 7번부터 시작
	for (int i = 7; i < BLOCK_SIZE/sizeof(int)*sizeof(int); i++) {
        if (pBuf[i] == (char) 0)
            //printf("Block pBuf[i] = %d, i=%d\n", pBuf[i],i);
            return i;

	}

	free(pBuf);
	return -1;
}

void PutIndirectBlockEntry(int blkno, int index, int number)
{
	// blkno로 지정된 indirect block의 특정 위치(index)에 값(number)을 저장함
	// entry의 크기는 4bytes 이며, block 당 entry 개수는 block size / 4
	// ex) PutIndirectBlockEntry(100,2,300);

	char* pBuf = (char*)malloc(BLOCK_SIZE);

    int * value=&number;
	DevReadBlock(blkno, pBuf);

    memcpy(pBuf + (index % (BLOCK_SIZE / sizeof(int))) * sizeof(int), value, sizeof(int));

	DevWriteBlock(blkno, pBuf);

	free(pBuf);
}

int GetIndirectBlockEntry(int blkno, int index)
{
	// blkno로 지정된 indirect block의 특정위치(index)에 저장된 값을 반환함
	char* pBuf = (char*)malloc(BLOCK_SIZE);

	DevReadBlock(blkno, pBuf);
    int * value;
    memcpy(value, pBuf + (index % (BLOCK_SIZE / sizeof(int))) * sizeof(int), sizeof(int));

    //DevWriteBlock(blkno, pBuf);

	free(pBuf);
    return *value;
}

void PutDirEntry(int blkno, int index, DirEntry* pEntry)
{
	// blkno로 지정된 block의 특정 위치(index)에 pEntry에 저장된 값을 저장
	// DirEntry의 크기는 32 bytes이며, block 당 entry 개수는 Block size/32.
	// ex) PutDirEntry(200, 2, pEntry):
	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(blkno, pBuf); // 2)
    memcpy(pBuf + (index % (BLOCK_SIZE / sizeof(DirEntry))) * sizeof(DirEntry), pEntry, sizeof(DirEntry));
    DevWriteBlock(blkno, pBuf);
    free(pBuf);
}

int GetDirEntry(int blkno, int index, DirEntry* pEntry)
{
	// blkno로 지정된 block에서 특정 위치(index)의 directory entry를 획득한다.
	// pEntry가 가리키는 메모리 공간으로 획득된 값을 저장함.

	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(blkno, pBuf); // 2)
    memcpy(pEntry, pBuf + (index % (BLOCK_SIZE / sizeof(DirEntry))) * sizeof(DirEntry), sizeof(DirEntry));
    DevWriteBlock(blkno, pBuf);
	free(pBuf);
    if (pEntry->inodeNum == INVALID_ENTRY)
        return -1;
    else
        return 1;
}
void RemoveIndirectBlockEntry(int blkno, int index) {
    PutIndirectBlockEntry(blkno, index, INVALID_ENTRY);
}
void RemoveDirEntry(int blkno, int index) {
    DirEntry* pEntry=(DirEntry*)malloc(sizeof(DirEntry));
    pEntry->inodeNum=INVALID_ENTRY;
    PutDirEntry(blkno, index, pEntry);
    free(pEntry);
}