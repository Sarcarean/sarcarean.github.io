public interface ILinkedList<Comparable>
{ 
    public void add(int index, Comparable e);
    public void addFirst(Comparable e);
    public void addLast(Comparable e);   
    public void delete(int index);    
    public void deleteFirst();
    public void deleteLast();
    public int size();
    public void clear();
    public boolean contains(Comparable e);
    public Comparable get(int index);
    public Comparable getFirst();
    public Comparable getLast();  
}
    
    
    
   