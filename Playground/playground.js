class Node{
    constructor(val=0, next= null){
        this.val = val
        this.next = next
    }
}

let ll = new Node()
let dummy = ll
for(let i = 0; i < 5; i++){
    dummy.next = new Node(i)
    dummy = dummy.next
}

function printLL(ll){
    while(ll){
        console.log(ll.val)
        ll = ll.next
    }
}

printLL(ll.next)