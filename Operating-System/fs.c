#include <stdio.h>
#include <stdlib.h>
#include "disk.h"
#include "fs.h"
#include <string.h>

void FileSysInit() {
	// FileSys info, inode bytemap, block bytemap, inode list�� 0���� ä���� �ʱ�ȭ
	// ��� ũ���� �޸𸮸� �Ҵ� ���� �� 0���� ä��� ��ũ�� �����ϸ� ��
	// 1) Block ũ���� �޸� �Ҵ��ϰ� 0���� ä���
	// 2) DevWriteBlock �Լ��� ���� �޸𸮸� Block 0���� 6���� �����Ѵ�
	DevCreateDisk();
	DevOpenDisk();

	char* pBuf = (char*)malloc(BLOCK_SIZE);

	// DevWriteBlock �Լ��� ���� �޸𸮸� Block 0���� 6���� ����
	for (int i = 0;i < 7;i++) {
		DevWriteBlock(i, pBuf);
	}
	// �����Ҵ� �޸� ����
	free(pBuf);
}

void SetInodeBytemap(int inodeno)
{
	// Inode bytemap���� byte inodeNum�� 1�� �����ϰ� �ٽ� ��ũ�� ����
	// Inode bytemap�� block 1�� �����
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) Block 1�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�.
	// 3) byte inodeNum�� 1�� ������
	// 4) DevWriteBlock �Լ��� ���� Block 1�� ������
	char *pBuf =(char *)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 2)
    pBuf[inodeno] = (char)1; // 3)
	DevWriteBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 4)
}


void ResetInodeBytemap(int inodeno)
{
	// Inode bytemap���� byte inodeNum�� 0���� �����ϰ� �ٽ� ��ũ�� ����
	// Inode bytemap�� block 1�� �����
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) Block 1�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�.
	// 3) byte inodeNum�� 0���� ������
	// 4) DevWriteBlock �Լ��� ���� Block 1�� ������

	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 2)
    pBuf[inodeno] = (char)0; // 3)
	DevWriteBlock(INODE_BYTEMAP_BLOCK_NUM, pBuf); // 4)
}


void SetBlockBytemap(int blkno)
{
	// Block bytemap���� byte blkNum�� 1�� �����ϰ� �ٽ� ��ũ�� ����
	// Block bytemap�� block 2�� �����
	// SetInodeBytemap �Լ��� block ��ȣ�� �ٸ��� ���� ����

	char* pBuf = (char*)malloc(BLOCK_SIZE); 

	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
    pBuf[blkno] = (char)1;
	DevWriteBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
    free(pBuf);
}


void ResetBlockBytemap(int blkno)
{
	// Block bytemap���� byte blkNum�� 0�� �����ϰ� �ٽ� ��ũ�� ����
	// Block bytemap�� block 2�� �����
	// ResetInodeBytemap �Լ��� block ��ȣ�� �ٸ��� ���� ����

	char* pBuf = (char*)malloc(BLOCK_SIZE);

	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);

    pBuf[blkno] = (char) 0;
	DevWriteBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);
}


void PutInode(int inodeno, Inode* pInode)
{
	// pInode�� �����ϴ� �޸� ������ ����� Inode inodeNum�� ������ ��ũ�� �����Ѵ�.
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) inodeNum�� ����� block ��ȣ�� ���Ѵ�
	// 3) block�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�
	// 4) pInode�� ������ Inode inodeNum�� �����Ѵ�.
	// 5) DevWriteBlock �Լ��� ���� block�� �����Ѵ�.
	
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
	// Inode 0�� ��ũ���� �о pInode�� �����ϴ� �޸� �������� ������
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) inodeNum�� ����� block ��ȣ�� ���Ѵ�.
	// 3) block�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�
	// 4) inodeNum�� ������ pInode�� �����Ѵ�. Inode �迭�� ������ �� Inode type ��ȯ�ؼ� ������ �� �ִ�.
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
	// �Ҵ���� ���� inode ��ȣ�� ȹ���Ѵ�.
	// Inode bytemap (block1)���� first fit searching ��� �����
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) block 1�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�.
	// 3) ���� ��ġ���� 0�� ������ byte�� ã�´�. �� ����� First fit searching�̴�.
	// 4) ã�� index�� return �Ѵ�.

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
	// �Ҵ���� ���� block ��ȣ�� ȹ���Ѵ�.
	// Inode bytemap (block 2)���� first fit searching ��� �����
	// 1) malloc���� block ũ���� �޸� �Ҵ�
	// 2) block 2�� DevReadBlock �Լ��� ���� �޸𸮷� �д´�.
	// 3) ���� ��ġ���� 0�� ������ byte�� ã�´�. �� ����� First fit searching�̴�.
	// 4) ã�� index�� return �Ѵ�.

	char* pBuf = (char*)malloc(BLOCK_SIZE);
	DevReadBlock(BLOCK_BYTEMAP_BLOCK_NUM, pBuf);

	// FileSysInit() �Լ����� block 6���� �޸� �Ҵ��� ������ 7������ ����
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
	// blkno�� ������ indirect block�� Ư�� ��ġ(index)�� ��(number)�� ������
	// entry�� ũ��� 4bytes �̸�, block �� entry ������ block size / 4
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
	// blkno�� ������ indirect block�� Ư����ġ(index)�� ����� ���� ��ȯ��
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
	// blkno�� ������ block�� Ư�� ��ġ(index)�� pEntry�� ����� ���� ����
	// DirEntry�� ũ��� 32 bytes�̸�, block �� entry ������ Block size/32.
	// ex) PutDirEntry(200, 2, pEntry):
	char* pBuf = (char*)malloc(BLOCK_SIZE); // 1)

	DevReadBlock(blkno, pBuf); // 2)
    memcpy(pBuf + (index % (BLOCK_SIZE / sizeof(DirEntry))) * sizeof(DirEntry), pEntry, sizeof(DirEntry));
    DevWriteBlock(blkno, pBuf);
    free(pBuf);
}

int GetDirEntry(int blkno, int index, DirEntry* pEntry)
{
	// blkno�� ������ block���� Ư�� ��ġ(index)�� directory entry�� ȹ���Ѵ�.
	// pEntry�� ����Ű�� �޸� �������� ȹ��� ���� ������.

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