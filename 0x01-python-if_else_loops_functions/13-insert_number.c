#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: The sorted linked list
 * @number: The mumber to be inserted
 * Return: The address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	if (head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->next == NULL || number < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
