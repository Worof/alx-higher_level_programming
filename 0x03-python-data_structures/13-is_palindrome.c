#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * reverse_listint - Reverses a listint_t list.
 * @head: A pointer to the start of the listint_t list.
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the start of the listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *temp, *rev_head;

	if (!*head || !(*head)->next)
		return (1);

	/* Finding the middle of the list */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reversing the second half of the list */
	rev_head = reverse_listint(&slow);

	/* Comparing the first half and the reversed second half */
	temp = *head;
	while (rev_head)
	{
		if (temp->n != rev_head->n)
			return (0);
		temp = temp->next;
		rev_head = rev_head->next;
	}

	/* Optional: Reverse the second half back to its original form */
	/* reverse_listint(&slow); */

	return (1);
}
