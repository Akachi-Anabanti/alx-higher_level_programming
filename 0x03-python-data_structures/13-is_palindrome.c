#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * Description: A palindrome is a phenomenon where the
 * reverse of a sequence is the same as the original sequence.
 * @head: The linked list to check
 * Return: 0 if it's not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *nextnode;

	if (head == NULL || *head == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		nextnode = slow->next;
		slow->next = prev;
		prev = slow;
		slow = nextnode;
	}
	if (fast != NULL)
		slow = slow->next;
	while (prev != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
