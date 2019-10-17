import java.util.Iterator;

public class DLinkedList<T> implements ILinkedList, Iterable<T>
{
    private LNode first_node;
    private LNode last_node;
    private int node_count = 0;
    
    public DLinkedList()
    {
        this.first_node = null;
        this.last_node = null;
    }

    public void add(int index, Object o) {
        LNode new_node = new LNode(o);       
        LNode selected = getNode(index);
        if (selected==null) { return; }
        LNode prev = selected.previous;
        prev.next = new_node;
        selected.previous = new_node;
        new_node.next = selected;
        new_node.previous = prev;
        node_count++;
    }
    
    public void addFirst(Object o) {
        LNode new_node = new LNode(o);
        if (node_count==0) {
            this.first_node = last_node = new_node;  
        } else {
            this.first_node.previous = new_node;
            new_node.previous = this.last_node;
            new_node.next = this.first_node;
            this.first_node = new_node;             
        }
        node_count++;
    }
    
    public void addLast(Object o) {
        LNode new_node = new LNode(o);
        if (node_count==0) {
            this.first_node = new_node;
            this.last_node = new_node;
            new_node.next = new_node;
            new_node.previous = new_node; 
        } else {
            this.last_node.next = new_node;
            new_node.next = this.first_node;
            new_node.previous = this.last_node;
            this.last_node = new_node;
            this.first_node.previous = new_node;
        }
        node_count++;
    }
    
    public void delete(int index) { 
        LNode selected = getNode(index);
        if (!(selected==null)) {
            LNode prev_node = selected.previous;
            LNode next_node = selected.next;
            prev_node.next = next_node;
            next_node.previous = prev_node;
            if (index==0) {
                this.first_node = next_node;
            } else if (index==(node_count-1)) {
                this.last_node = prev_node;
            }
            node_count-=1;
        }
    }
    
    public void deleteFirst() {
        delete(0);
    }
    
    public void deleteLast() {
        delete(node_count-1);
    }
    
    public int size() {
        return node_count;
    }
    
    public String toString() {
        return "LinkedList (" + this.size() + " items)";
    }
            
    public void clear() {
        this.first_node = null;
        this.last_node = null;
        node_count=0;
    }
    
    public boolean contains(Object o) {
        if (this.size()==0) { return false; }
        for (int i = 0; i<node_count; i++) {
         if (getNode(i).getData()==o) { return true; }
        }
        return false;
    }
    
    public Object get(int index) {
        LNode selected_node = getNode(index);
        if (selected_node==null) { return null; }
        return selected_node.data;
    }
    
    public Object getFirst() {
        return this.first_node.data;
    }
    
    public Object getLast() {
        return this.last_node.data;
    }
    
    private LNode getNode(int index) {
        if (!((index>=0) && (index<node_count))) { return null; } //BOUNDS ERROR}
        LNode selected_node = this.first_node;
        for (int i = 0; i<index; i++) {
            selected_node = selected_node.next;
        }
        return selected_node;
    }
        
    public Iterator<T> iterator() {
        return new DListIterator<T>(this);
    }
    
    private class DListIterator<T> implements Iterator<T> {
        private int index = 0;  // the current element we are looking at
        private DLinkedList list;

        public DListIterator(DLinkedList o) {
            this.list = o;
        }
              
        public boolean hasNext() {
            if (this.index<this.list.node_count) {
                return true;
            } else {
                return false;
            }
        }
    
        public T next() {
            LNode<T> selected_node = this.list.getNode(index++);
            return selected_node.getData();
        }
    
        public void remove() {
            throw new UnsupportedOperationException(); //Not supported
        }
    }
    
    //LinkedNode class
    private static class LNode<T> {
        private LNode<T> next;
        private LNode<T> previous;
        private T data;
        
        public LNode(T data) {
           this.data = data;
        }
        
        public LNode<T> getNext() { return next; }
        public LNode<T> getPrevious() { return previous; }
        public T getData() { return data; }
        public void setNext(LNode<T> next) { this.next = next; }
        public void setPrevious(LNode<T> previous) { this.previous = previous; }
    }  
    
}
