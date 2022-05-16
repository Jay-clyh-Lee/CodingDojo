class Node {
    constructor(data) {
        this.value = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    addFront(data) {
        var newNode = new Node(data); 
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    removeFront() {
        if (this.head == null) {
            return this.head;
        }
        var removedNode = this.head;
        this.head = removedNode.next;
        removedNode.next = null;
        return this.head;
    }

    front() {
        if (this.head == null) {
            return null;
        } else {
            return this.head.value;
        }
    }

    display() {
        arr = []
        for (int i=0; i<arr.length; i++){
            arr[i] = 
        }
            
    }
}