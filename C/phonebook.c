#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

typedef struct Contact {
    char number[20];
    char name[50];
} Contact;

void addContact(Contact *contacts, int *index, const char name[], const char number[]);
void newContact(Contact *contacts, int *index);
void viewAll(Contact *contacts, const int *index);
void deleteContact(Contact *contacts, int *index);

int main(void)
{
    Contact contacts[50];
    int index = 0;

    while (true) {
        printf("<====================>\n");
        printf("Welcome to phonebook.\n");
        printf("Please choose a function:\n");
        printf("<====================>\n");
        printf("1. Add contact\n");
        printf("2. Delete contact\n");
        printf("3. Search contact\n");
        printf("4. View all contacts\n");
        printf("5. Exit\n");
        printf("<====================>\n");

        int choice;
        printf(">> ");
        choice = getchar();
        while (getchar() != '\n'); // Clear the input buffer

        switch (choice) {
            case '1':
                newContact(contacts, &index);
                break;
            case '2':
                deleteContact(contacts, &index);
                break; // Add this break statement
            case '4':
                viewAll(contacts, &index);
                break;
            case '5':
                return 0;
            default:
                printf("Invalid choice.\n");
                break;
        }
    }
}

void addContact(Contact *contacts, int *index, const char name[], const char number[])
{
    if (*index < 50) {
        strcpy(contacts[*index].name, name);
        strcpy(contacts[*index].number, number);
        (*index)++;
    } else {
        printf("Phonebook is full. Cannot add more contacts.\n");
    }
}

// int searchContact(Contact *contact, int low, int high, char key[])
// {
//     int len = strlen(contact->name);
    
//     if (low > high)
//     {
//         return -1;
//     }

//     int mid = floor((high - low) / 2);

//     if (strcmp(contact[mid].name, key))
//     {
//         return mid;
//     } else if ()
// }

void deleteContact(Contact *contacts, int *index)
{
    int ind;
    printf("Enter the index of the contact to delete (1 to %d): ", *index);
    scanf("%d", &ind);
    while (getchar() != '\n'); // Clear the input buffer

    if (ind < 1 || ind > *index) {
        printf("Invalid index.\n");
        return;
    }

    // Clear the contact at the specified index
    for (int i = ind - 1; i < *index - 1; i++) {
        contacts[i] = contacts[i + 1];
    }
    
    (*index)--; // Decrement the index count
    printf("Contact deleted.\n");
}

void newContact(Contact *contacts, int *index)
{
    bool running = true;
    char name[50];
    char number[20];

    while (running)
    {
        printf("Input a name: ");
        fgets(name, 50, stdin);
        name[strcspn(name, "\n")] = '\0';

        printf("Input a number: ");
        fgets(number, 20, stdin);
        number[strcspn(number, "\n")] = '\0';

        addContact(contacts, index, name, number);
        
        printf("Test: %s\n", contacts[*index - 1].name);

        printf("Before Index: %d\n", (*index));
        printf("After Index: %d\n", (*index));

        char cont;
        printf("Do you want to add another contact? (y/n): ");
        cont = getchar();
        while (getchar() != '\n'); // Clear the input buffer
        if (cont != 'y' && cont != 'Y') {
            running = false;
        }
    }
}

void viewAll(Contact *contacts, const int *index)
{
    printf("Index: %d\n", *index);
    printf("Viewing contacts\n");
    for (int i = 0; i < *index; i++) // Fix loop condition
    {
        printf("<====================>\n");
        printf("Index: %d\n", i);
        printf("Name: %s\n", contacts[i].name);
        printf("Number: %s\n", contacts[i].number);
        printf("<====================>\n");
    }
}
