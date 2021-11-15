#include "lists.h"

/**
 * check_cycle - check a singly linked list has a cycle in it
 *
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *current_current = list;
	while (current && current_current  && current_current->next)
	{
		current = current->next;
		current_current  = current_current->next->next;
		if (current == current_current)
		{
			return (1);
		}
	}
	return (0);
}
