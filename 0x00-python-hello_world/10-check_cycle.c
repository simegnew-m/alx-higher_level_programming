#include "lists.h"

/**
 * check_cycle - check a singly linked list has a cycle in it
 *
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *new = list, *new_new = list;
	while (new && new_new  && new_new->next)
	{
		new = new->next;
		new_new  = new_new->next->next;
		if (new == new_new)
		{
			return (1);
		}
	}
	return (0);
}
