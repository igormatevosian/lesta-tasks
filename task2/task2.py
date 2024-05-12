from typing import TypeVar, Generic

T = TypeVar('T')


class CircularBuffer(Generic[T]):
    """Circular FIFO buffer"""

    def __init__(self, capacity: int) -> None:
        """Initialize the circular buffer.

        Args:
            capacity (int): Capacity of the buffer.
        """
        self.data: list[T | None] = [None] * capacity
        self.head = 0
        self.tail = 0
        self.empty = True

    def __len__(self) -> int:
        """Return capacity of buffer."""
        return len(self.data)

    def put(self, item: T) -> None:
        """Add an element to the buffer.

        If the buffer overflows, the oldest element will be replaced.

        Args:
            item (T): The item to add to the buffer.
        """
        if not self.empty:
            self.tail = (self.tail + 1) % len(self.data)
            if self.tail == self.head:
                self.head = (self.head + 1) % len(self.data)
        else:
            self.empty = False
            self.head = self.tail
        self.data[self.tail] = item

    def get(self) -> T | None:
        """Retrieve an element from the buffer.

        Returns:
            T | None: The element retrieved from the buffer, or None if the buffer is empty.
        """
        if self.empty:
            return None

        if self.head == self.tail:
            self.empty = True

        item = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)

        return item


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] | None = None
        self.prev: Node[T] | None = None


class CircularBufferUsingLinkedList(Generic[T]):
    """Circular FIFO buffer implemented using a doubly linked list"""

    def __init__(self, capacity: int) -> None:
        """Initialize the circular buffer.

        Args:
            capacity (int): Capacity of the buffer.
        """
        self.capacity = capacity
        self.size = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def __len__(self) -> int:
        """Return capacity of buffer."""
        return self.capacity

    def put(self, item: T) -> None:
        """Add an element to the buffer.

        If the buffer overflows, the oldest element will be replaced.

        Args:
            item (T): The item to add to the buffer.
        """
        new_node = Node(item)

        if self.size < self.capacity:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.head = self.head.next

    def get(self) -> T | None:
        """Retrieve an element from the buffer.

        Returns:
            T | None: The element retrieved from the buffer, or None if the buffer is empty.
        """
        if self.size == 0:
            return None

        item = self.head.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1

        return item
