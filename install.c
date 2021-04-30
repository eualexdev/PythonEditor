// Install in C
#include <stdio.h>
#include <sys/types.h>

#if defined(_WIN32) || defined(_WIN64) || defined(__CYGWIN__)
    #define PLATFORM "WINDOWS"
    #include "windows_os.h"
#elif defined(__linux__)
    #define PLATFORM "LINUX"
    #include "linux_os.h"

#elif defined(__unix__) || !defined(__APPLE__) && defined(__MACH__)
    #define PLATFORM "MAC"
    #include "mac_os.h"
#else
    #define PLATFORM ""
#endif    

const char *GetPlatform() {
    if (PLATFORM == ""){
        return "";
    } else {
        return PLATFORM;
    }
} 

int main(){
    const char *value = GetPlatform();
    int valueINT;
    if (value != ""){
        valueINT = ExecuteOS();
        if (valueINT == 1){
            printf("Instaled");
        } else if (valueINT == 2){
            printf("has instaled");
        } else {
            printf("not instaled");
        }
    } else {
        printf("not instaled");
    }
}