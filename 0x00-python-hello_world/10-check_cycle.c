#include "lists.h"

/**
 * check_cycle - checks if a singly linked list is has a cycle
 * @list: singly linked list
 * Return: 1 if there is a cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *current;

	head = list;
	current = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (current != NULL)
	{
		if (current == head)
			return (1);
		current = current->next;
	}
	return (0);
}
