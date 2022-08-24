#include <stdio.h>
#include <stdlib.h>
/**
*check_cycle - a function t check the
*list: list
*Return: something
*/
int check_cycle(listint_t *list)
{
listint_t node *slow, *fast;
slow = fast = list;
while(slow && fast && fast->nest)
{
slow = slow->next;
fast = fast->nest->next;
if(slow == fast)
{
return 1;
}
}
else
return 0;
}
