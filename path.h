#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>


int CreatePath(const char *value){
    struct stat st = {0};
	
	if (stat(value, &st) == -1) {
		if(mkdir(value) == 0){
            return true;
		} else {
            return 1;
        }
    } else {
        return 2;
    }
}