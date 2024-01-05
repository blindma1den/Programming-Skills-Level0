/* 3. Create an university enrollment system with the following characteristics:
* 	The system has a login with a username and password.
* 	Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 	The user must input their first name, last name, and chosen program.
* 	Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 	If login information is incorrect three times, the system should be locked.
* 	The user must choose a campus from three cities: London, Manchester, Liverpool.
* 	In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 	If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct user{
    char username[256];
    char password[256];
}user;

typedef struct courses{
    int slots_amount;
    char * students_name[256];
    char * students_last_name[256];
}courses;

typedef struct campus{
    struct courses slots[4];
}campus;

int main(){
    char * ptruser;
    char * ptrpassw;
    char * name;
    char * last_name;
    int user_counter=0;
    user users[256];
    int log_in_counter = 0;
    int counter;
    int menu1 = 1;
    int menu2;
    int menu3;
    int menu4;
    int option1;
    int course_option;
    int campus_option;
    int flag_slot_avialable;
    int flag_log_in;
    int slots_counter = 0;
    int amount_occupied_slots= 0;
    campus campus_slots[3];
    //Initializing the amount of slots in each campus
    int k;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 4; j++){
            if(i == 1){
                k=3;
            }else{
                k=1;
            }
            campus_slots[i].slots[j].slots_amount=k;
        }
    }


    while(menu1==1){
        printf("University Enrollment System\n1-Create an Account\n2-Log in\n3-Exit\n");
        scanf("%i",&option1);
        switch (option1){
            //Creating an account
            case 1:
                ptruser = malloc(sizeof(char));
                ptrpassw = malloc(sizeof(char));
                printf("Enter your new credentials\nNew Username (no blank spaces):");
                scanf("%s",ptruser);
                printf("\nNew Password (no black spaces):");
                scanf("%s",ptrpassw);
                strcpy(users[user_counter].username,ptruser);
                strcpy(users[user_counter].password,ptrpassw);
                user_counter++;
                printf("Account created Successfuly\n\n");
                free(ptruser);
                free(ptrpassw);
                ptruser = NULL;
                ptrpassw = NULL;
                break;
            //Log In
            case 2:
                menu2 = 1;
                //Checking the credentials
                while(menu2 == 1){
                    ptruser = malloc(sizeof(char));
                    ptrpassw = malloc(sizeof(char));
                    printf("Enter your Credentials\nUsername:");
                    scanf("%s",ptruser);
                    printf("Enter your password:");
                    scanf("%s",ptrpassw);
                    flag_log_in = 0;
                    counter = 0;
                    while(counter < user_counter && menu2 == 1){
                        if(0 == strcmp(ptruser,users[counter].username) && 0 == strcmp(ptrpassw,users[counter].password)){
                            //Valid Credentials
                            menu3 = 1;
                            flag_slot_avialable = 0;
                            flag_log_in = 1;
                            slots_counter = 0;
                            while(menu3==1){
                                //Choosing a course
                                printf("Avaible Programs\n1-Computer Science\n2-Medicine\n3-Marketing\n4-Arts\n");
                                scanf("%i",&course_option);
                                for(int i = 0; i < 3;i++){
                                    //Checking available slots
                                    if(campus_slots[i].slots[course_option-1].slots_amount>0){
                                        flag_slot_avialable = 1;
                                        break;
                                    }
                                    if(flag_slot_avialable==1){
                                        break;
                                    }
                                }
                                //Is a slot avialable in the choosen course
                                if(flag_slot_avialable==1){
                                    menu4 = 1;
                                    name = malloc(sizeof(char));
                                    last_name = malloc(sizeof(char));
                                    //Asking the name and last name
                                    printf("There are slots available in the program.\n Please write your name:");
                                    scanf("%s",name);
                                    printf("Now please write your Last Name:");
                                    scanf("%s",last_name);
                                    //Choosing a campus
                                    while(menu4 == 1){
                                        printf("\nNow you need to choose a campus\n1-London\n2-Manchester\n3-Liverpool\n");
                                        scanf("%i",&campus_option);
                                        //Checking if the choosen campus have an avialable slot
                                        if(campus_slots[campus_option-1].slots[course_option-1].slots_amount > 0){
                                            //Saving the data
                                            printf("Congratulations, your enrollment have been succesful\n\n");
                                            campus_slots[campus_option-1].slots[course_option-1].students_name[slots_counter] = name;
                                            campus_slots[campus_option-1].slots[course_option-1].students_last_name[slots_counter]= last_name;
                                            menu3 = 0;
                                            menu2 = 0;
                                            slots_counter++;
                                            campus_slots[campus_option-1].slots[course_option-1].slots_amount --;
                                            break;
                                        }else{
                                            printf("There are not avialable slots in this campus, try another one\n\n");
                                        }
                                    }
                                    free(name);
                                    free(last_name);
                                    name = NULL;
                                    last_name = NULL;
                                }
                            }
                            if(flag_slot_avialable == 0){
                                printf("This course is unavailable, choose another \n\n");
                            }
                        }
                        counter++;
                    }
                    if(flag_log_in == 0){
                        printf("\nWrong Credentials\n\n");
                        log_in_counter++;
                        if(log_in_counter == 3){
                            printf("Too many attempts");
                            menu1= 0 ;
                            break;
                        }
                    }
                    free(ptruser);
                    free(ptrpassw);
                    ptruser = NULL;
                    ptrpassw = NULL;
                }

                break;
            case 3:
                menu1 = 0;
                break;
            default:
                menu1 = 0;
                break;
        }
    }

    return 0 ;
}
