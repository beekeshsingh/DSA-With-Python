Linked Lists
A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.

    * A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.
    * The easiest way to understand linked lists is perhaps by comparing linked lists with arrays.



Types of Linked Lists 
    1. Single Linked Lists
    2. Doubly Linked Lists
    3. Circular Linked Lists

Single Linked Lists: A SLL is the simplest kind of linked lists. It takes up less space in memory because each node has only one address to next node,
    ----------     ----------
    |- data -|  -> |- data -|
    ---------- -   ----------
    |- next -|-    |- next -|
    ----------     ----------

Doubly Linked Lists: A DLL has nodes with addresses to both the previous and the next node, like in the images below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.
    ----------         ----------
    |- prev -|<------- |- prev -|
    ----------      -> ----------
    |- data -|    -    |- data -|
    ----------  -      ----------
    |- next -|-        |- next -|
    ----------         ----------

Circular Linked Lists: A CLL is like a Single or doubly linked list with the first node, the "head", and the last node, the "tail", connected.
