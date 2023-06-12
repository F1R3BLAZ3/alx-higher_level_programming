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

/* Additional utility functions for testing */

/**
 * print_listint - Prints a linked list of integers.
 * @h: Pointer to the head of the linked list.
 *
 * Return: The number of nodes in the linked list.
 */
size_t print_listint(const listint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d", h->n);
		if (h->next != NULL)
			printf(" -> ");
		h = h->next;
		count++;
	}
	printf("\n");
	return (count);
}

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: Double pointer to the head of the linked list.
 * @n: The integer to be added to the new node.
 *
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new_node, *last_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		last_node = *head;
		while (last_node->next != NULL)
			last_node = last_node->next;
		last_node->next = new_node;
	}

	return (new_node);
}

/**
 * free_listint - Frees a linked list.
 * @head: Pointer to the head of the linked list.
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
