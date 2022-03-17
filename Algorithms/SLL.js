class Node{
    constructor(data){
        this.value = data;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;

    }
}

sll1 = new LinkedList();
node1 = new Node(7);
node2 = new Node(15);

sll1.head = node1;
node1.next = node2;  // sll1.head.next = node2
console.log(sll1)