//SrimatreNamaha
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct TrieNode{
	char ch;
	struct TrieNode *links[26];
	short isWord;
};

struct TrieNode * createNode(char);

struct TrieNode * createNode(char ch)
{
	struct TrieNode *tempNode;
	
	tempNode = malloc(sizeof(struct TrieNode));
	if(tempNode == NULL){
		printf("Error: Node creation failed!");
		exit(0);
	}
	tempNode->ch=ch;
	tempNode->isWord=0;
	for(int i=0; i<26;i++)
		tempNode->links[i]=NULL;
	return(tempNode);
}

void addWord(struct TrieNode * root, char *word)
{
	if(*word == '\0' || root == NULL)
		return;
	//puts(word);
	if(root->links[word[0]-'a'] == NULL){
		root->links[word[0]-'a']=createNode(word[0]);
	}
	root=root->links[word[0]-'a'];
	if(word[1]=='\0'){
		root->isWord++;
		return;
	}
	addWord(root, ++word);
}

void printTree(struct TrieNode * root)
{
	if(root == NULL)
		return;
		
	if(root->ch >= 'a' && root->ch <= 'z')
		printf("%c-%d, ", root->ch, root->isWord);

	for(int i=0;i<26;i++){
		printTree(root->links[i]);
	}
}

char * updatePreFix(char * preFix, char ch)
{
	char * tempStr;
	int iStrLen, i;
	
	iStrLen=strlen(preFix);
	tempStr=malloc(iStrLen+2);
	
	for(i=0;preFix[i] != '\0';i++)
		tempStr[i]=preFix[i];

	tempStr[i++]=ch;
	tempStr[i]='\0';
	return tempStr;
}

void printTreeWords(struct TrieNode * root, char *preFix)
{
	if(root == NULL)
		return;
	
	if(root->ch >= 'a' && root->ch <= 'z')
		preFix=updatePreFix(preFix, root->ch);
		
	if(root->isWord){
		printf("%s\n", preFix);
	}
	for(int i=0;i<26;i++){
		printTreeWords(root->links[i], preFix);
	}
	free(preFix);
}

void main(void)
{
	struct TrieNode * root;
	char *list[8]={"aac","a","ab","abc","abcd","abcde","xyz","pqrs"};
	
	root=createNode('0');
	for(int i=0;i<8;i++){
		addWord(root, list[i]);
	}
	printTreeWords(root, "");
	//printTree(root);
	
	//printf("SriMatreNamaha!");
}
