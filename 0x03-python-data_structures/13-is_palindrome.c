#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* Empty list or single element list is considered palindrome */

	/* Find the middle of the linked list and reverse the first half */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/* Reverse the first half of the linked list */
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	/*
	 * If the list has odd number of elements,
	 * move the slow pointer one step ahead
	 */
	if (fast != NULL)
		slow = slow->next;

	/* Compare the reversed first half with the second half */
	while (slow != NULL)
	{
		if (slow->n != prev->n)
		{
			return (0); /* Not a palindrome */
		}
		slow = slow->next;
		prev = prev->next;
	}

	return (1); /* Palindrome */
}
