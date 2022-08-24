#include "lists.h"
/**
*check_cycle - a function t check the
*@list: list
*Return: something
*/
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;
slow = fast = list;
while (slow != NULL && fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
